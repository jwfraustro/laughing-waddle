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
import edit_product_widget
import orders_widget
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

        self.ordersBtn.clicked.connect(self.initOrdersList)

    def initOrdersList(self):
        self.order_widget = orders_widget.Ui_catalogWidget()
        self.order_widget.setupUi(self.widget)

def main():
    app = QtWidgets.QApplication(sys.argv)

    form = HSMainWindow('')

    form.show()

    app.exec()


if __name__ == '__main__':
    sys.excepthook = my_exception_hook

    main()
