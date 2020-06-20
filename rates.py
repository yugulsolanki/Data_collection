from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.x-rates.com/table/?from=INR&amount=1"
response = requests.get(url)
#print(response)
data = response.text
#print(data)
soup = BeautifulSoup(data, 'html.parser')
#items = soup.find("table", {"class":"tablesorter ratesTable"})
countries = soup.find_all("td", {"class":""})
Other_currency = []
for country in range(10, len(countries)):
    Other_currency.append(countries[country].text)

INR = []
values = soup.find_all("td", {"class":"rtRates"})
for value in range(21, len(values), 2):
    INR.append(values[value].text)

#print((INR))
#print((Other_currency))

currency_rates = pd.DataFrame(
    {
        'Other_currency': Other_currency,
        'Indian_rates': INR,
    })

print(currency_rates)
currency_rates.to_csv('currency_rates.csv')
