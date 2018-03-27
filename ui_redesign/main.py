# importing misc modules
import logging
import sys
# importing networking modules
import webbrowser

import logic_scripts
from modular_product_test import Ui_newListing as ProductDialog
# importing external widgets
import login_form
import main_window_redesign
import csv
import newProductDialog
# importing GUI elements
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QHeaderView
import time, os
from multiprocessing import Process

if not os.path.exists("./logs"):
    os.makedirs("./logs")
if not os.path.exists("./bin/cache"):
    os.makedirs("./bin/cache")

logging.basicConfig(filename="./logs/runtime.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

NetworkSession = None
username = ""

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()

class HSMainWindow(QtWidgets.QMainWindow, main_window_redesign.Ui_HSMainWindow):
    def __init__(self, parent=None):
        super(HSMainWindow, self).__init__(parent)
        logging.debug("UI Setup")
        self.setupUi(self)

        logging.debug("Inbox Model")
        self.inbox_model = QtGui.QStandardItemModel(self)
        self.inbox_model.setData(self.inbox_model.index(0, 0), "", 0)
        self.inboxTable.setModel(self.inbox_model)
        logging.debug("Built")

        logging.debug("Unread Model")
        self.unread_model = QtGui.QStandardItemModel(self)
        self.unread_model.setData(self.unread_model.index(0, 0), "", 0)
        logging.debug("Built")

        self.pending_model = QtGui.QStandardItemModel(self)
        self.pending_model.setData(self.pending_model.index(0,0),"",0)
        self.pendTable.setModel(self.pending_model)

        logging.debug("Sent Model")
        self.sent_model = QtGui.QStandardItemModel(self)
        self.sent_model.setData(self.sent_model.index(0, 0), "", 0)
        logging.debug("Built")

        logging.debug("Trash Model")
        self.trash_model = QtGui.QStandardItemModel(self)
        self.trash_model.setData(self.trash_model.index(0, 0), "", 0)
        logging.debug("Built")

        logging.debug("Model Assignment")
        self.unreadTable.setModel(self.unread_model)
        self.trashTable.setModel(self.trash_model)
        self.sentTable.setModel(self.sent_model)
        logging.debug("Built")

        logging.debug("Catalog Model")
        self.catalog_model = QtGui.QStandardItemModel(self)
        self.catalog_model.setData(self.catalog_model.index(0, 0), "", 0)
        self.catalogTable.setModel(self.catalog_model)
        self.catalogTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.catalogTable.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        logging.debug("Built")

        logging.debug("Order Model")
        self.order_model = QtGui.QStandardItemModel(self)
        self.order_model.setData(self.order_model.index(0, 0), "", 0)
        self.orderTable.setModel(self.order_model)
        logging.debug("Built")

        logging.debug("Catalog Context Menu")
        self.catalogTable.customContextMenuRequested.connect(self.catalogContextMenu)
        self.pendTable.customContextMenuRequested.connect(self.pendingContextMenu)
        logging.debug("Built")

        self.categoryCombo.addItem("Active")
        self.categoryCombo.addItem("Inactive")
        self.categoryCombo.addItem("Disabled")
        self.categoryCombo.addItem("Sold")
        self.categoryCombo.setCurrentIndex(0)

        logging.debug("Loading Account Info")
        try:
            runInParallel(self.loadProfile(), self.loadPending(), self.loadMessages(), self.loadLandingListings(), self.refreshProfilePage(), self.loadProductCatalog("Active"), self.loadOrders())

        except TimeoutError or ConnectionRefusedError or ConnectionError:
            logging.debug("network failure -- loading account info")
            QtWidgets.QMessageBox.warning(self, 'Error',
                                          'Network Connection Error: please check network, and restart program.',
                                          QtWidgets.QMessageBox.Ok)
            return

    def initOrdersView(self):
        self.stackedWidget.setCurrentWidget(self.ordersPage)
        logging.debug("Switched to Orders Page")

    def initInboxView(self):
        self.stackedWidget.setCurrentWidget(self.inboxPage)
        logging.debug("Switched to Inbox Page")

    def initProductsView(self):
        self.stackedWidget.setCurrentWidget(self.catalogPage)
        logging.debug("Switched to Catalog Page")

    def initPendingView(self):
        self.stackedWidget.setCurrentWidget(self.pendingPage)
        logging.debug("Switched to Pending Page")

    def initProfileView(self):
        logging.debug("Checked if profile info already loaded")
        if self.profileDescTE.toPlainText() == "":
            self.refreshProfilePage()
        self.stackedWidget.setCurrentWidget(self.profilePage)
        logging.debug("Switched to Profile Page")

    def initLandingView(self):
        self.stackedWidget.setCurrentWidget(self.landingPage)
        logging.debug("Switched to Landing Page")

    def initStorePageView(self):
        logging.debug("tried initStorePageView")
        return

    def initNewProductsView(self):
        webbrowser.open("http://www.hangarswap.com/Search/Newest")
        logging.debug("opened newest online listings")
        return

    def switchInboxTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.inboxTablePage)
        logging.debug("Switched to inbox table")

    def switchSentTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.sentTablePage)
        logging.debug("Switched to sent table")

    def switchTrashTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.trashTablePage)
        logging.debug("Switched to trash table")

    def switchUnreadTable(self):
        self.inboxStackedWidget.setCurrentWidget(self.unreadTablePage)
        logging.debug("Switched to unread table")

    def changeProfileIcon(self):
        logging.debug("tried to change profile pic")
        profileIconFile, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Profile Icon",
                                                                   (QtCore.QDir.homePath()))
        logging.debug("pic: %s", profileIconFile)

        profilePixmap = QPixmap(profileIconFile)
        scaledProfilePixmap = QPixmap(profilePixmap.scaled(50, 50))
        self.profileIcon.setPixmap(scaledProfilePixmap)
        logging.debug("Successfully set profile pic")

    def saveProfileChanges(self):
        logging.debug("tried to save profile changes")
        return

    def changeOrderTableLength(self):
        logging.debug("tried to change order table length")
        return

    def orderContextMenu(self):

        self.order_context = QtWidgets.QMenu(self)

        printPreviewContext = QtWidgets.QAction('View Order', self)
        printPreviewContext.triggered.connect(lambda: self.orderPrintPreview)

        self.order_context.addAction(printPreviewContext)

        self.order_context.popup(QtGui.QCursor.pos())
        logging.debug("requested order table context menu")

    def orderPrintPreview(self):
        logging.debug("tried to get order print preview")
        return

    def catalogContextMenu(self):

        self.catalog_context = QtWidgets.QMenu(self)

        addProductContext = QtWidgets.QAction('Add New Product', self)
        addProductContext.triggered.connect(self.addProduct)

        viewProductContext = QtWidgets.QAction('View Product Online', self)
        viewProductContext.triggered.connect(lambda: self.viewProductAction())

        disableProductContext = QtWidgets.QAction('Disable Product', self)
        disableProductContext.triggered.connect(lambda: self.disableProductAction())

        markSoldContext = QtWidgets.QAction('Mark Product Sold', self)
        markSoldContext.triggered.connect(lambda: self.markProductSoldAction())

        editProductContext = QtWidgets.QAction('Edit Product', self)
        editProductContext.triggered.connect(lambda: self.editProductAction())

        self.catalog_context.addAction(addProductContext)
        self.catalog_context.addSeparator()
        self.catalog_context.addAction(viewProductContext)
        self.catalog_context.addSeparator()
        self.catalog_context.addAction(disableProductContext)
        self.catalog_context.addAction(markSoldContext)
        self.catalog_context.addAction(editProductContext)

        self.catalog_context.popup(QtGui.QCursor.pos())
        logging.debug("requested catalog context menu")

    def viewProductAction(self):
        logging.debug("clicked view product")
        row = self.catalogTable.selectionModel().selection().indexes()[0].row()
        pid = self.catalog_model.item(row, 0)

        webbrowser.open('http://www.hangarswap.com/Shop/DisplayProduct?ProductID=' + pid.text())
        logging.debug("opened product %s online", pid)
        return

    def disableProductAction(self):
        logging.debug("clicked disable product")
        row = self.catalogTable.selectionModel().selection().indexes()[0].row()
        pid = self.catalog_model.item(row, 0)

        try:
            logging.debug("sent disable request")
            NetworkSession.get("https://www.hangarswap.com/Seller/RemoveProduct?ProductID=" + pid.text())
            logging.debug("disable product %s request successful", pid)
            QtWidgets.QMessageBox.information(self, 'Success', 'Product ID ' + pid.text() + " disabled.",
                                              QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Unable to disable product.', QtWidgets.QMessageBox.Ok)

    def markProductSoldAction(self):
        logging.debug("clicked mark as sold")
        return

    def editProductAction(self):
        logging.debug("clicked edit product action")
        row = self.catalogTable.selectionModel().selection().indexes()[0].row()
        pid = self.catalog_model.item(row, 0)

        webbrowser.open('https://www.hangarswap.com/Seller/EditProduct?ProductID=' + pid.text())
        logging.debug("opened edit product %s page", pid)

    def searchOrderTable(self):
        logging.debug("searching order table, category %s, search text %s", self.orderSearchCatCombo.currentText(),
                      self.orderSearchLE.text())
        if self.orderSearchLE.text():
            search_results = self.order_model.findItems(self.orderSearchLE.text(), flags=QtCore.Qt.MatchContains,
                                                        column=self.orderSearchCatCombo.currentIndex())

            proxy_model = QtGui.QStandardItemModel(self)
            proxy_model.clear()
            proxy_model.setHorizontalHeaderLabels(
                ["OrderId", "Customer", "Product", "Date Shipped", "Qty", "Unit Price"])

            if len(search_results) > 0:
                for result in search_results:
                    row = []
                    for col in range(0, self.order_model.columnCount()):
                        row.append(self.order_model.item(result.row(), col).clone())
                    proxy_model.appendRow(row)

            self.orderTable.setModel(proxy_model)
            logging.debug("search results displayed")

        if not self.orderSearchLE.text():
            self.orderTable.setModel(self.order_model)
            logging.debug("search results cleared")

    def addProduct(self):
        logging.debug("launch add product screen")
        # addProductWidget = newProductDialog.Ui_newListing()
        # if addProductWidget.exec() == QtWidgets.QDialog.Accepted:
        #     self.loadPending()
        #     return
        logic_scripts.launchProductDialog()

    def filterPendingProductsTable(self):
        logging.debug("filter pending table")
        return

    def filterProductsTable(self):
        logging.debug("filter products table")
        if self.categoryCombo.currentText() == 'Active':
            self.loadProductCatalog("Active")
            self.productCatalogLbl.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Product Catalog - Active</span></p></body></html>")
            return
        if self.categoryCombo.currentText() == 'Inactive':
            self.loadProductCatalog("Inactive")
            self.productCatalogLbl.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Product Catalog - Inactive</span></p></body></html>")
            return
        if self.categoryCombo.currentText() == 'Disabled':
            self.loadProductCatalog("Disabled")
            self.productCatalogLbl.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Product Catalog - Disabled</span></p></body></html>")
            return
        if self.categoryCombo.currentText() == 'Sold':
            self.loadProductCatalog("Sold")
            self.productCatalogLbl.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Product Catalog - Sold</span></p></body></html>")
            return
        return

    def searchCatalogTable(self):
        logging.debug("searching order table, category %s, search text %s", self.catalogSearchColCombo.currentText(),
                      self.catalogSearchLE.text())
        if self.catalogSearchLE.text():
            catalog_search_results = self.catalog_model.findItems(self.catalogSearchLE.text(),
                                                                  flags=QtCore.Qt.MatchContains,
                                                                  column=self.catalogSearchColCombo.currentIndex())

            catalog_proxy_model = QtGui.QStandardItemModel(self)
            catalog_proxy_model.clear()
            catalog_proxy_model.setHorizontalHeaderLabels(
                ["ProductID", "Name", "Description", "MPN", "SKU", "Price", "Active", "OnSale", "Featured", "Action"])

            if len(catalog_search_results) > 0:
                for result in catalog_search_results:
                    row = []
                    for col in range(0, self.catalog_model.columnCount()):
                        row.append(self.catalog_model.item(result.row(), col).clone())
                    catalog_proxy_model.appendRow(row)

            self.catalogTable.setModel(catalog_proxy_model)
            logging.debug("search results displayed")

        if not self.catalogSearchLE.text():
            self.catalogTable.setModel(self.catalog_model)
            logging.debug("search results cleared")

    def refreshProfilePage(self):
        desc, paypal_email = logic_scripts.getProfilePage(NetworkSession)
        logging.debug("refresh profile page %s, %s", desc[0:20], paypal_email)
        self.profileDescTE.setText(desc)
        self.paypalEmailLE.setText(paypal_email)

    def loadProfile(self):
        storeName, customerName = logic_scripts.getSellerName(NetworkSession)
        logging.debug("load profile %s, %s", storeName, customerName)
        self.storeNameLbl.setText(storeName)
        self.customerNameLbl.setText(customerName)

    def loadMessages(self):
        logging.debug("Load Messages -- pinging network")
        inbox_list, unread_list, sent_list, trash_list = logic_scripts.getInbox(NetworkSession)

        self.inbox_model.clear()

        self.unread_model.setHorizontalHeaderLabels(["Sender", "Message", "button", "Time Received"])
        self.sent_model.setHorizontalHeaderLabels(["Recipient", "Message", "button", "Time Sent"])
        self.trash_model.setHorizontalHeaderLabels(["Sender", "Message", "button", "Time"])
        self.inbox_model.setHorizontalHeaderLabels(["Sender", "Message", "button", "Time Received"])

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

        logging.debug("Messages Load Success")

    def loadProductCatalog(self, category):
        global username
        if not os.path.exists("./bin/cache/"+username):
            os.makedirs("./bin/cache/"+username)
        logging.debug("loading catalog data")
        if category == "Active":
            if os.path.exists("./bin/cache/"+username+"/active_cat.dat"):
                catalog_data = []
                catalog_headers = []
                with open("./bin/cache/"+username+"/active_cat.dat") as f:
                    reader = csv.reader(f, delimiter=',')
                    catalog_headers = next(reader)
                    for row in reader:
                        catalog_data.append(row)
            if not os.path.exists("./bin/cache/"+username+"/active_cat.dat"):
                catalog_data, catalog_headers = logic_scripts.getActiveCatalog(NetworkSession)
                with open("./bin/cache/"+username+"/active_cat.dat","w",newline='') as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(catalog_headers)
                    for product in range(0, len(catalog_data)):
                        writer.writerow(catalog_data[product])
        if category == "Inactive":
            if os.path.exists("./bin/cache/"+username+"/inactive_cat.dat"):
                catalog_data = []
                catalog_headers = []
                with open("./bin/cache/"+username+"/inactive_cat.dat") as f:
                    reader = csv.reader(f, delimiter=',')
                    catalog_headers = next(reader)
                    for row in reader:
                        catalog_data.append(row)
            if not os.path.exists("./bin/cache/"+username+"/inactive_cat.dat"):
                catalog_data, catalog_headers = logic_scripts.getInactiveCatalog(NetworkSession)
                with open("./bin/cache/"+username+"/inactive_cat.dat","w",newline='') as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(catalog_headers)
                    for product in range(0, len(catalog_data)):
                        writer.writerow(catalog_data[product])
        if category == "Disabled":
            if os.path.exists("./bin/cache/"+username+"/disabled_cat.dat"):
                catalog_data = []
                catalog_headers = []
                with open("./bin/cache/"+username+"/disabled_cat.dat") as f:
                    reader = csv.reader(f, delimiter=',')
                    catalog_headers = next(reader)
                    for row in reader:
                        catalog_data.append(row)
            if not os.path.exists("./bin/cache/"+username+"/disabled_cat.dat"):
                catalog_data, catalog_headers = logic_scripts.getDisabledCatalog(NetworkSession)
                with open("./bin/cache/"+username+"/disabled_cat.dat","w",newline='') as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(catalog_headers)
                    for product in range(0, len(catalog_data)):
                        writer.writerow(catalog_data[product])
        if category == "Sold":
            if os.path.exists("./bin/cache/"+username+"/sold_cat.dat"):
                catalog_data = []
                catalog_headers = []
                with open("./bin/cache/"+username+"/sold_cat.dat") as f:
                    reader = csv.reader(f, delimiter=',')
                    catalog_headers = next(reader)
                    for row in reader:
                        catalog_data.append(row)
            if not os.path.exists("./bin/cache/"+username+"/sold_cat.dat"):
                catalog_data, catalog_headers = logic_scripts.getSoldCatalog(NetworkSession)
                with open("./bin/cache/"+username+"/sold_cat.dat","w",newline='') as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(catalog_headers)
                    for product in range(0, len(catalog_data)):
                        writer.writerow(catalog_data[product])
        self.catalog_model.clear()
        self.catalog_model.setHorizontalHeaderLabels(catalog_headers[0:8])
        for row in catalog_data:
            items = []
            for field in row[0:8]:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.catalog_model.appendRow(items)

        logging.debug("catalog loaded")

    def loadLandingListings(self):
        logging.debug("loading landing listings")
        prod1, prod2, prod3, prod4 = logic_scripts.getNewestListings(NetworkSession)

        self.prod1titleLbl.setText(prod1['title'][0:50] + "...")
        self.prod1priceLbl.setText(prod1['price'])
        self.prod1imgLbl.setPixmap(prod1['img'])

        self.prod2titleLbl.setText(prod2['title'][0:50] + "...")
        self.prod2priceLbl.setText(prod2['price'])
        self.prod2imgLbl.setPixmap(prod2['img'])

        self.prod3titleLbl.setText(prod3['title'][0:50] + "...")
        self.prod3priceLbl.setText(prod3['price'])
        self.prod3imgLbl.setPixmap(prod3['img'])

        self.prod4titleLbl.setText(prod4['title'][0:50] + "...")
        self.prod4priceLbl.setText(prod4['price'])
        self.prod4imgLbl.setPixmap(prod4['img'])

        logging.debug("landing listings loaded")

    def loadOrders(self):
        logging.debug("loading orders list")
        orders_list = logic_scripts.getOrders(NetworkSession)
        self.order_model.clear()
        self.order_model.setHorizontalHeaderLabels(["OrderId", "Customer", "Product", "Date Shipped", "Qty", "Unit Price"])
        for row in orders_list:
            items = []
            for field in row:
                value = str(field)
                items.append(QtGui.QStandardItem(value))
            self.order_model.appendRow(items)
        logging.debug("orders list loaded")

    def loadPending(self):
        self.pending_model.clear()
        self.pending_model.setHorizontalHeaderLabels(["Item Number","Title","Description","Category","Condition","Qty","Part Number","Alt P/N","S/N","SKU","Manufacturer","Price","Shipping Price","Core","Core Charge","Active","On Sale","Best Offer","Featured"])
        try:
            with open("pend.dat", "r") as r:
                reader = csv.reader(r)
                for row in reader:
                    items=[]
                    for field in row:
                        value = str(field)
                        items.append(QtGui.QStandardItem(value))
                    self.pending_model.appendRow(items)
        except:
            pass

    def pendingContextMenu(self):

        self.pending_context = QtWidgets.QMenu(self)

        addProductContext = QtWidgets.QAction('Add New Product', self)
        addProductContext.triggered.connect(self.addProduct)

        editProductContext = QtWidgets.QAction('Edit Product',self)
        editProductContext.triggered.connect(lambda: self.editPendingAction())

        uploadPendingContext = QtWidgets.QAction('Upload Product', self)
        uploadPendingContext.triggered.connect(lambda: self.uploadPendingAction())

        deleteProductContext = QtWidgets.QAction('Delete Product', self)
        deleteProductContext.triggered.connect(lambda: self.deletePendingProductAction())

        self.pending_context.addAction(addProductContext)
        self.pending_context.addAction(editProductContext)
        self.pending_context.addSeparator()
        self.pending_context.addAction(uploadPendingContext)
        self.pending_context.addSeparator()
        self.pending_context.addAction(deleteProductContext)

        self.pending_context.popup(QtGui.QCursor.pos())
        logging.debug("requested catalog context menu")

    def deletePendingProductAction(self):
        row = self.pendTable.selectionModel().selection().indexes()[0].row()
        item_num = self.pending_model.item(row, 0)

        QtWidgets.QMessageBox.information(self, 'Delete Pending',
                                     'Unimplemented: This function would delete pending item ' + str(
                                         item_num),
                                     QtWidgets.QMessageBox.Ok)
        return

    def editPendingAction(self):
        row = self.pendTable.selectionModel().selection().indexes()[0].row()
        item_num = self.pending_model.item(row, 0)

        QtWidgets.QMessageBox.information(self, 'Edit Pending',
                                     'Unimplemented: This function would open the edit dialog for item ' + str(item_num),
                                     QtWidgets.QMessageBox.Ok)
        return

    def uploadPendingAction(self):
        row = self.pendTable.selectionModel().selection().indexes()[0].row()
        item_num = self.pending_model.item(row, 0)

        QtWidgets.QMessageBox.information(self, 'Upload Pending',
                                      'Unimplemented: This function would upload item '+str(item_num),
                                      QtWidgets.QMessageBox.Ok)

def main():
    logging.debug("loading app / login")
    app = QtWidgets.QApplication(sys.argv)
    login = login_form.Ui_Dialog()
    logging.debug("setting splash pic")
    splash_pic = QPixmap('assets/imgs/loading_splash.png')
    splash = QSplashScreen(splash_pic)

    global NetworkSession
    global username

    logging.debug("displayed login")
    if login.exec() == QtWidgets.QDialog.Accepted:
        logging.debug("login accepted")
        NetworkSession, username = login.getNetSesh()
        logging.debug("showed splash")
        splash.show()
        form = HSMainWindow()
        form.show()
        splash.finish(form)
    else:
        logging.debug("login quit")
        return

    app.exec()


def getNetworkSession():
    return NetworkSession


if __name__ == '__main__':
    sys.excepthook = my_exception_hook
    logging.debug('Main Function')
    main()
