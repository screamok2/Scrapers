import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://shiny-diski.com.ua"
n = 1
result = []

while n < 10:
    url = f"{base_url}/uk/tires?start={n}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    prices = soup.find_all("span", class_="standard-price js-price-sorting")
    names = soup.find_all("a", class_="product-card__title js-product-name")

    for name, price in zip(names, prices):
        result.append({
            "name": name.text.strip(),
            "price": price.text.strip(),})

    for i in result:
        print(i["name"])

    n=n+1
df = pd.DataFrame(result)
print(f"Added {len(result)}")

excel_filename = "qeq.xlsx"
df.to_excel(excel_filename, index=False)
