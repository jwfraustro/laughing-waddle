import csv
import imghdr
import sys

import bs4
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from requests_toolbelt.multipart.encoder import MultipartEncoder

import edit_product_widget
import login_form
import mainwindow
import new_product_widget

s = ''

pr_id = ''

payload  = {
            'Username': '',
            'Password': '',
            'authToken': ''
}

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def addProduct(item_data, filenames):
    with requests.Session() as s:
        p = s.post('http://www.hangarswap.com/Main/Login')
        soup = bs4.BeautifulSoup(p.text, "html.parser")

        # print(s.cookies.get_dict())

        authToken = soup.select('input[name="authToken"]')[0]
        payload['authToken'] = authToken.get('value')
        # print(payload['authToken'])

        p = s.post('https://www.hangarswap.com/Main/ProcessLogin', data=payload, verify=False)
        # print(p.text)

        # An authorised request.
        r = s.get('https://www.hangarswap.com/Seller/AddProduct')

        print(item_data)

        product_data = MultipartEncoder(fields=item_data, boundary='-----WebKitFormBoundarymkISNjkugjjFZdvE')

        print("encoded succesful")

        t = s.post('https://www.hangarswap.com/Seller/SaveProduct', data=product_data,
                   headers={'Content-Type': product_data.content_type})
        print("Post Successful")

        if (len(filenames) > 1):
            soup = bs4.BeautifulSoup(t.text, "html.parser")
            pr_id = soup.select('[href*="ProductID"]')[0].get("href")[-5:].strip("=")
            for i in range(2, len(filenames)):
                photo_form = MultipartEncoder(
                    fields={
                        'productid': str(pr_id),
                        'ProductImage': (
                        'filename', open(filenames['img'+str(i)+'_lbl'], 'rb'), ('image/' + str(imghdr.what(filenames['img'+str(i)+'_lbl'])))),
                    }, boundary='-----WebKitFormBoundarydMG06kgczAncwn4B')
                t = s.post('https://www.hangarswap.com/Seller/SaveExtraImages', data=photo_form,
                           headers={'Content-Type': photo_form.content_type})
                print('submitted ', filenames['img'+str(i)+'_lbl'])


class NewItemWidget(QtWidgets.QMainWindow, new_product_widget.Ui_ListItemWidget):
    def __init__(self, parent=None):
        super(NewItemWidget, self).__init__(parent)

        self.setupUi(self)

        self.img_names={}
        # item_form = self.readForm(self)
        self.img_upload_btn.clicked.connect(self.insertImages)
        self.upload_new_button.clicked.connect(self.uploadItem)
        self.save_templ_button.clicked.connect(self.saveProduct)
        print(self.gridLayout.count())
        # addProduct(item_form)

        self.img1_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img2_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img3_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img4_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img5_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img6_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img7_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img8_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img9_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img10_lbl.customContextMenuRequested.connect(self.contextMenuEvent)

    def contextMenuEvent(self, event):

        self.menu2 = QtWidgets.QMenu(self)
        print("made menu")

        removePhotoAction = QtWidgets.QAction('Remove Photo', self)
        removePhotoAction.triggered.connect(lambda: self.removePhotoContext(event))

        addPhotoAction = QtWidgets.QAction('Add/Replace Photo', self)
        addPhotoAction.triggered.connect(lambda: self.addPhotoContext(event))


        defaultPhotoAction = QtWidgets.QAction('Set as Default Photo', self)
        defaultPhotoAction.triggered.connect(lambda: self.defaultPhotoContext(event)) 

        self.menu2.addAction(addPhotoAction)
        self.menu2.addAction(removePhotoAction)
        self.menu2.addSeparator()
        self.menu2.addAction(defaultPhotoAction)

        self.menu2.popup(QtGui.QCursor.pos())
        w = QtWidgets.QApplication.widgetAt(QtGui.QCursor.pos())
        print(w.objectName())

    def defaultPhotoContext(self, event):
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)
        print(w.objectName())

        #instance temp holder lists / img
        temp_list =[]
        temp = self.img_names.get(w.objectName())

        #remove selected image from dict and fill temp list
        del self.img_names[w.objectName()]
        for labels, imgs in self.img_names.items():
            temp_list.append(imgs)
        self.img_names.clear()

        #reinsert temp img
        temp_list.insert(0, temp)
        print(len(temp_list))

        #clear pixmaps
        col = 0
        row = 0
        for i in range(0,11):
            if col == 2:
                col = 0
                row += 1
            w = self.gridLayout.itemAtPosition(row, col).widget()
            w.clear()

        #update pixmaps and file list
        col=0
        row=0
        for img in range(0,len(temp_list)):
            print(img, temp_list[img])
            pixmap = QPixmap(temp_list[img])
            pixmap = QPixmap(pixmap.scaled(97, 97))
            if col == 2:
                col = 0
                row += 1
            w = self.gridLayout.itemAtPosition(row, col).widget()
            self.img_names[w.objectName()]=temp_list[img]
            w.setPixmap(QPixmap(pixmap))
            col += 1

        print(w.objectName(), img)



    def removePhotoContext(self, event):
        #get lbl at cursor, and remove from dict
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)
        print(w.objectName())
        w.clear()
        del self.img_names[w.objectName()]
        print(self.img_names)

    def addPhotoContext(self, event):
        #get lbl at cursor, and place in dict
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)
        print(w.objectName())
        img, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Images", (QtCore.QDir.homePath()))
        print(img)
        pixmap = QPixmap(img)
        pixmap = QPixmap(pixmap.scaled(97, 97))
        w.setPixmap(pixmap)
        self.img_names[w.objectName()]=img
        print(self.img_names)


    def insertImages(self):
        #get images
        self.input_filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select Images",
                                                                   (QtCore.QDir.homePath()))
        #iterate through labels, set pixmaps, add to images dict
        col = 0
        row = 0
        for item in range(0, len(self.input_filenames)):
            pixmap = QPixmap(self.input_filenames[item])
            print("got pixmap")
            pixmap = QPixmap(pixmap.scaled(97, 97))
            print("scaled")
            if col == 2:
                col = 0
                row += 1
            w = self.gridLayout.itemAtPosition(row, col).widget()
            print(item)
            w.setPixmap(QPixmap(pixmap))
            self.img_names[w.objectName()]=self.input_filenames[item]
            print("placed")
            print(('image/' + str(imghdr.what(self.input_filenames[item]))))
            col += 1

        print(self.img_names)

    def saveProduct(self):
        item_data, imgs = self.processForm(self.img_names)
        with open("waiting_to_upload.csv", 'a', newline='\n') as f:
            writer = csv.writer(f, delimiter = ',')
            writer.writerow([item_data,imgs])

    def uploadItem(self):
        item_data, imgs = self.processForm(self.img_names)
        addProduct(item_data, imgs)

    def processForm(self, img_names):

        # processing text
        item_form = {
            'productName': self.name_le.text(),
            'productDescription': self.desc_te.toPlainText(),
            'CategoryID': '',
            'productCondition': '',
            'Qty': self.qty_le.text(),
            'PartNumber': self.pn_le.text(),
            'APN': self.apn_le.text(),
            'SerialNumber': self.sn_le.text(),
            'SKU': self.sku_le.text(),
            'Manufacturer': self.mfr_le.text(),
            'Price': self.price_le.text(),
            'ShippingCost': self.ship_le.text(),
            'HasCore': '',
            'CoreCharge': '0.00',
            'productImage': ('filename', open(self.img_names['img1_lbl'], 'rb'), ('image/' + str(imghdr.what(self.img_names['img1_lbl'])))),
            # 'SecondaryproductImage' : '',
            'Active': '',
            'OnSale': '',
            'AllowBestOffer': '',
            'Featured': '',
        }
        
        # processing buttons
        if self.core_yes.isChecked():
            item_form['HasCore'] = '1'
        if self.core_no.isChecked():
            item_form['HasCore'] = '0'

        if self.active_yes.isChecked():
            item_form['Active'] = '1'
        if self.active_no.isChecked():
            item_form['Active'] = '0'

        if self.sale_yes.isChecked():
            item_form['OnSale'] = '1'
        if self.sale_no.isChecked():
            item_form['OnSale'] = '0'

        if self.offer_yes.isChecked():
            item_form['AllowBestOffer'] = '1'
        if self.offer_no.isChecked():
            item_form['AllowBestOffer'] = '0'

        if self.feat_yes.isChecked():
            item_form['Featured'] = '1'
        if self.feat_no.isChecked():
            item_form['Featured'] = '0'

        # processing category menus
        if self.cat_options.currentText() == 'Airboat':
            item_form['CategoryID'] = '2'
        if self.cat_options.currentText() == 'Aircraft For Sale':
            item_form['CategoryID'] = '1'
        if self.cat_options.currentText() == 'Airframe':
            item_form['CategoryID'] = '3'
        if self.cat_options.currentText() == 'Art':
            item_form['CategoryID'] = '4'
        if self.cat_options.currentText() == 'Avionics':
            item_form['CategoryID'] = '5'
        if self.cat_options.currentText() == 'Electrical':
            item_form['CategoryID'] = '6'
        if self.cat_options.currentText() == 'Experimental':
            item_form['CategoryID'] = '8'
        if self.cat_options.currentText() == 'Hardware & Tools':
            item_form['CategoryID'] = '7'
        if self.cat_options.currentText() == 'Landing Gear':
            item_form['CategoryID'] = '14'
        if self.cat_options.currentText() == 'Misc':
            item_form['CategoryID'] = '9'
        if self.cat_options.currentText() == 'Pilot Supplies':
            item_form['CategoryID'] = '15'
        if self.cat_options.currentText() == 'Powerplant':
            item_form['CategoryID'] = '10'
        if self.cat_options.currentText() == 'Wheels & Brakes':
            item_form['CategoryID'] = '11'

        # processing condition
        if self.cond_options.currentText() == 'As Removed':
            item_form['productCondition'] = 'AR'
        if self.cond_options.currentText() == 'Serviceable':
            item_form['productCondition'] = 'SV'
        if self.cond_options.currentText() == 'Overhauled':
            item_form['productCondition'] = 'OH'
        if self.cond_options.currentText() == 'New Stock':
            item_form['productCondition'] = 'NS'
        if self.cond_options.currentText() == 'Repairable':
            item_form['productCondition'] = 'RP'
        if self.cond_options.currentText() == 'New Surplus (NOS)':
            item_form['productCondition'] = 'NE'
        if self.cond_options.currentText() == 'Beyond Repair':
            item_form['productCondition'] = 'BER'
        if self.cond_options.currentText() == 'Unknown':
            item_form['productCondition'] = 'UN'
        if self.cond_options.currentText() == 'Core':
            item_form['productCondition'] = 'Core'

        return(item_form, self.img_names)


class EditItemWidget(QtWidgets.QMainWindow, edit_product_widget.Ui_ListItemWidget):
    def __init__(self, pr_id, parent=None):
        super(EditItemWidget, self).__init__(parent)
        self.setupUi(self)

        #instance context menu options
        self.img1_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img2_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img3_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img4_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img5_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img6_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img7_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img8_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img9_lbl.customContextMenuRequested.connect(self.contextMenuEvent)
        self.img10_lbl.customContextMenuRequested.connect(self.contextMenuEvent)

    def loadProduct(self, pr_id):

        r = s.get('https://www.hangarswap.com/Seller/EditProduct?ProductID=' + str(pr_id), verify=False)

        editSoup = bs4.BeautifulSoup(r.text, "html.parser")

        self.name_le.setText(str(editSoup.select('input[name="productName"]')[0].get('value')))
        self.desc_te.setText(str(editSoup.select('textarea[name="productDescription"]')[0].contents[0]))
        self.qty_le.setText(str(editSoup.select('input[name="Qty"]')[0].get('value')))
        self.pn_le.setText(str(editSoup.select('input[name="PartNumber"]')[0].get('value')))
        self.apn_le.setText(str(editSoup.select('input[name="APN"]')[0].get('value')))
        self.sn_le.setText(str(editSoup.select('input[name="SerialNumber"]')[0].get('value')))
        self.sku_le.setText(str(editSoup.select('input[name="SKU"]')[0].get('value')))
        self.mfr_le.setText(str(editSoup.select('input[name="Manufacturer"]')[0].get('value')))
        self.price_le.setText(str(editSoup.select('input[name="Price"]')[0].get('value')))
        self.ship_le.setText(str(editSoup.select('input[name="ShippingCost"]')[0].get('value')))

        r = s.get('http://www.hangarswap.com/Shop/DisplayProduct?productID=' + str(pr_id))

        editSoup = bs4.BeautifulSoup(r.text, "html.parser")

        img_elems = editSoup.select('#thumbnails img')

        col = 0
        row = 0
        for img in range(0, len(img_elems)):
            img_URL = 'http://www.hangarswap.com' + img_elems[img].get('src')
            img_bytes = s.get(img_URL).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_bytes)
            print("got pixmap")
            pixmap = QPixmap(pixmap.scaled(97, 97))
            print("scaled")
            if col == 2:
                col = 0
                row += 1
            w = self.gridLayout.itemAtPosition(row, col).widget()
            w.setPixmap(QPixmap(pixmap))
            print("placed")
            col += 1

    def contextMenuEvent(self, event):

        self.menu2 = QtWidgets.QMenu(self)
        print("made menu")

        removePhotoAction = QtWidgets.QAction('Remove Photo', self)
        removePhotoAction.triggered.connect(lambda: self.removePhotoContext(event))

        addPhotoAction = QtWidgets.QAction('Add Photo', self)
        addPhotoAction.triggered.connect(lambda: self.addPhotoContext(event))

        self.menu2.addAction(addPhotoAction)
        self.menu2.addAction(removePhotoAction)

        self.menu2.popup(QtGui.QCursor.pos())
        print(QtGui.QCursor.pos())

    def removePhotoContext(self, event):
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)
        print(w)
        w.clear()

    def addPhotoContext(self, event):
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)
        print(w)
        img, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Images", (QtCore.QDir.homePath()))
        print(img)
        pixmap = QPixmap(img)
        pixmap = QPixmap(pixmap.scaled(97, 97))
        w.setPixmap(pixmap)


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_HSMainWindow):
    def __init__(self, fileName, parent=None):
        super(ExampleApp, self).__init__(parent)

        self.fileName = ""
        self.fname = "List"

        self.setupUi(self)

        self.model = QtGui.QStandardItemModel(self)
        self.model2 = QtGui.QStandardItemModel(self)
        item = QtGui.QStandardItem()
        self.model.appendRow(item)
        self.model.setData(self.model.index(0, 0), "", 0)
        self.model2.appendRow(item)
        self.model2.setData(self.model.index(0, 0), "", 0)
        self.orders_list.setModel(self.model2)
        self.catalog_table.setModel(self.model)
        self.catalog_table.horizontalHeader()
        self.catalog_table.resizeColumnsToContents()
        self.catalog_table.customContextMenuRequested.connect(self.catalogContextMenu)
        self.orders_list.customContextMenuRequested.connect(self.ordersContextMenu)

        self.newitemwidget = NewItemWidget(self)
        self.actionNewItem.triggered.connect(self.init_new_product)
        self.edititemwidget = EditItemWidget(self)

        with open("orders.dat", 'r') as f:
            reader = csv.reader(f, delimiter = "\t")
            for row in reader:
                items = [QtGui.QStandardItem(field) for field in row]
                self.model2.appendRow(items)
            self.orders_list.resizeColumnsToContents()


        #item = QtWidgets.QListWidgetItem("Item #1")
        #self.orders_list.addItem(item)

        self.newprod_button.clicked.connect(self.init_new_product)
        self.edit_button.clicked.connect(self.init_edit_product)
        self.order_btn.clicked.connect(self.orders_list.raise_)
        self.active_cat_button.clicked.connect(self.catalog_table.raise_)

        self.actionInventory_CSV.triggered.connect(self.load_csv)

    def init_new_product(self):
        self.newitemwidget.show()

    def init_edit_product(self):
        pr_id = self.editPIDWarnDialog()
        self.edititemwidget.loadProduct(pr_id)
        self.edititemwidget.show()

    def editPIDWarnDialog(self):
        pr_id, ok = QtWidgets.QInputDialog.getText(self, 'Edit Item',
                                                   'Editing from an inventory file is not currently implemented. \nPlease enter a live HS Product ID to continue:')
        if ok:
            return pr_id
        else:
            self.close()

    def load_csv(self, fileName):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open CSV",
                                                            (QtCore.QDir.homePath), "CSV (*.csv *.tsv)")

        if fileName:
            print(fileName)
            ff = open(fileName, 'r')
            mytext = ff.read()
            # print(mytext)
            ff.close()
            with open(fileName, "r") as f:
                reader = csv.reader(f, delimiter=',')
                self.model.clear()
                print("Model clear")
                for row in reader:
                    items = [QtGui.QStandardItem(field) for field in row]
                    self.model.appendRow(items)
                self.catalog_table.resizeColumnsToContents()

    def ordersContextMenu(self, event):
        self.menu = QtWidgets.QMenu(self)
        
        viewOrderAction = QtWidgets.QAction('View Order', self)
        viewOrderAction.triggered.connect(lambda: self.viewOrderContext(event))

        self.menu.addAction(viewOrderAction)

        self.menu.popup(QtGui.QCursor.pos())
        print(QtGui.QCursor.pos())

    def catalogContextMenu(self, event):

        self.menu = QtWidgets.QMenu(self)
        print("made menu")

        addItemAction = QtWidgets.QAction('Add Item', self)
        addItemAction.triggered.connect(lambda: self.addByContext(event))

        editItemAction = QtWidgets.QAction('Edit Item', self)
        editItemAction.triggered.connect(lambda: self.editByContext(event))

        self.menu.addAction(addItemAction)
        self.menu.addAction(editItemAction)

        self.menu.popup(QtGui.QCursor.pos())
        print(QtGui.QCursor.pos())

    def addByContext(self, event):
        self.init_new_product()

    def editByContext(self, event):
        self.init_edit_product()

    def copyByContext(self, event):
        for i in self.catalog_table.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row, col)
            if myitem is not None:
                clip = QtWidgets.QApplication.clipboard()
                clip.setText(myitem.text())

    def pasteByContext(self, event):
        for i in self.catalog_table.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
            myitem = self.model.item(row, col)
            clip = QtWidgets.QApplication.clipboard()
            myitem.setText(clip.text())

class loginForm(QtWidgets.QMainWindow, login_form.Ui_LoginDialog):
    def __init__(self, parent=None):
        super(loginForm, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.loginProcess)

    def loginProcess(self):

        payload['Username']= self.userName_le.text()
        payload['Password']= self.pswd_le.text()

        global s
        s = requests.Session()
        p = s.post('http://www.hangarswap.com/Main/Login')
        soup = bs4.BeautifulSoup(p.text, "html.parser")

        authToken = soup.select('input[name="authToken"]')[0]
        payload['authToken'] = authToken.get('value')

        p = s.post('https://www.hangarswap.com/Main/ProcessLogin', data=payload, verify=False, allow_redirects=False)
        if 'location' not in p.headers.keys():
            self.error_lbl.setText('There was an error logging in.')
        else:
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)

    form = ExampleApp('')
    form.show()

    login = loginForm()
    login.show()

    app.exec()


if __name__ == '__main__':
    sys.excepthook = my_exception_hook

    main()
