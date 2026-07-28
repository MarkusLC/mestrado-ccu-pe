#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(microdatasus)
  library(dplyr)
})

cat("Debugging SISCAN data format...\n")

tryCatch({
  cat("Pulling SIA-PA data (2018-2026, small sample)...\n")
  dados <- fetch_datasus(
    year_start = 2018,
    year_end = 2018,
    information_system = "SIA-PA"
  )

  if (is.null(dados)) {
    cat("ERROR: fetch_datasus returned NULL\n")
    quit(status = 1)
  }

  dados <- as.data.frame(dados)
  cat(sprintf("Fetched: %d rows, %d cols\n", nrow(dados), ncol(dados)))
  cat("First 10 columns:\n")
  print(names(dados)[1:10])

  if ("PA_DT_PROC" %in% colnames(dados)) {
    cat("\nPA_DT_PROC info:\n")
    cat("Type:", class(dados$PA_DT_PROC), "\n")
    cat("Sample values:\n")
    print(head(dados$PA_DT_PROC, 10))
  } else {
    cat("\nPA_DT_PROC not found. Available date-like columns:\n")
    date_cols <- names(dados)[grepl("DT|DATA|DATE", names(dados), ignore.case = TRUE)]
    print(date_cols)
  }

}, error = function(e) {
  cat("ERROR:", conditionMessage(e), "\n")
  quit(status = 1)
})
