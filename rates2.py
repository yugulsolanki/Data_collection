from bs4 import BeautifulSoup
import requests
import pandas as pd
abbrs = []
url = "https://www.gkquestionbank.com/list-of-different-currency-in-the-world/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
countries = soup.find_all("strong", {"class":""})
for country in range(3, (len(countries)-20), 2):
    abbrs.append(countries[country].text)
abbrs.remove('INR')
abbrs.remove('LTL')
abbrs.remove('VEF')
country_names = []
for country_name in range(4, (len(countries)-20), 2):
    country_names.append(countries[country_name].text)

country_names.remove(country_names[7])
country_names.remove(country_names[19])
country_names.remove(country_names[2])


To_INR = []
#url = "https://transferwise.com/gb/currency-converter/usd-to-inr-rate?amount=1"
for abbr in abbrs:
    url = "https://transferwise.com/gb/currency-converter/" + abbr + "-to-inr-rate?amount=1"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    INR = soup.find("span", {"class":"text-success"})
    #print(INR.text)
    To_INR.append(INR.text)

#print(country_names)
#print(abbrs)
#print(To_INR)

currency_rates = pd.DataFrame(
    {
        'Currency': country_names,
        'Abbrivation': abbrs,
        'To_INR': To_INR,
    })

print(currency_rates)
currency_rates.to_csv('currency_rates2.csv')
