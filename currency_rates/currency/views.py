from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

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




#print(currency_rates)
#currency_rates.to_csv('currency_rates2.csv')

arr = [12, 12.3, 6.7, 89, 5, 8]
arr2 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','POR']
#pd.concat([student_df1, temperature_df4])
def home(request):
    To_INR = []
    for abbr in abbrs:
        url = "https://transferwise.com/gb/currency-converter/" + abbr + "-to-inr-rate?amount=1"
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        INR = soup.find("span", {"class":"text-success"})
        To_INR.append(INR.text)

    localtime = time.asctime( time.localtime(time.time()) )
    currency_rates = pd.DataFrame(
        {
            'Currencies': country_names,
            'Short Form': abbrs,
            localtime: To_INR,
        })
    return render(request, 'currency/home.html', {'country_names':country_names, 'abbrs':abbrs, 'To_INR':To_INR, 'localtime':localtime})