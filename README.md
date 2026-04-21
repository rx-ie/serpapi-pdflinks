# Singapore Sustainability Report PDF Scraper

A simple Python script for collecting publicly available sustainability, ESG, and integrated report PDF links for Singapore companies using [SerpAPI](https://serpapi.com/).

This project is designed for quick research workflows in Google Colab or Python environments where you want to gather report links automatically and save them to a text file.

## Features

- Searches Google via SerpAPI
- Targets:
  - sustainability reports
  - ESG reports
  - annual sustainability reports
  - integrated reports
- Supports both:
  - broad Singapore-focused queries
  - company-specific queries
- Filters for PDF links only
- Deduplicates links automatically
- Exports all results to a `.txt` file

---

## Example Use Cases

- Building a dataset of sustainability reports
- ESG benchmarking research
- Collecting annual disclosures from Singapore-based firms
- Rapid PDF discovery for downstream document analysis

---

## Project Structure

```bash
.
├── sustainability_pdf_scraper.py
├── requirements.txt
├── README.md
└── .gitignore
