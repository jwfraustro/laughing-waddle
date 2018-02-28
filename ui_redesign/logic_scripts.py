import requests
import bs4
import pandas as pd
import csv
from PyQt5.QtGui import QPixmap


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
    inboxdata = pd.read_html(page.text)[0]
    #inboxTable.to_csv("inbox.csv", header = False, index = False)
    # pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    # inboxTable = pageSoup.select(".unread")
    # table = pd.read_html(inboxTable[0])
    return inboxdata

def getCatalog(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog")
    catalog_data = pd.read_html(page.text)[0]
    return catalog_data

def getNewestListings(NetworkSession):

    #s = requests.Session()

    page = NetworkSession.get("http://www.hangarswap.com/Shop/index")
    pageSoup = bs4.BeautifulSoup(page.content, "html.parser")

    product1 = {
        "img" : ("http://www.hangarswap.com" + pageSoup.select(".fp_images.relative img")[0].attrs['src']),
        "title" : str(pageSoup.select("figure a")[0].contents[0]),
        "price" : str(pageSoup.select(".fp_price.with_ie")[0].contents[0])
    }

    product2 = {
        "img": ("http://www.hangarswap.com" + pageSoup.select(".fp_images.relative img")[2].attrs['src']),
        "title": str(pageSoup.select("figure a")[1].contents[0]),
        "price": str(pageSoup.select(".fp_price.with_ie")[1].contents[0])
    }

    product3 = {
        "img": ("http://www.hangarswap.com" + pageSoup.select(".fp_images.relative img")[4].attrs['src']),
        "title": str(pageSoup.select("figure a")[2].contents[0]),
        "price": str(pageSoup.select(".fp_price.with_ie")[2].contents[0])

    }

    product4 = {
        "img": ("http://www.hangarswap.com" + pageSoup.select(".fp_images.relative img")[6].attrs['src']),
        "title": str(pageSoup.select("figure a")[3].contents[0]),
        "price": str(pageSoup.select(".fp_price.with_ie")[3].contents[0])
    }

    pixmap1 = QPixmap()
    pixmap2 = QPixmap()
    pixmap3 = QPixmap()
    pixmap4 = QPixmap()

    pixmap1.loadFromData(NetworkSession.get(product1['img']).content)
    pixmap2.loadFromData(NetworkSession.get(product2['img']).content)
    pixmap3.loadFromData(NetworkSession.get(product3['img']).content)
    pixmap4.loadFromData(NetworkSession.get(product4['img']).content)

    pixmap1 = QPixmap(pixmap1.scaled(150, 150))
    pixmap2 = QPixmap(pixmap2.scaled(150, 150))
    pixmap3 = QPixmap(pixmap3.scaled(150, 150))
    pixmap4 = QPixmap(pixmap4.scaled(150, 150))

    product1['img'] = pixmap1
    product2['img'] = pixmap2
    product3['img'] = pixmap3
    product4['img'] = pixmap4

    return (product1, product2, product3, product4)