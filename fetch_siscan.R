#!/usr/bin/env Rscript

# Fetch SISCAN (Citopatológico) data from DATASUS via microdatasus
# Aggregates by municipality and month, saves as JSON

suppressPackageStartupMessages({
  library(microdatasus)
  library(jsonlite)
  library(dplyr)
  library(tidyr)
})

cat("Fetching SISCAN data...\n")

tryCatch({
  # Fetch SIA (Ambulatorial) data — includes citopatológico
  # Using year_start and year_end; will fetch all available months
  dados <- fetch_datasus(
    year_start = 2018,
    year_end = 2026,
    information_system = "SIA"
  )

  cat("Raw data fetched. Processing...\n")

  # Parse if it's a DBC file
  if (is.null(dados)) {
    cat("ERROR: fetch_datasus returned NULL\n")
    quit(status = 1)
  }

  # Convert to data.frame if needed
  if (!is.data.frame(dados)) {
    dados <- as.data.frame(dados)
  }

  cat(sprintf("Rows: %d, Columns: %d\n", nrow(dados), ncol(dados)))
  cat("Columns:", paste(colnames(dados), collapse = ", "), "\n")

  # Filter for citopatológico (cervical cytology)
  # Look for procedure codes related to cytopathology
  # SISCAN citopatológico typically has specific codes

  if ("PA_PROC_ID" %in% colnames(dados)) {
    # Filter for cytopathology procedures (codes typically 020101, 020102, etc)
    dados_cito <- dados %>%
      filter(grepl("^0201", PA_PROC_ID, ignore.case = TRUE)) %>%
      select(any_of(c("PA_MUNOFN", "PA_AUTORIZ", "PA_DT_PROC")))
  } else {
    # If structure is different, keep all and let downstream handle it
    dados_cito <- dados
  }

  cat(sprintf("Filtered cytopathology records: %d\n", nrow(dados_cito)))

  # Aggregate by municipality and month
  if (nrow(dados_cito) > 0) {
    agregado <- dados_cito %>%
      mutate(
        ano_mes = format(as.Date(PA_DT_PROC, format = "%d%m%Y"), "%Y-%m"),
        municipio = PA_MUNOFN
      ) %>%
      group_by(municipio, ano_mes) %>%
      summarise(
        exames = n(),
        .groups = 'drop'
      ) %>%
      arrange(municipio, ano_mes)
  } else {
    cat("WARNING: No cytopathology records found. Creating empty structure...\n")
    agregado <- data.frame(
      municipio = character(),
      ano_mes = character(),
      exames = integer()
    )
  }

  # Ensure data directory exists
  dir.create("data", showWarnings = FALSE)

  # Save as JSON
  output_file <- "data/siscan_agregado.json"
  write_json(agregado, output_file, pretty = TRUE)

  cat(sprintf("✓ Data saved to %s\n", output_file))

  # Also save summary stats
  summary_stats <- list(
    total_exames = sum(agregado$exames, na.rm = TRUE),
    total_municipios = n_distinct(agregado$municipio),
    periodo = sprintf("%s a %s", min(agregado$ano_mes), max(agregado$ano_mes)),
    ultima_atualizacao = Sys.time()
  )

  write_json(summary_stats, "data/siscan_summary.json", pretty = TRUE)
  cat("✓ Summary stats saved\n")

  cat("\nSUCCESS: Data fetch complete\n")

}, error = function(e) {
  cat("ERROR:", conditionMessage(e), "\n")
  quit(status = 1)
})
