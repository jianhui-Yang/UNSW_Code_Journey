import requests
from bs4 import BeautifulSoup

print("=" * 40)
print(" SPIDER V1.0: RECON MISSION INITIALIZED ")
print("=" * 40)

target_url = "http://quotes.toscrape.com/"
print(f"Target URL: {target_url}")

response = requests.get(target_url)

if response.status_code == 200:
    print("Target locked. Commencing extraction...")
    soup = BeautifulSoup(response.text, "html.parser")
    all_quotes = soup.find_all("span", class_= "text")
    print("--- 🎯 EXTRACTION SUCCESSFUL ---")
    print(f"Total targets locked: {len(all_quotes)}\n")
    for i, quote in enumerate(all_quotes):
        print(f"Data [{i+1}]: {quote.text}")
    print("--------------------------------")

else:
    print(f"[!] Mission Failed. Status Code: {response.status_code}")