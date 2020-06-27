from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv


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

url = "https://www.x-rates.com/table/?from=INR&amount=1"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
countries = soup.find_all("td", {"class":""})
Other_currency = []
for country in range(10, len(countries)):
    Other_currency.append(countries[country].text)


df4 = pd.DataFrame(
    {
        'Currency': Other_currency,
    })

df1 = pd.DataFrame(
        {
            'Currencies': country_names,
            'Short Form': abbrs,
        })

df3 = pd.DataFrame(
        {
            'Currencies': country_names,
            'Short Form': abbrs,
        })



def home(request):
    return render(request, 'currency/home.html')


def transferwise(request):
    To_INR = []
    for abbr in abbrs:
        url = "https://transferwise.com/gb/currency-converter/inr-to-" + abbr + "-rate?amount=1"
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        INR = soup.find("span", {"class":"text-success"})
        To_INR.append(INR.text)

    localtime = time.asctime( time.localtime(time.time()) )
    df2 = pd.DataFrame(
        {
            localtime: To_INR,
        })
    df1[localtime] = df2
    df1.to_csv('mydata1.csv')
    a = pd.read_csv("mydata1.csv")
    a.to_html("Table1.html")
    html_file = a.to_html()
    return render(request, 'currency/transferwise.html', {'html_file':html_file})


def iban(request):
    To_INR = []
    for abbr in abbrs:
        url = "https://www.iban.com/currency-converter?from_currency=INR&to_currency=" + abbr + "&amount=1"
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        rates = soup.find_all("strong", {"strong":""})
        To_INR.append(rates[1].text)

    localtime = time.asctime( time.localtime(time.time()) )
    df2 = pd.DataFrame(
        {
            localtime: To_INR,
        })
    df3[localtime] = df2
    df3.to_csv('mydata2.csv')
    a = pd.read_csv("mydata2.csv")
    a.to_html("Table2.html")
    html_file = a.to_html()
    return render(request, 'currency/iban.html', {'html_file':html_file})



def xrates(request):
    url = "https://www.x-rates.com/table/?from=INR&amount=1"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    To_INR = []
    values = soup.find_all("td", {"class":"rtRates"})
    for value in range(20, len(values), 2):
        To_INR.append(values[value].text)

    localtime = time.asctime( time.localtime(time.time()) )
    df2 = pd.DataFrame(
        {
            localtime: To_INR,
        })

    df4[localtime] = df2
    df4.to_csv('mydata3.csv')
    a = pd.read_csv("mydata3.csv")
    a.to_html("Table3.html")
    html_file = a.to_html()
    return render(request, 'currency/xrates.html', {'html_file':html_file})