# Singapore Sustainability Report PDF Scraper

A simple Python script for collecting publicly available sustainability, ESG, and integrated report PDF links for Singapore companies using [SerpAPI](https://serpapi.com/). Change the code to get PDF links for any topic/company you want.

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

# Installation

### Option 1: Google Colab
Install the dependency in a Colab cell:

```python
!pip install google-search-results
```

### Option 2: Local Python Environment
```bash
pip install -r requirements.txt
```

# Requirements
* Python 3.8+
* SerpAPI account and API key

# Setup

### 1. Get a SerpAPI key
Sign up at: [https://serpapi.com/](https://serpapi.com/)

### 2. Add your API key
In the script, replace:

```python
SERPAPI_KEY = "YOUR_API_KEY_HERE"
```
with your actual key.

**Recommended:** use an environment variable instead of hardcoding your key.

Example:

```python
import os
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
```
Then set it in your environment:

```bash
export SERPAPI_KEY="your_actual_key"
```

# Usage
Run the script in Colab or locally.

### Google Colab
Paste the script into a notebook and run the cells.

### Local
```bash
python sustainability_pdf_scraper.py
```

The script will:
* Run a set of broad search queries
* Run company-specific search queries
* Collect PDF links from the search results
* Save them into:
  ```bash
  sustainability_pdfs.txt
  ```

# Default Search Queries
The script currently uses these broad queries:
* `site:sg sustainability report filetype:pdf`
* `Singapore ESG report filetype:pdf`
* `annual sustainability report Singapore company filetype:pdf`
* `integrated report Singapore filetype:pdf`

And these company-specific searches:
* DBS
* OCBC
* UOB
* SIA
* Keppel
* CapitaLand

# Output
Output is saved as:

```bash
sustainability_pdfs.txt
```
Each line contains one unique PDF link.

**Example:**

```text
https://www.example.com/report1.pdf
https://www.example.com/report2.pdf
https://www.example.com/report3.pdf
```

# Notes
* SerpAPI usage may incur costs depending on your plan.
* Search results depend on Google indexing and availability.
* Not every sustainability report may appear in results.
* Some URLs may later become inactive or redirect.

# Limitations
* Only returns links visible in SerpAPI's Google search results
* Only collects direct links containing `.pdf`
* Does not validate whether the PDF is actually a sustainability report
* Does not download PDFs themselves, only saves URLs

# Possible Improvements
- [ ] Add pagination to collect more than 10 results per query
- [ ] Validate URLs before saving
- [ ] Download PDFs automatically
- [ ] Export to CSV/JSON
- [ ] Add metadata like title, snippet, and source domain
- [ ] Support more countries and companies
- [ ] Add retry handling and logging

# Security
**Do not commit your API key to GitHub.**

If publishing this project:
* Remove hardcoded credentials
* Use environment variables
* Consider adding a `.env` workflow

# License
MIT License
