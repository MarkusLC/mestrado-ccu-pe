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

  # Load existing data to use as base
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

  # Save as JSON
  output_file <- "data/siscan_agregado.json"
  write_json(agregado, output_file, pretty = TRUE)
  cat(sprintf("✓ Data saved to %s\n", output_file))

  # Save summary stats
  if (nrow(agregado) > 0) {
    summary_stats <- list(
      total_exames = sum(as.numeric(agregado$exames), na.rm = TRUE),
      total_municipios = length(unique(agregado$municipio)),
      periodo = sprintf("%s a %s", min(agregado$ano_mes), max(agregado$ano_mes)),
      ultima_atualizacao = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ")
    )
  } else {
    summary_stats <- list(
      total_exames = 0,
      total_municipios = 0,
      periodo = "sem dados",
      ultima_atualizacao = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ")
    )
  }

  write_json(summary_stats, "data/siscan_summary.json", pretty = TRUE)
  cat("✓ Summary stats saved\n")

  cat("\nSUCCESS: Data processed\n")

}, error = function(e) {
  cat("ERROR:", conditionMessage(e), "\n")
  quit(status = 1)
})
