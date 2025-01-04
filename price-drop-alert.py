import requests
import smtplib
from bs4 import BeautifulSoup

#here, paste the URL for the item that you would like to buy
URL = ""

#input the current price of the item
initial_price = 

#For the price_check function, input your User Agent into the "headers" variable. If that doesn't work, try inputting the following: 'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"

#in "search_price", after class, input the name of the element associated with the price on the website. To find out what this is, on the webpage, right-click on the price and select "inspect".

def price_check(URL):
  headers = {}
  response = requests.get(URL,headers=headers)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    search_price = soup.find("span", {"class", ""}).text
    new_price = float(search_price[1:])
    if new_price < initial_price:
      price_drop_alert(URL, new_price)
  else:
    error_alert(URL)
      
#For the functions below, in "server.login", input the email and password for the email address that you want to send the automated emails from. In "server.sendmail", input the sender's email adress, and then the recipient's email address.

def price_drop_alert(URL, new_price):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login("sender's email address", "sender's password")
  subject = 'Price Alert: ' + str(f'{new_price:.2f}')
  body = "Hooray! The item you want has reduced in price. Here's the link: " + URL
  msg = f"Subject:{subject}\n\n{body}".encode('utf8')
  server.sendmail("sender's email address", "recipient's email address", msg)
  server.quit()

def error_alert(URL):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login("sender's email address", "sender's password")
  subject = 'Error alert'
  body = "The item has been discontinued, or there was an error when accessing the webpage. Here's the link: " + URL
  msg = f"Subject:{subject}\n\n{body}".encode('utf8')
  server.sendmail("sender's email address", "recipient's email address", msg)
  server.quit()

price_check(URL)