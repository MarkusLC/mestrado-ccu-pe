#!/usr/bin/env Rscript

# SISCAN Data Fetch — REAL DATA ONLY
# No fake data, no fallbacks to examples
# Direct fetch from DATASUS via microdatasus

suppressPackageStartupMessages({
  library(microdatasus)
  library(jsonlite)
  library(dplyr)
})

cat("🔄 SISCAN Fetch - REAL DATA ONLY\n")
cat("================================\n\n")

fetch_real_data <- function() {
  cat("📡 Connecting to DATASUS...\n")

  # SIA-PA = Procedimentos Ambulatoriais (includes citopatologia)
  dados <- fetch_datasus(
    year_start = 2018,
    year_end = 2026,
    information_system = "SIA-PA"
  )

  if (is.null(dados) || nrow(as.data.frame(dados)) == 0) {
    stop("DATASUS returned no data")
  }

  dados <- as.data.frame(dados)
  cat(sprintf("✅ Fetched: %d rows\n", nrow(dados)))

  # Filter for citopatologia (cervical cytology codes)
  # Codes: 020101, 020102, 020103, etc
  if ("PA_PROC_ID" %in% colnames(dados)) {
    cat("🔍 Filtering for citopatologia...\n")

    dados_cito <- dados %>%
      filter(grepl("^0201", as.character(PA_PROC_ID), ignore.case = TRUE)) %>%
      select(any_of(c("PA_MUNOFN", "PA_DT_PROC"))) %>%
      filter(!is.na(PA_MUNOFN), !is.na(PA_DT_PROC))

    cat(sprintf("✅ Found %d citopatologia records\n", nrow(dados_cito)))

    if (nrow(dados_cito) == 0) {
      stop("No citopatologia records found")
    }

    # Parse dates flexibly
    dados_cito <- dados_cito %>%
      mutate(
        ano_mes = tryCatch(
          format(as.Date(as.character(PA_DT_PROC), format = "%d%m%Y"), "%Y-%m"),
          error = function(e) {
            tryCatch(
              format(as.Date(as.character(PA_DT_PROC)), "%Y-%m"),
              error = function(e) NA_character_
            )
          }
        ),
        municipio = as.character(PA_MUNOFN)
      ) %>%
      filter(!is.na(ano_mes)) %>%
      select(municipio, ano_mes)

    # Aggregate
    agregado <- dados_cito %>%
      group_by(municipio, ano_mes) %>%
      summarise(exames = n(), .groups = 'drop') %>%
      arrange(municipio, ano_mes) %>%
      as.data.frame()

    return(agregado)
  } else {
    stop("PA_PROC_ID column not found in DATASUS response")
  }
}

tryCatch({
  agregado <- fetch_real_data()

  if (nrow(agregado) == 0) {
    stop("Aggregation resulted in empty dataset")
  }

  # Save
  dir.create("data", showWarnings = FALSE)

  write_json(agregado, "data/siscan_agregado.json", pretty = TRUE)
  cat(sprintf("✓ Saved %d records\n", nrow(agregado)))

  # Summary
  summary_json <- sprintf(
    '{\n  "total_exames": %d,\n  "total_municipios": %d,\n  "periodo": "%s a %s",\n  "ultima_atualizacao": "%s"\n}',
    sum(agregado$exames),
    length(unique(agregado$municipio)),
    min(agregado$ano_mes),
    max(agregado$ano_mes),
    format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ")
  )

  writeLines(summary_json, "data/siscan_summary.json")

  cat("\n✅ SUCCESS - REAL DATA ONLY\n")
  cat(sprintf("   %d exames\n", sum(agregado$exames)))
  cat(sprintf("   %d municipios\n", length(unique(agregado$municipio))))

}, error = function(e) {
  cat("\n❌ FATAL ERROR\n")
  cat(sprintf("   %s\n", conditionMessage(e)))
  cat("\nNo fallback to fake data. DATASUS must be reachable.\n")
  quit(status = 1)
})
