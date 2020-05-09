from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

product = input("Enter the Product: ")
product = product.replace(' ', '%20')

urlname = "https://www.flipkart.com/search?q=" + product + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
print(urlname)
try:
    page = urlopen(urlname)
except:
    print('Error in page loading..')
soup = BeautifulSoup(page, 'html.parser')


products = []
prices = []
for i in soup.findAll('div', {'class': '_3O0U0u'}):
    
    name = i.find('div', {'class': '_3wU53n'})

    price=i.find('div',{'class':'_1vC4OE _2rQ-NK'})
    products.append(name)
    prices.append(price)
    

df=DataFrame({'Products':products,'Prices':prices})
print(df)
