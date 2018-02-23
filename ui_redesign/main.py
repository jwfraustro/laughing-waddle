#importing misc modules
import csv
import imghdr
import sys

#importing networking modules
import bs4
import requests
import webbrowser

#importing GUI elements
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from requests_toolbelt.multipart.encoder import MultipartEncoder

#importing external widgets
import main_window_redesign
import new_product_widget

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

    def initOrdersView(self):
        self.stackedWidget.setCurrentWidget(self.ordersPage)
    def initInboxView(self):
        self.stackedWidget.setCurrentWidget(self.inboxPage)
    def initProductsView(self):
        self.stackedWidget.setCurrentWidget(self.catalogPage)
    def initPendingView(self):
        self.stackedWidget.setCurrentWidget(self.pendingPage)
    def initProfileView(self):
        self.stackedWidget.setCurrentWidget(self.profilePage)
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


def main():
    app = QtWidgets.QApplication(sys.argv)

    form = HSMainWindow('')

    form.show()

    app.exec()


if __name__ == '__main__':
    sys.excepthook = my_exception_hook

    main()
