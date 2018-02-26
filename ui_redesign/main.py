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
from PyQt5.QtWidgets import QMessageBox
from requests_toolbelt.multipart.encoder import MultipartEncoder

#importing external widgets
import login_form
import main_window_redesign
import new_product_widget

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
        #self.inboxTable.resizeColumnstoContents()

        self.loadProfile()





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
        return

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

        messagesList = logic_scripts.getInbox(NetworkSession)
        messagesTemp = messagesList.values.tolist()
        print(messagesTemp)
        self.inbox_model.clear()
        for row in messagesTemp:
           items = []
           for field in row:
             value = str(field)
             items.append(QtGui.QStandardItem(value))
           self.inbox_model.appendRow(items)
        #self.inboxTable.resizeColumnstoContents()








def main():
    app = QtWidgets.QApplication(sys.argv)
    login = login_form.Ui_Dialog()

    global NetworkSession

    if login.exec() == QtWidgets.QDialog.Accepted:
        NetworkSession = login.getNetSesh()
        form = HSMainWindow('')
        form.show()
    else:
        return

    app.exec()


if __name__ == '__main__':
    sys.excepthook = my_exception_hook

    main()
