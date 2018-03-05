#importing misc modules
import csv
import imghdr
import sys
import login_form
#importing networking modules
import bs4
import requests
import webbrowser

#importing GUI elements
from PyQt5 import QtCore, QtGui, QtWidgets
import logic_scripts
import PyQt5.QtNetwork
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QSplashScreen
from requests_toolbelt.multipart.encoder import MultipartEncoder

#importing external widgets
import login_form
import main_window_redesign
import newProductDialog
import loadingDialog

NetworkSession = None

sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


class HSMainWindow(QtWidgets.QMainWindow, main_window_redesign.Ui_HSMainWindow):
    def __init__(self, fileName, parent=None):
        super(HSMainWindow, self).__init__(parent)

        self.setupUi(self)

        self.inbox_model = QtGui.QStandardItemModel(self)
        item = QtGui.QStandardItem()
        self.inbox_model.appendRow(item)
        self.inbox_model.setData(self.inbox_model.index(0, 0), "", 0)
        self.inboxTable.setModel(self.inbox_model)

        self.unread_model = QtGui.QStandardItemModel(self)
        self.unread_model.appendRow(item)
        self.unread_model.setData(self.unread_model.index(0,0),"",0)

        self.sent_model = QtGui.QStandardItemModel(self)
        self.sent_model.appendRow(item)
        self.sent_model.setData(self.sent_model.index(0, 0), "", 0)

        self.trash_model = QtGui.QStandardItemModel(self)
        self.trash_model.appendRow(item)
        self.trash_model.setData(self.trash_model.index(0, 0), "", 0)

        self.unreadTable.setModel(self.unread_model)
        self.trashTable.setModel(self.trash_model)
        self.sentTable.setModel(self.sent_model)

        self.catalog_model = QtGui.QStandardItemModel(self)
        self.catalog_model.appendRow(item)
        self.catalog_model.setData(self.catalog_model.index(0, 0), "", 0)
        self.catalogTable.setModel(self.catalog_model)

        self.order_model = QtGui.QStandardItemModel(self)
        self.order_model.appendRow(item)
        self.order_model.setData(self.order_model.index(0, 0), "", 0)
        self.orderTable.setModel(self.order_model)

        try:
            self.loadProfile()
            self.loadMessages()
            self.loadLandingListings()
            self.refreshProfilePage()
            self.loadProductCatalog()
            self.loadOrders()

        except ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Network Connection Error: please check network, and restart program.', QtWidgets.QMessageBox.Ok)


    def initOrdersView(self):
        self.stackedWidget.setCurrentWidget(self.ordersPage)
    def initInboxView(self):
        self.stackedWidget.setCurrentWidget(self.inboxPage)
    def initProductsView(self):
        self.stackedWidget.setCurrentWidget(self.catalogPage)
    def initPendingView(self):
        self.stackedWidget.setCurrentWidget(self.pendingPage)
    def initProfileView(self):
        if self.profileDescTE.toPlainText() == "":
            self.refreshProfilePage()
        self.stackedWidget.setCurrentWidget(self.profilePage)
    def initLandingView(self):
        self.stackedWidget.setCurrentWidget(self.landingPage)
    def initStorePageView(self):
        return
    def initNewProductsView(self):
        return


    def switchInboxTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.inboxTablePage)
    def switchSentTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.sentTablePage)
    def switchTrashTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.trashTablePage)
    def switchUnreadTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.unreadTablePage)

    def changeProfileIcon(self):
        return
    def saveProfileChanges(self):
        return

    def changeOrderTableLength(self):
        return
    def searchOrderTable(self):
        return

    def addProduct(self):
        addProductWidget = newProductDialog.Ui_newListing()
        if addProductWidget.exec() == QtWidgets.QDialog.Accepted:
            print("You theoretically added a product!")

    def filterPendingProductsTable(self):
        return
    def filterProductsTable(self):
        return

    def refreshProfilePage(self):
        desc, paypal_email = logic_scripts.getProfilePage(NetworkSession)
        self.profileDescTE.setText(desc)
        self.paypalEmailLE.setText(paypal_email)

    def loadProfile(self):
        storeName, customerName = logic_scripts.getSellerName(NetworkSession)
        self.storeNameLbl.setText(storeName)
        self.customerNameLbl.setText(customerName)


    def loadMessages(self):
        inbox_list, unread_list, sent_list, trash_list = logic_scripts.getInbox(NetworkSession)

        self.unread_model.setHorizontalHeaderLabels(["Sender","Message","button","Time Received"])
        self.sent_model.setHorizontalHeaderLabels(["Recipient","Message","button","Time Sent"])
        self.trash_model.setHorizontalHeaderLabels(["Sender","Message","button","Time"])
        self.inbox_model.setHorizontalHeaderLabels(["Sender","Message","button","Time Received"])

        for row in inbox_list:
           items = []
           for field in row:
             value = str(field)
             items.append(QtGui.QStandardItem(value))
           self.inbox_model.appendRow(items)

        for row in unread_list:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.unread_model.appendRow(items)

        for row in sent_list:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.sent_model.appendRow(items)

        for row in trash_list:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.trash_model.appendRow(items)

    def loadProductCatalog(self):
        catalog_data, catalog_headers = logic_scripts.getCatalog(NetworkSession)
        self.catalog_model.clear()
        self.catalog_model.setHorizontalHeaderLabels(catalog_headers)
        for row in catalog_data:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.catalog_model.appendRow(items)

    def loadLandingListings(self):

        prod1, prod2, prod3, prod4 = logic_scripts.getNewestListings(NetworkSession)

        self.prod1titleLbl.setText(prod1['title'])
        self.prod1priceLbl.setText(prod1['price'])
        self.prod1imgLbl.setPixmap(prod1['img'])

        self.prod2titleLbl.setText(prod2['title'])
        self.prod2priceLbl.setText(prod2['price'])
        self.prod2imgLbl.setPixmap(prod2['img'])

        self.prod3titleLbl.setText(prod3['title'])
        self.prod3priceLbl.setText(prod3['price'])
        self.prod3imgLbl.setPixmap(prod3['img'])

        self.prod4titleLbl.setText(prod4['title'])
        self.prod4priceLbl.setText(prod4['price'])
        self.prod4imgLbl.setPixmap(prod4['img'])

    def loadOrders(self):

        orders_list = logic_scripts.getOrders(NetworkSession)
        #self.order_model.clear()
        self.order_model.setHorizontalHeaderLabels(["OrderId","Customer","Product","Date Shipped","Qty","Unit Price"])
        for row in orders_list:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.order_model.appendRow(items)

def main():
    app = QtWidgets.QApplication(sys.argv)
    login = login_form.Ui_Dialog()

    splash_pic = QPixmap('loading_splash.png')
    splash = QSplashScreen(splash_pic)

    global NetworkSession

    if login.exec() == QtWidgets.QDialog.Accepted:
        NetworkSession = login.getNetSesh()
        splash.show()
        form = HSMainWindow('')
        form.show()
        splash.finish(form)
    else:
        return

    app.exec()


if __name__ == '__main__':
    sys.excepthook = my_exception_hook

    main()
