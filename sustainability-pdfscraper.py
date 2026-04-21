# STEP 1: Install SerpAPI library
# Run this in a separate Colab cell if possible:
# !pip install google-search-results

# STEP 2: Imports
from serpapi import GoogleSearch
from google.colab import files

# STEP 3: Put your SerpAPI key here
SERPAPI_KEY = "YOUR_API_KEY_HERE"

# STEP 4: Search queries (broad + targeted)
queries = [
    "site:sg sustainability report filetype:pdf",
    "Singapore ESG report filetype:pdf",
    "annual sustainability report Singapore company filetype:pdf",
    "integrated report Singapore filetype:pdf"
]

companies = ["DBS", "OCBC", "UOB", "SIA", "Keppel", "CapitaLand"]

# STEP 5: Function to run search
def get_pdf_links(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 10
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    links = []
    
    # Safely extract organic results
    for item in results.get("organic_results", []):
        link = item.get("link", "")
        if ".pdf" in link.lower():  # Added .lower() to catch .PDF extensions
            links.append(link)
            
    return links

# STEP 6: Collect all links
pdf_links = set() # Using a set prevents duplicate links

# Run general queries
for q in queries:
    print(f"Searching: {q}")
    links = get_pdf_links(q)
    pdf_links.update(links)

# Run company-specific queries
for c in companies:
    q = f"{c} sustainability report filetype:pdf"
    print(f"Searching: {q}")
    links = get_pdf_links(q)
    pdf_links.update(links)

# STEP 7: Save results to file
file_name = "sustainability_pdfs.txt"

with open(file_name, "w") as f:
    for link in pdf_links:
        f.write(link + "\n")

print(f"\nSaved {len(pdf_links)} unique PDF links to {file_name}")

# STEP 8: Download file
files.download(file_name)
