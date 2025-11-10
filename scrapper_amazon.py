import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8"
}
base_url = "https://www.amazon.de/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm"
#n = 1
result = []

#while n < 10:
url = f"https://www.amazon.de/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

prices = [el.get_text(strip=True) for el in soup.select("._cDEzb_p13n-sc-css-line-clamp-3_g3dy1")]
names = [el.get_text(strip=True) for el in soup.select("._cDEzb_p13n-sc-price_3mJ9Z")]

for name, price in zip(names, prices):
    result.append({
        "name": name,
        "price": price})

for i in result:
    print(i["name"])

    #n=n+1
df = pd.DataFrame(result)
print(f"Added {len(result)}")
# Save to xlsx
excel_filename = "qeq.xlsx"
df.to_excel(excel_filename, index=False)
