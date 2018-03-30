from bs4 import BeautifulSoup
import pandas as pd
import imghdr
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIcon
import logging
from modular_product_test import Ui_newListing as ProductForm
from requests_toolbelt.multipart.encoder import MultipartEncoder
import csv
from random import randint

username = ""

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
airframe_subcats = [
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

    pageSoup = BeautifulSoup(page.text, "html.parser")
    desc = pageSoup.select("textarea[name='profile']")[0].text
    paypal_email = pageSoup.select("input[name='PaypalEmail']")[0].get('value')
    print(desc, paypal_email)
    return desc, paypal_email


def getSellerName(NetworkSession):
    page = NetworkSession.get("https://www.hangarswap.com/Seller/Dashboard", verify=False)

    pageSoup = BeautifulSoup(page.text, "html.parser")
    storeName = pageSoup.select(
        "body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > h5 > a")[
        0].text.strip()
    customerName = pageSoup.select(
        "body > div > div.site-content > div > div > div.row.row-md.mb-1 > div.col-md-4 > div > div.u-content > p")[
        0].text
    print(storeName, customerName)
    return storeName, customerName


def getOrders(NetworkSession):
    orders_page = NetworkSession.get("https://www.hangarswap.com/Seller/OrderHistory", verify=False)

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


def getActiveCatalog(NetworkSession):
    active_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog")
    active_catalog_df = pd.read_html(active_catalog_page.text)[0]
    active_list = active_catalog_df.values.tolist()
    catalog_headers = list(active_catalog_df.columns.values)

    return active_list, catalog_headers


def getInactiveCatalog(NetworkSession):
    inactive_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog?View=Inactive")
    inactive_catalog_df = pd.read_html(inactive_catalog_page.text)[0]
    inactive_list = inactive_catalog_df.values.tolist()
    inactive_headers = list(inactive_catalog_df.columns.values)

    return inactive_list, inactive_headers


def getDisabledCatalog(NetworkSession):
    disabled_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog?View=Disabled")
    disabled_catalog_df = pd.read_html(disabled_catalog_page.text)[0]
    disabled_list = disabled_catalog_df.values.tolist()
    disabled_headers = list(disabled_catalog_df.columns.values)

    return disabled_list, disabled_headers


def getSoldCatalog(NetworkSession):
    sold_catalog_page = NetworkSession.get("https://www.hangarswap.com/Seller/Catalog?View=Sold")
    sold_catalog_df = pd.read_html(sold_catalog_page.text)[0]
    sold_list = sold_catalog_df.values.tolist()
    sold_headers = list(sold_catalog_df.columns.values)

    return sold_list, sold_headers


def getNewestListings(NetworkSession):
    # s = requests.Session()

    page = NetworkSession.get("http://www.hangarswap.com/Shop/index")
    pageSoup = BeautifulSoup(page.content, "html.parser")

    product1 = {
        "img": ("http://www.hangarswap.com" + pageSoup.select(".fp_images.relative img")[0].attrs['src']),
        "title": str(pageSoup.select("figure a")[0].contents[0]),
        "price": str(pageSoup.select(".fp_price.with_ie")[0].contents[0])
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

    return product1, product2, product3, product4

def submitItem(item_form, img_names, NetworkSession):
    # encode product dictionary into multi-part/form
    product_data = MultipartEncoder(fields=item_form, boundary='-----WebKitFormBoundarymkISNjkugjjFZdvE')

    # making the post to submit listing
    t = NetworkSession.post('https://www.hangarswap.com/Seller/SaveProduct', data=product_data,
                            headers={'Content-Type': product_data.content_type})

    # checks if there is more than one image in the upload list
    if (len(img_names) > 1):

        # checks to see what productID HS has assigned the item, and grabs it
        soup = BeautifulSoup(t.text, "html.parser")
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


def savePendingProduct(item_form, img_names):
    with open("pend.dat", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([
            randint(0, 2147483647),
            item_form['productName'],
            item_form['productDescription'],
            item_form['CategoryID'],
            item_form['productCondition'],
            item_form['Qty'],
            item_form['PartNumber'],
            item_form['APN'],
            item_form['SerialNumber'],
            item_form['SKU'],
            item_form['Manufacturer'],
            item_form['Price'],
            item_form['ShippingCost'],
            item_form['HasCore'],
            item_form['CoreCharge'],
            item_form['Active'],
            item_form['OnSale'],
            item_form['AllowBestOffer'],
            item_form['Featured']
        ])
    return

def launchProductDialog(username, NetworkSession):
    img_names = {}

    dialog = QtWidgets.QDialog()
    dialog.ui = ProductForm()
    dialog.ui.setupUi(dialog)

    dialog.ui.img_upload_btn.clicked.connect(lambda: insertImages())
    dialog.ui.upload_new_button.clicked.connect(lambda: parseProductForm("upload", username, NetworkSession))
    dialog.ui.save_templ_button.clicked.connect(lambda: parseProductForm("save", username, NetworkSession))
    dialog.ui.cancel_new_button.clicked.connect(lambda: dialog.done(0))

    dialog.ui.cat_options.currentTextChanged.connect(lambda: changedCat())

    dialog.ui.img1_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img2_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img3_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img4_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img5_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img6_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img7_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img8_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img9_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())
    dialog.ui.img10_lbl.customContextMenuRequested.connect(lambda: contextMenuEvent())

    dialog.ui.img1_lbl.setScaledContents(True)
    dialog.ui.img2_lbl.setScaledContents(True)
    dialog.ui.img3_lbl.setScaledContents(True)
    dialog.ui.img4_lbl.setScaledContents(True)

    dialog.ui.core_btnGroup = QtWidgets.QButtonGroup()
    dialog.ui.core_btnGroup.setObjectName("core_btnGroup")
    dialog.ui.core_btnGroup.addButton(dialog.ui.core_yes)
    dialog.ui.core_btnGroup.addButton(dialog.ui.core_no)

    dialog.ui.active_btnGroup = QtWidgets.QButtonGroup()
    dialog.ui.active_btnGroup.setObjectName("active_btnGroup")
    dialog.ui.active_btnGroup.addButton(dialog.ui.active_yes)
    dialog.ui.active_btnGroup.addButton(dialog.ui.active_no)

    dialog.ui.sale_btnGroup = QtWidgets.QButtonGroup()
    dialog.ui.sale_btnGroup.setObjectName("sale_btnGroup")
    dialog.ui.sale_btnGroup.addButton(dialog.ui.sale_yes)
    dialog.ui.sale_btnGroup.addButton(dialog.ui.sale_no)

    dialog.ui.offer_btnGroup = QtWidgets.QButtonGroup()
    dialog.ui.offer_btnGroup.setObjectName("offer_btnGroup")
    dialog.ui.offer_btnGroup.addButton(dialog.ui.offer_yes)
    dialog.ui.offer_btnGroup.addButton(dialog.ui.offer_no)

    dialog.ui.feat_btnGroup = QtWidgets.QButtonGroup()
    dialog.ui.feat_btnGroup.setObjectName("feat_btnGroup")
    dialog.ui.feat_btnGroup.addButton(dialog.ui.feat_yes)
    dialog.ui.feat_btnGroup.addButton(dialog.ui.feat_no)


    icon = QIcon()
    icon.addPixmap(QPixmap("assets/icons/HSAPP.ico"), QIcon.Normal, QIcon.Off)
    dialog.setWindowIcon(icon)

    def contextMenuEvent():
        # creates a context menu for image thumbnails
        logging.debug("new product context menu")
        menu2 = QtWidgets.QMenu(dialog)

        w = QtWidgets.QApplication.widgetAt(QtGui.QCursor.pos())

        # creating actions for context menu
        removePhotoAction = QtWidgets.QAction('Remove Photo', dialog)
        removePhotoAction.triggered.connect(lambda: removePhotoContext(w))
        addPhotoAction = QtWidgets.QAction('Add/Replace Photo', dialog)
        addPhotoAction.triggered.connect(lambda: addPhotoContext(w))
        defaultPhotoAction = QtWidgets.QAction('Set as Default Photo', dialog)
        defaultPhotoAction.triggered.connect(lambda: defaultPhotoContext(w))

        menu2.addAction(addPhotoAction)
        menu2.addAction(removePhotoAction)
        menu2.addSeparator()
        menu2.addAction(defaultPhotoAction)

        # show context menu at cursor location
        menu2.popup(QtGui.QCursor.pos())
        return
    def removePhotoContext(loc):
        loc.clear()
        del img_names[loc.objectName()]
        return
    def addPhotoContext(loc):
        img, _ = QtWidgets.QFileDialog.getOpenFileName(dialog, "Select Images", (QtCore.QDir.homePath()))
        pixmap = QPixmap(img)
        pixmap = QPixmap(pixmap.scaled(125, 125))
        loc.setPixmap(pixmap)
        img_names[loc.objectName()] = img
    def defaultPhotoContext(loc):
        temp_list = []
        temp = img_names.get(loc.objectName())

        # remove selected image from dict and populate temp list
        del img_names[loc.objectName()]
        for labels, imgs in img_names.items():
            temp_list.append(imgs)
        img_names.clear()

        # reinsert temp img
        temp_list.insert(0, temp)

        # clear pixmaps
        col = 0
        row = 0
        for i in range(0, 11):
            if col == 2:
                col = 0
                row += 1
            w = dialog.ui.gridLayout.itemAtPosition(row, col).widget()
            w.clear()

        # update pixmaps and file list
        col = 0
        row = 0
        for img in range(0, len(temp_list)):
            pixmap = QPixmap(temp_list[img])
            pixmap = QPixmap(pixmap.scaled(97, 97))
            if col == 2:
                col = 0
                row += 1
            w = dialog.ui.gridLayout.itemAtPosition(row, col).widget()
            img_names[w.objectName()] = temp_list[img]
            w.setPixmap(QPixmap(pixmap))
            col += 1
        return

    def changedCat():
        logging.debug("changed product category")
        # clears and displays relevant subcategories
        dialog.ui.subcat_options.clear()
        # adds appropriate subcategories to subcat widget
        if dialog.ui.cat_options.currentText() == 'Airboat':
            dialog.ui.subcat_options.addItems(airboat_subcats)
        if dialog.ui.cat_options.currentText() == 'Aircraft For Sale':
            dialog.ui.subcat_options.addItems(aircraft_for_sale_subcats)
        if dialog.ui.cat_options.currentText() == 'Airframe':
            dialog.ui.subcat_options.addItems(airframe_subcats)
        if dialog.ui.cat_options.currentText() == 'Avionics':
            dialog.ui.subcat_options.addItems(avionics_subcats)
        if dialog.ui.cat_options.currentText() == 'Electrical':
            dialog.ui.subcat_options.addItems(electrical_subcats)
        if dialog.ui.cat_options.currentText() == 'Hardware & Tools':
            dialog.ui.subcat_options.addItems(hardware_subcats)
        if dialog.ui.cat_options.currentText() == 'Landing Gear':
            dialog.ui.subcat_options.addItems(gear_subcats)
        if dialog.ui.cat_options.currentText() == 'Pilot Supplies':
            dialog.ui.subcat_options.addItems(pilot_supp_subcats)
        if dialog.ui.cat_options.currentText() == 'Powerplant':
            dialog.ui.subcat_options.addItems(powerplant_subcats)
        return

    def insertImages():
        # get images
        input_filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(dialog, "Select Images",
                                                                         (QtCore.QDir.homePath()))
        # iterate through labels, set pixmaps, add to images dict
        col = 0
        row = 0
        for item in range(0, len(input_filenames)):
            pixmap = QPixmap(input_filenames[item])
            print("got pixmap")
            pixmap = QPixmap(pixmap.scaled(125, 125))
            print("scaled")
            if col == 2:
                col = 0
                row += 1
            w = dialog.ui.gridLayout.itemAtPosition(row, col).widget()
            print(item)
            w.setPixmap(QPixmap(pixmap))
            img_names[w.objectName()] = input_filenames[item]
            print("placed")
            print(('image/' + str(imghdr.what(input_filenames[item]))))
            col += 1

        print(img_names)
        return

    def parseProductForm(action, username, NetworkSession):

        # processing data from text fields
        item_form = {
            'productName': dialog.ui.name_le.text(),
            'productDescription': dialog.ui.desc_te.toPlainText(),
            'CategoryID': '',
            'productCondition': '',
            'Qty': dialog.ui.qty_le.text(),
            'PartNumber': dialog.ui.pn_le.text(),
            'APN': dialog.ui.apn_le.text(),
            'SerialNumber': dialog.ui.sn_le.text(),
            'SKU': dialog.ui.sku_le.text(),
            'Manufacturer': dialog.ui.mfr_le.text(),
            'Price': dialog.ui.price_le.text(),
            'ShippingCost': dialog.ui.ship_le.text(),
            'HasCore': '',
            'CoreCharge': '0.00',
            'Active': '',
            'OnSale': '',
            'AllowBestOffer': '',
            'Featured': '',
        }

        try:
            item_form['productImage'] = ('filename', open(img_names['img1_lbl'], 'rb'),
                                         ('image/' + str(imghdr.what(img_names['img1_lbl']))))
        except:
            item_form['productImage'] = ''

        # processing button choices
        if dialog.ui.core_yes.isChecked():
            item_form['HasCore'] = '1'
        if dialog.ui.core_no.isChecked():
            item_form['HasCore'] = '0'

        if dialog.ui.active_yes.isChecked():
            item_form['Active'] = '1'
        if dialog.ui.active_no.isChecked():
            item_form['Active'] = '0'

        if dialog.ui.sale_yes.isChecked():
            item_form['OnSale'] = '1'
        if dialog.ui.sale_no.isChecked():
            item_form['OnSale'] = '0'

        if dialog.ui.offer_yes.isChecked():
            item_form['AllowBestOffer'] = '1'
        if dialog.ui.offer_no.isChecked():
            item_form['AllowBestOffer'] = '0'

        if dialog.ui.feat_yes.isChecked():
            item_form['Featured'] = '1'
        if dialog.ui.feat_no.isChecked():
            item_form['Featured'] = '0'

        # processing category menus
        if dialog.ui.cat_options.currentText() == 'Airboat':
            item_form['CategoryID'] = '2'
            if dialog.ui.subcat_options.currentText() == 'Airboats':
                item_form['CategoryID'] = '25'
            if dialog.ui.subcat_options.currentText() == 'Engines':
                item_form['CategoryID'] = '22'
            if dialog.ui.subcat_options.currentText() == 'Hulls':
                item_form['CategoryID'] = '24'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '26'
            if dialog.ui.subcat_options.currentText() == 'Parts':
                item_form['CategoryID'] = '23'
        if dialog.ui.cat_options.currentText() == 'Aircraft For Sale':
            item_form['CategoryID'] = '1'
            if dialog.ui.subcat_options.currentText() == 'Aircraft for Sale':
                item_form['CategoryID'] = '13'
            if dialog.ui.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '16'
            if dialog.ui.subcat_options.currentText() == 'Helicopters':
                item_form['CategoryID'] = '17'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '21'
            if dialog.ui.subcat_options.currentText() == 'Projects':
                item_form['CategoryID'] = '12'
            if dialog.ui.subcat_options.currentText() == 'Singles':
                item_form['CategoryID'] = '18'
            if dialog.ui.subcat_options.currentText() == 'Twins':
                item_form['CategoryID'] = '19'
        if dialog.ui.cat_options.currentText() == 'Airframe':
            item_form['CategoryID'] = '3'
            if dialog.ui.subcat_options.currentText() == 'Aerobatic':
                item_form['CategoryID'] = '28'
            if dialog.ui.subcat_options.currentText() == 'Aeronca':
                item_form['CategoryID'] = '27'
            if dialog.ui.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '29'
            if dialog.ui.subcat_options.currentText() == 'Antique':
                item_form['CategoryID'] = '30'
            if dialog.ui.subcat_options.currentText() == 'Beechcraft':
                item_form['CategoryID'] = '31'
            if dialog.ui.subcat_options.currentText() == 'Bellanca':
                item_form['CategoryID'] = '32'
            if dialog.ui.subcat_options.currentText() == 'Cessna':
                item_form['CategoryID'] = '33'
            if dialog.ui.subcat_options.currentText() == 'Cirrus':
                item_form['CategoryID'] = '34'
            if dialog.ui.subcat_options.currentText() == 'Control Surfaces':
                item_form['CategoryID'] = '35'
            if dialog.ui.subcat_options.currentText() == 'General Parts':
                item_form['CategoryID'] = '117'
            if dialog.ui.subcat_options.currentText() == 'Helicopter':
                item_form['CategoryID'] = '37'
            if dialog.ui.subcat_options.currentText() == 'Interior':
                item_form['CategoryID'] = '38'
            if dialog.ui.subcat_options.currentText() == 'Luscombe':
                item_form['CategoryID'] = '39'
            if dialog.ui.subcat_options.currentText() == 'Mooney':
                item_form['CategoryID'] = '40'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '44'
            if dialog.ui.subcat_options.currentText() == 'Piper':
                item_form['CategoryID'] = '41'
            if dialog.ui.subcat_options.currentText() == 'Taylorcraft':
                item_form['CategoryID'] = '42'
            if dialog.ui.subcat_options.currentText() == 'Warbird':
                item_form['CategoryID'] = '43'
        if dialog.ui.cat_options.currentText() == 'Art':
            item_form['CategoryID'] = '4'
        if dialog.ui.cat_options.currentText() == 'Avionics':
            item_form['CategoryID'] = '5'
            if dialog.ui.subcat_options.currentText() == 'Antennas':
                item_form['CategoryID'] = '45'
            if dialog.ui.subcat_options.currentText() == 'Audio Panels':
                item_form['CategoryID'] = '46'
            if dialog.ui.subcat_options.currentText() == 'AutoPilot':
                item_form['CategoryID'] = '47'
            if dialog.ui.subcat_options.currentText() == 'ELTs':
                item_form['CategoryID'] = '48'
            if dialog.ui.subcat_options.currentText() == 'Engine Monitors':
                item_form['CategoryID'] = '49'
            if dialog.ui.subcat_options.currentText() == 'GPS':
                item_form['CategoryID'] = '50'
            if dialog.ui.subcat_options.currentText() == 'Indicators':
                item_form['CategoryID'] = '51'
            if dialog.ui.subcat_options.currentText() == 'Intercoms':
                item_form['CategoryID'] = '52'
            if dialog.ui.subcat_options.currentText() == 'Nav/Coms':
                item_form['CategoryID'] = '53'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '59'
            if dialog.ui.subcat_options.currentText() == 'Packages':
                item_form['CategoryID'] = '54'
            if dialog.ui.subcat_options.currentText() == 'Pitot Tubes':
                item_form['CategoryID'] = '55'
            if dialog.ui.subcat_options.currentText() == 'Transponders':
                item_form['CategoryID'] = '56'
            if dialog.ui.subcat_options.currentText() == 'Trays & Connectors':
                item_form['CategoryID'] = '57'
            if dialog.ui.subcat_options.currentText() == 'Weather Systems':
                item_form['CategoryID'] = '58'
        if dialog.ui.cat_options.currentText() == 'Electrical':
            item_form['CategoryID'] = '6'
            if dialog.ui.subcat_options.currentText() == 'Batteries':
                item_form['CategoryID'] = '60'
            if dialog.ui.subcat_options.currentText() == 'Lighting':
                item_form['CategoryID'] = '61'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '62'
        if dialog.ui.cat_options.currentText() == 'Experimental':
            item_form['CategoryID'] = '8'
        if dialog.ui.cat_options.currentText() == 'Hardware & Tools':
            item_form['CategoryID'] = '7'
            if dialog.ui.subcat_options.currentText() == 'Jacks':
                item_form['CategoryID'] = '63'
            if dialog.ui.subcat_options.currentText() == 'Nuts & Bolts':
                item_form['CategoryID'] = '64'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '68'
            if dialog.ui.subcat_options.currentText() == 'Rivets':
                item_form['CategoryID'] = '65'
            if dialog.ui.subcat_options.currentText() == 'Testing Equipment':
                item_form['CategoryID'] = '67'
            if dialog.ui.subcat_options.currentText() == 'Tools':
                item_form['CategoryID'] = '66'
        if dialog.ui.cat_options.currentText() == 'Landing Gear':
            item_form['CategoryID'] = '14'
            if dialog.ui.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '69'
            if dialog.ui.subcat_options.currentText() == 'Skis':
                item_form['CategoryID'] = '70'
            if dialog.ui.subcat_options.currentText() == 'Tailwheel':
                item_form['CategoryID'] = '71'
            if dialog.ui.subcat_options.currentText() == 'Tires & Tubes':
                item_form['CategoryID'] = '72'
            if dialog.ui.subcat_options.currentText() == 'Wheels & Brakes':
                item_form['CategoryID'] = '73'
        if dialog.ui.cat_options.currentText() == 'Misc':
            item_form['CategoryID'] = '9'
        if dialog.ui.cat_options.currentText() == 'Pilot Supplies':
            item_form['CategoryID'] = '15'
            if dialog.ui.subcat_options.currentText() == 'Aviator Accessories':
                item_form['CategoryID'] = '74'
            if dialog.ui.subcat_options.currentText() == 'Bags':
                item_form['CategoryID'] = '75'
            if dialog.ui.subcat_options.currentText() == 'Books':
                item_form['CategoryID'] = '76'
            if dialog.ui.subcat_options.currentText() == 'Collectibles':
                item_form['CategoryID'] = '77'
            if dialog.ui.subcat_options.currentText() == 'Covers & Accessories':
                item_form['CategoryID'] = '78'
            if dialog.ui.subcat_options.currentText() == 'Headsets':
                item_form['CategoryID'] = '79'
            if dialog.ui.subcat_options.currentText() == 'Manuals':
                item_form['CategoryID'] = '80'
            if dialog.ui.subcat_options.currentText() == 'Oils, Liquids, & Sprays':
                item_form['CategoryID'] = '81'
            if dialog.ui.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '86'
            if dialog.ui.subcat_options.currentText() == 'Pilot Wear':
                item_form['CategoryID'] = '82'
            if dialog.ui.subcat_options.currentText() == 'Safety':
                item_form['CategoryID'] = '83'
            if dialog.ui.subcat_options.currentText() == 'Stickers & Decals':
                item_form['CategoryID'] = '84'
            if dialog.ui.subcat_options.currentText() == 'Tow':
                item_form['CategoryID'] = '85'
        if dialog.ui.cat_options.currentText() == 'Powerplant':
            item_form['CategoryID'] = '10'
            if dialog.ui.subcat_options.currentText() == 'Engine Parts':
                item_form['CategoryID'] = '88'
            if dialog.ui.subcat_options.currentText() == 'Engines':
                item_form['CategoryID'] = '87'
            if dialog.ui.subcat_options.currentText() == 'Environmental':
                item_form['CategoryID'] = '118'
            if dialog.ui.subcat_options.currentText() == 'Exhaust':
                item_form['CategoryID'] = '89'
            if dialog.ui.subcat_options.currentText() == 'Fuel System':
                item_form['CategoryID'] = '90'
            if dialog.ui.subcat_options.currentText() == 'General Parts':
                item_form['CategoryID'] = '116'
            if dialog.ui.subcat_options.currentText() == 'Propellers':
                item_form['CategoryID'] = '91'
        if dialog.ui.cat_options.currentText() == 'Wheels & Brakes':
            item_form['CategoryID'] = '11'

        # processing condition
        if dialog.ui.cond_options.currentText() == 'As Removed':
            item_form['productCondition'] = 'AR'
        if dialog.ui.cond_options.currentText() == 'Serviceable':
            item_form['productCondition'] = 'SV'
        if dialog.ui.cond_options.currentText() == 'Overhauled':
            item_form['productCondition'] = 'OH'
        if dialog.ui.cond_options.currentText() == 'New Stock':
            item_form['productCondition'] = 'NS'
        if dialog.ui.cond_options.currentText() == 'Repairable':
            item_form['productCondition'] = 'RP'
        if dialog.ui.cond_options.currentText() == 'New Surplus (NOS)':
            item_form['productCondition'] = 'NE'
        if dialog.ui.cond_options.currentText() == 'Beyond Repair':
            item_form['productCondition'] = 'BER'
        if dialog.ui.cond_options.currentText() == 'Unknown':
            item_form['productCondition'] = 'UN'
        if dialog.ui.cond_options.currentText() == 'Core':
            item_form['productCondition'] = 'Core'

        print(username)
        validate_code = validateForm(item_form)

        if validate_code == 0:
            pass
        else:
            QtWidgets.QMessageBox.warning(dialog, 'Product Error', 'Please complete required field: ' + validate_code,
                                          QtWidgets.QMessageBox.Ok)
            return

        if action == "upload":
            try:
                uploadProductForm(item_form, img_names, NetworkSession)
            except Exception as e:
                logging.exception(e)
                QtWidgets.QMessageBox.warning(dialog, 'Upload Error', 'There was an error uploading the product. Try again later.',
                                              QtWidgets.QMessageBox.Ok)
            return
        if action == "save":
            try:
                saveProductForm(item_form, img_names, username)
            except Exception as e:
                logging.exception(e)
                QtWidgets.QMessageBox.warning(dialog, 'Save Error','There was an error saving the product. Try again later.', QtWidgets.QMessageBox.Ok)

    def uploadProductForm(item_form, img_names, NetworkSession):

        product_data = MultipartEncoder(fields=item_form, boundary='-----WebKitFormBoundarymkISNjkugjjFZdvE')

        # making the post to submit listing
        t = NetworkSession.post('https://www.hangarswap.com/Seller/SaveProduct', data=product_data,
                                headers={'Content-Type': product_data.content_type})

        # checks if there is more than one image in the upload list
        if (len(img_names) > 1):

            # checks to see what productID HS has assigned the item, and grabs it
            soup = BeautifulSoup(t.text, "html.parser")
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

    def saveProductForm(item_form, img_names, username):
        print("./bin/cache/"+username+"/pend.dat")
        with open("./bin/cache/"+username+"/pend.dat", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([
                randint(0, 999),
                item_form['productName'],
                item_form['productDescription'],
                item_form['CategoryID'],
                item_form['productCondition'],
                item_form['Qty'],
                item_form['PartNumber'],
                item_form['APN'],
                item_form['SerialNumber'],
                item_form['SKU'],
                item_form['Manufacturer'],
                item_form['Price'],
                item_form['ShippingCost'],
                item_form['HasCore'],
                item_form['CoreCharge'],
                item_form['Active'],
                item_form['OnSale'],
                item_form['AllowBestOffer'],
                item_form['Featured'],
                img_names
            ])

        return

    dialog.exec_()

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