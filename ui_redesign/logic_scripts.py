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

def getOrders(NetworkSession):

    orders_page = NetworkSession.get("https://www.hangarswap.com/Seller/OrderHistory")

    orders_list = []

    try:
        orders_list = pd.read_html(orders_page.text)[0]
    except:
        pass

    return orders_list

def getInbox(NetworkSession):
    inbox_page = NetworkSession.get("https://www.hangarswap.com/Seller/Inbox")
    unread_page = NetworkSession.get("https://www.hangarswap.com/Seller/Inbox?View=UnRead")
    sent_page = NetworkSession.get("https://www.hangarswap.com/Seller/Inbox?View=Sent")
    trash_page = NetworkSession.get("https://www.hangarswap.com/Seller/Inbox?View=Trash")

    inbox_list = []
    unread_list = []
    sent_list = []
    trash_list = []

    try:
        inbox_data = pd.read_html(inbox_page.text)[0]
        unread_data = pd.read_html(unread_page.text)[0]
        sent_data = pd.read_html(sent_page.text)[0]
        trash_data = pd.read_html(trash_page.text)[0]
    except IndexError:
        pass

    try:
        inbox_list = inbox_data.values.tolist()
        unread_list = unread_data.values.tolist()
        sent_list = sent_data.values.tolist()
        trash_list = trash_data.values.tolist()
    except:
        pass

    return inbox_list, unread_list, sent_list, trash_list

def getCatalog(NetworkSession):
    active_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog")
    inactive_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog?View=Inactive")

    active_catalog_df = pd.read_html(active_catalog_page.text)[0]
    inactive_catalog_df = pd.read_html(inactive_catalog_page.text)[0]

    active_list = active_catalog_df.values.tolist()
    inactive_list = inactive_catalog_df.values.tolist()

    merged_catalog = active_list + inactive_list

    catalog_headers = list(active_catalog_df.columns.values)

    return merged_catalog, catalog_headers

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