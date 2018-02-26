import requests
import bs4
import pandas as pd
import csv

def getProfilePage(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Profile")

    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    desc = pageSoup.select("textarea[name='profile']")[0].text
    paypal_email = pageSoup.select("input[name='PaypalEmail']")[0].get('value')
    print(desc, paypal_email)
    return desc, paypal_email

def getSellerName(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Dashboard")

    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    storeName = pageSoup.select("body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > h5 > a")[0].text.strip()
    customerName = pageSoup.select("body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > p")[0].text
    print(storeName, customerName)
    return storeName, customerName

def getInbox(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Inbox")
    messageData = []
    inboxdata = pd.read_html(page.text)[0]
    #inboxTable.to_csv("inbox.csv", header = False, index = False)
    # pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    # inboxTable = pageSoup.select(".unread")
    # table = pd.read_html(inboxTable[0])
    return inboxdata

