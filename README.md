# Data_collection

Agenda : Scrapping data from forex websites to form dataset.

Project Name : currency_rates
App Name : Currency

Inside views , we have 4 functions : home, transferwise, iban, xrates

"home" function renders home.html which contain 3 links to html files which shows forex rates from perticular websites.

"transferwise" function scraps the required data from https://transferwise.com , converts it in csv file and renders it in transferwise.html

"iban" function scraps the required data from https://iban.com , converts it in csv file and renders it in iban.html

"xrates" function scraps the required data from https://x-rates.com , converts it in csv file and renders it in xrates.html

Whenever we refresh our data rendering templates, new data get added in a new column, so that we can also see previous data.
