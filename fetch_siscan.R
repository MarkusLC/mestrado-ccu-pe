#!/usr/bin/env Rscript

# Fetch SISCAN (Citopatológico) data from DATASUS via microdatasus
# Aggregates by municipality and month, saves as JSON

suppressPackageStartupMessages({
  library(microdatasus)
  library(jsonlite)
  library(dplyr)
})

cat("Fetching SISCAN data from DATASUS...\n")

tryCatch({
  # Fetch SIA (Ambulatorial) data — includes citopatológico
  cat("Pulling SIA data (2018-2026)...\n")
  dados <- fetch_datasus(
    year_start = 2018,
    year_end = 2026,
    information_system = "SIA"
  )

  cat("Raw data fetched. Processing...\n")

  if (is.null(dados)) {
    cat("ERROR: fetch_datasus returned NULL\n")
    quit(status = 1)
  }

  # Convert to data.frame if needed
  if (!is.data.frame(dados)) {
    dados <- as.data.frame(dados)
  }

  cat(sprintf("Rows: %d, Columns: %d\n", nrow(dados), ncol(dados)))
  cat("Columns:", paste(head(colnames(dados), 10), collapse = ", "), "...\n")

  # Filter for citopatológico (cervical cytology)
  # SISCAN procedure codes typically start with 0201
  if ("PA_PROC_ID" %in% colnames(dados)) {
    dados_cito <- dados %>%
      filter(grepl("^0201", PA_PROC_ID, ignore.case = TRUE)) %>%
      select(any_of(c("PA_MUNOFN", "PA_DT_PROC"))) %>%
      filter(!is.na(PA_MUNOFN), !is.na(PA_DT_PROC))

    cat(sprintf("Filtered to cytopathology: %d records\n", nrow(dados_cito)))

    # Aggregate by municipality and month
    if (nrow(dados_cito) > 0) {
      agregado <- dados_cito %>%
        mutate(
          ano_mes = format(as.Date(PA_DT_PROC, format = "%d%m%Y"), "%Y-%m"),
          municipio = PA_MUNOFN
        ) %>%
        group_by(municipio, ano_mes) %>%
        summarise(exames = n(), .groups = 'drop') %>%
        arrange(municipio, ano_mes) %>%
        as.data.frame()
    } else {
      cat("WARNING: No cytopathology records found\n")
      agregado <- data.frame(
        municipio = character(),
        ano_mes = character(),
        exames = integer()
      )
    }
  } else {
    cat("WARNING: PA_PROC_ID not found. Using all records.\n")
    agregado <- dados %>%
      select(any_of(c("PA_MUNOFN", "PA_DT_PROC"))) %>%
      filter(!is.na(PA_MUNOFN), !is.na(PA_DT_PROC)) %>%
      mutate(
        ano_mes = format(as.Date(PA_DT_PROC, format = "%d%m%Y"), "%Y-%m"),
        municipio = PA_MUNOFN
      ) %>%
      group_by(municipio, ano_mes) %>%
      summarise(exames = n(), .groups = 'drop') %>%
      arrange(municipio, ano_mes) %>%
      as.data.frame()
  }

  cat(sprintf("Final aggregated records: %d\n", nrow(agregado)))

  # Ensure data directory exists
  dir.create("data", showWarnings = FALSE)

  # Save aggregated data as JSON
  output_file <- "data/siscan_agregado.json"
  write_json(agregado, output_file, pretty = TRUE)
  cat(sprintf("✓ Data saved to %s\n", output_file))

  # Calculate summary
  if (nrow(agregado) > 0) {
    total_exames <- sum(as.numeric(agregado$exames), na.rm = TRUE)
    total_municipios <- length(unique(agregado$municipio))
    periodo <- sprintf("%s a %s", min(agregado$ano_mes), max(agregado$ano_mes))
  } else {
    total_exames <- 0
    total_municipios <- 0
    periodo <- "sem dados"
  }

  # Build JSON summary
  json_str <- sprintf(
    '{\n  "total_exames": %d,\n  "total_municipios": %d,\n  "periodo": "%s",\n  "ultima_atualizacao": "%s"\n}',
    as.integer(total_exames),
    as.integer(total_municipios),
    as.character(periodo),
    as.character(format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ"))
  )

  writeLines(json_str, "data/siscan_summary.json")
  cat(sprintf("✓ Summary: %d exames, %d municípios, %s\n", total_exames, total_municipios, periodo))

  cat("\n✅ SUCCESS: Data fetch complete\n")

}, error = function(e) {
  cat("❌ ERROR:", conditionMessage(e), "\n")
  cat("Falling back to existing data...\n")

  # Fallback: use existing data
  if (file.exists("data/siscan_agregado.json")) {
    cat("Using cached data\n")
  } else {
    cat("No cached data available\n")
    quit(status = 1)
  }
})
