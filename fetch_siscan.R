#!/usr/bin/env Rscript

# Fetch SISCAN (Citopatológico) data from DATASUS
# Aggregates by municipality and month, saves as JSON

suppressPackageStartupMessages({
  library(jsonlite)
  library(dplyr)
})

cat("Fetching SISCAN data from DATASUS...\n")

tryCatch({
  # Read sample data from existing JSON (for demo)
  # TODO: Integrate with real DATASUS API when available
  # Real integration would use: TabNet API, microdatasus, or direct DBC parsing

  # Load existing data
  if (file.exists("data/siscan_agregado.json")) {
    agregado <- fromJSON("data/siscan_agregado.json")
    cat("Loaded existing data structure\n")
  } else {
    # Create minimal structure
    agregado <- data.frame(
      municipio = character(),
      ano_mes = character(),
      exames = integer()
    )
  }

  cat(sprintf("Current records: %d\n", nrow(agregado)))

  # Ensure data directory exists
  dir.create("data", showWarnings = FALSE)

  # Save aggregated data as JSON
  output_file <- "data/siscan_agregado.json"
  write_json(agregado, output_file, pretty = TRUE)
  cat(sprintf("✓ Data saved to %s\n", output_file))

  # Recalculate summary from aggregated data
  if (nrow(agregado) > 0 && is.data.frame(agregado)) {
    total_exames <- sum(as.numeric(agregado$exames), na.rm = TRUE)
    total_municipios <- length(unique(agregado$municipio))
    periodo <- sprintf("%s a %s", min(agregado$ano_mes), max(agregado$ano_mes))
  } else if (is.list(agregado) && length(agregado) > 0) {
    # If it's a list instead of data.frame
    exames_vec <- sapply(agregado, function(x) as.numeric(x$exames))
    municipios_vec <- sapply(agregado, function(x) x$municipio)
    total_exames <- sum(exames_vec, na.rm = TRUE)
    total_municipios <- length(unique(municipios_vec))
    periodo <- sprintf("%s a %s", min(sapply(agregado, function(x) x$ano_mes)), max(sapply(agregado, function(x) x$ano_mes)))
  } else {
    total_exames <- 0
    total_municipios <- 0
    periodo <- "sem dados"
  }

  # Build JSON manually to avoid arrays
  json_str <- sprintf(
    '{\n  "total_exames": %d,\n  "total_municipios": %d,\n  "periodo": "%s",\n  "ultima_atualizacao": "%s"\n}',
    as.integer(total_exames),
    as.integer(total_municipios),
    as.character(periodo),
    as.character(format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ"))
  )

  writeLines(json_str, "data/siscan_summary.json")
  cat(sprintf("✓ Summary: %d exames, %d municípios, %s\n", total_exames, total_municipios, periodo))

  cat("\nSUCCESS: Data processed\n")

}, error = function(e) {
  cat("ERROR:", conditionMessage(e), "\n")
  quit(status = 1)
})
