import requests
import bs4
import pandas as pd
import imghdr
import csv
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from requests_toolbelt.multipart.encoder import MultipartEncoder

airboat_subcats = [

    'Airboats',
    'Engines',
    'Hulls',
    'Other',
    'Parts'
]
aircraft_for_sale_subcats = [

    'Aircraft for Sale',
    'Amphibian',
    'Helicopters',
    'Other',
    'Projects',
    'Singles',
    'Twins',
]
airframe_subcats=[
    'Aerobatic',
    'Aeronca',
    'Amphibian',
    'Antique',
    'Beechcraft',
    'Bellanca',
    'Cessna',
    'Cirrus',
    'Control Surfaces',
    'General Parts',
    'Helicopter',
    'Interior',
    'Luscombe',
    'Mooney',
    'Other',
    'Piper',
    'Taylorcraft',
    'Warbird',
]
avionics_subcats = [
    'Antennas',
    'Audio Panels',
    'AutoPilot',
    'ELTs',
    'Engine Monitors',
    'GPS',
    'Indicators',
    'Intercom',
    'Nav/Coms',
    'Other',
    'Packages',
    'Pitot Tubes',
    'Transponders',
    'Trays & Connectors',
    'Weather Systems'
]
electrical_subcats = [
    'Batteries',
    'Lighting',
    'Other'
]
hardware_subcats = [
    'Jacks',
    'Nuts & Bolts',
    'Other',
    'Rivets',
    'Testing Equipment',
    'Tools'
]
gear_subcats = [
    'Amphibian',
    'Skis',
    'Tailwheel',
    'Tires & Tubes',
    'Wheels & Brakes'
]
pilot_supp_subcats = [
    'Aviator Accessories',
    'Bags',
    'Books',
    'Collectibles',
    'Cover & Accessories',
    'Headsets',
    'Manuals',
    'Oils, Liquids, & Sprays',
    'Other',
    'Pilot Wear',
    'Safety',
    'Stickers & Decals',
    'Tow'

]
powerplant_subcats = [
    'Engine Parts',
    'Engines',
    'Environmental',
    'Exhaust',
    'Fuel System',
    'General Parts',
    'Propellers'
]


def getProfilePage(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Profile")

    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    desc = pageSoup.select("textarea[name='profile']")[0].text
    paypal_email = pageSoup.select("input[name='PaypalEmail']")[0].get('value')
    print(desc, paypal_email)
    return desc, paypal_email

def getSellerName(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Dashboard", verify = False)

    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    storeName = pageSoup.select("body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > h5 > a")[0].text.strip()
    customerName = pageSoup.select("body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > p")[0].text
    print(storeName, customerName)
    return storeName, customerName

def getOrders(NetworkSession):

    orders_page = NetworkSession.get("https://www.hangarswap.com/Seller/OrderHistory")

    orders_list = []

    try:
        orders_list_df = pd.read_html(orders_page.text)[0]
        orders_list = orders_list_df.values.tolist()
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

def validateForm(form_data):

    if not form_data['productName']:
        return 'Product Name'
    if not form_data['productDescription']:
        return 'Product Description'
    if not form_data['CategoryID']:
        return 'Product Category'
    if not form_data['productCondition']:
        return 'Product Condition'
    if not form_data['Qty']:
        return 'Quantity Available'
    if not form_data['Price']:
        return 'Price'
    if not form_data['ShippingCost']:
        return 'Shipping Cost'
    return 0

def submitItem(item_form, img_names, NetworkSession):
    # encode product dictionary into multi-part/form
    product_data = MultipartEncoder(fields=item_form, boundary='-----WebKitFormBoundarymkISNjkugjjFZdvE')

    # making the post to submit listing
    t = NetworkSession.post('https://www.hangarswap.com/Seller/SaveProduct', data=product_data,
               headers={'Content-Type': product_data.content_type})

    # checks if there is more than one image in the upload list
    if (len(img_names) > 1):

        # checks to see what productID HS has assigned the item, and grabs it
        soup = bs4.BeautifulSoup(t.text, "html.parser")
        pr_id = soup.select('[href*="ProductID"]')[0].get("href")[-5:].strip("=")

        # iterates through image upload list and hits 'AddAditionalPhotos' successively
        for i in range(2, len(img_names) + 1):
            # encoding, determining image type and uploading
            photo_form = MultipartEncoder(
                fields={
                    'productid': str(pr_id),
                    'ProductImage': (
                        'filename', open(img_names['img' + str(i) + '_lbl'], 'rb'),
                        ('image/' + str(imghdr.what(img_names['img' + str(i) + '_lbl'])))),
                }, boundary='-----WebKitFormBoundarydMG06kgczAncwn4B')
            t = NetworkSession.post('https://www.hangarswap.com/Seller/SaveExtraImages', data=photo_form,
                       headers={'Content-Type': photo_form.content_type})

    return

