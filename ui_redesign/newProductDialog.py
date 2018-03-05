# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProductDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import imghdr, logic_scripts, main


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

class Ui_newListing(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_newListing, self).__init__(parent)

        self.setObjectName("newListing")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(621, 644)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 1, 381, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newproduct_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newproduct_lbl.sizePolicy().hasHeightForWidth())
        self.newproduct_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.newproduct_lbl.setFont(font)
        self.newproduct_lbl.setObjectName("newproduct_lbl")
        self.verticalLayout.addWidget(self.newproduct_lbl)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, -1, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.name_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_lbl.setObjectName("name_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_lbl)
        self.name_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_le.setObjectName("name_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_le)
        self.desc_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.desc_lbl.setObjectName("desc_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.desc_lbl)
        self.desc_te = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.desc_te.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.desc_te.setObjectName("desc_te")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.desc_te)
        self.cat_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cat_lbl.setObjectName("cat_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cat_lbl)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cat_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cat_options.sizePolicy().hasHeightForWidth())
        self.cat_options.setSizePolicy(sizePolicy)
        self.cat_options.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cat_options.setObjectName("cat_options")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.horizontalLayout_10.addWidget(self.cat_options)
        self.subcat_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.subcat_options.setFrame(True)
        self.subcat_options.setObjectName("subcat_options")
        self.subcat_options.addItem("")
        self.horizontalLayout_10.addWidget(self.subcat_options)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.cond_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cond_lbl.setObjectName("cond_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cond_lbl)
        self.cond_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cond_options.sizePolicy().hasHeightForWidth())
        self.cond_options.setSizePolicy(sizePolicy)
        self.cond_options.setMinimumSize(QtCore.QSize(50, 20))
        self.cond_options.setBaseSize(QtCore.QSize(50, 0))
        self.cond_options.setObjectName("cond_options")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cond_options)
        self.qty_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qty_lbl.setObjectName("qty_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.qty_lbl)
        self.qty_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qty_le.setObjectName("qty_le")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.qty_le)
        self.mpn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mpn_lbl.setObjectName("mpn_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.mpn_lbl)
        self.pn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pn_le.setObjectName("pn_le")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pn_le)
        self.ampn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ampn_lbl.setObjectName("ampn_lbl")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ampn_lbl)
        self.apn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.apn_le.setObjectName("apn_le")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.apn_le)
        self.sn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sn_lbl.setObjectName("sn_lbl")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.sn_lbl)
        self.sn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sn_le.setObjectName("sn_le")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sn_le)
        self.sku_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sku_lbl.setObjectName("sku_lbl")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.sku_lbl)
        self.sku_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sku_le.setObjectName("sku_le")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sku_le)
        self.mfr_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mfr_lbl.setObjectName("mfr_lbl")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.mfr_lbl)
        self.mfr_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mfr_le.setObjectName("mfr_le")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.mfr_le)
        self.price_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.price_lbl.setObjectName("price_lbl")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.price_lbl)
        self.price_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.price_le.setObjectName("price_le")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.price_le)
        self.ship_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ship_lbl.setObjectName("ship_lbl")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.ship_lbl)
        self.ship_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ship_le.setObjectName("ship_le")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ship_le)
        self.core_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.core_lbl.setObjectName("core_lbl")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.core_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.core_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.core_yes.sizePolicy().hasHeightForWidth())
        self.core_yes.setSizePolicy(sizePolicy)
        self.core_yes.setObjectName("core_yes")
        self.horizontalLayout.addWidget(self.core_yes)
        self.core_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.core_no.sizePolicy().hasHeightForWidth())
        self.core_no.setSizePolicy(sizePolicy)
        self.core_no.setObjectName("core_no")
        self.horizontalLayout.addWidget(self.core_no)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.img_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_lbl.setObjectName("img_lbl")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.img_lbl)
        self.img_upload_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_upload_btn.sizePolicy().hasHeightForWidth())
        self.img_upload_btn.setSizePolicy(sizePolicy)
        self.img_upload_btn.setObjectName("img_upload_btn")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.img_upload_btn)
        self.active_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.active_lbl.setObjectName("active_lbl")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.active_lbl)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.active_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_yes.sizePolicy().hasHeightForWidth())
        self.active_yes.setSizePolicy(sizePolicy)
        self.active_yes.setObjectName("active_yes")
        self.horizontalLayout_6.addWidget(self.active_yes)
        self.active_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.active_no.setObjectName("active_no")
        self.horizontalLayout_6.addWidget(self.active_no)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.onsale_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.onsale_lbl.setObjectName("onsale_lbl")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.onsale_lbl)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sale_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sale_yes.sizePolicy().hasHeightForWidth())
        self.sale_yes.setSizePolicy(sizePolicy)
        self.sale_yes.setObjectName("sale_yes")
        self.horizontalLayout_7.addWidget(self.sale_yes)
        self.sale_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sale_no.setObjectName("sale_no")
        self.horizontalLayout_7.addWidget(self.sale_no)
        self.formLayout.setLayout(15, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.offer_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.offer_lbl.setObjectName("offer_lbl")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.offer_lbl)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.offer_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offer_yes.sizePolicy().hasHeightForWidth())
        self.offer_yes.setSizePolicy(sizePolicy)
        self.offer_yes.setObjectName("offer_yes")
        self.horizontalLayout_8.addWidget(self.offer_yes)
        self.offer_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.offer_no.setObjectName("offer_no")
        self.horizontalLayout_8.addWidget(self.offer_no)
        self.formLayout.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.feat_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.feat_lbl.setObjectName("feat_lbl")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.feat_lbl)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.feat_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feat_yes.sizePolicy().hasHeightForWidth())
        self.feat_yes.setSizePolicy(sizePolicy)
        self.feat_yes.setObjectName("feat_yes")
        self.horizontalLayout_9.addWidget(self.feat_yes)
        self.feat_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.feat_no.setObjectName("feat_no")
        self.horizontalLayout_9.addWidget(self.feat_no)
        self.formLayout.setLayout(17, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.formLayout)
        self.img_groupbox = QtWidgets.QGroupBox(self)
        self.img_groupbox.setGeometry(QtCore.QRect(389, 0, 221, 601))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.img_groupbox.setFont(font)
        self.img_groupbox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.img_groupbox.setObjectName("img_groupbox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.img_groupbox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 201, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.img3_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img3_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img3_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img3_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img3_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img3_lbl.setText("")
        self.img3_lbl.setObjectName("img3_lbl")
        self.gridLayout.addWidget(self.img3_lbl, 1, 0, 1, 1)
        self.img6_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img6_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img6_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img6_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img6_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img6_lbl.setText("")
        self.img6_lbl.setObjectName("img6_lbl")
        self.gridLayout.addWidget(self.img6_lbl, 2, 1, 1, 1)
        self.img7_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img7_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img7_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img7_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img7_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img7_lbl.setText("")
        self.img7_lbl.setObjectName("img7_lbl")
        self.gridLayout.addWidget(self.img7_lbl, 3, 0, 1, 1)
        self.img8_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img8_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img8_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img8_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img8_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img8_lbl.setText("")
        self.img8_lbl.setObjectName("img8_lbl")
        self.gridLayout.addWidget(self.img8_lbl, 3, 1, 1, 1)
        self.img5_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img5_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img5_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img5_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img5_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img5_lbl.setText("")
        self.img5_lbl.setObjectName("img5_lbl")
        self.gridLayout.addWidget(self.img5_lbl, 2, 0, 1, 1)
        self.img4_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img4_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img4_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img4_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img4_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img4_lbl.setText("")
        self.img4_lbl.setObjectName("img4_lbl")
        self.gridLayout.addWidget(self.img4_lbl, 1, 1, 1, 1)
        self.img1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img1_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img1_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img1_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img1_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img1_lbl.setText("")
        self.img1_lbl.setObjectName("img1_lbl")
        self.gridLayout.addWidget(self.img1_lbl, 0, 0, 1, 1)
        self.img2_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img2_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img2_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img2_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img2_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img2_lbl.setText("")
        self.img2_lbl.setObjectName("img2_lbl")
        self.gridLayout.addWidget(self.img2_lbl, 0, 1, 1, 1)
        self.img9_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img9_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img9_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img9_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img9_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img9_lbl.setText("")
        self.img9_lbl.setObjectName("img9_lbl")
        self.gridLayout.addWidget(self.img9_lbl, 4, 0, 1, 1)
        self.img10_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img10_lbl.setBaseSize(QtCore.QSize(97, 109))
        self.img10_lbl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.img10_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img10_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img10_lbl.setText("")
        self.img10_lbl.setObjectName("img10_lbl")
        self.gridLayout.addWidget(self.img10_lbl, 4, 1, 1, 1)
        self.img10_lbl.raise_()
        self.img9_lbl.raise_()
        self.img7_lbl.raise_()
        self.img2_lbl.raise_()
        self.img5_lbl.raise_()
        self.img8_lbl.raise_()
        self.img6_lbl.raise_()
        self.img4_lbl.raise_()
        self.img1_lbl.raise_()
        self.img3_lbl.raise_()
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 601, 381, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_11.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.upload_new_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.upload_new_button.setObjectName("upload_new_button")
        self.horizontalLayout_11.addWidget(self.upload_new_button)
        self.save_templ_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.save_templ_button.setObjectName("save_templ_button")
        self.horizontalLayout_11.addWidget(self.save_templ_button)
        self.cancel_new_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.cancel_new_button.setObjectName("cancel_new_button")
        self.horizontalLayout_11.addWidget(self.cancel_new_button)

        self.core_btnGroup = QtWidgets.QButtonGroup(self)
        self.core_btnGroup.setObjectName("core_btnGroup")
        self.core_btnGroup.addButton(self.core_yes)
        self.core_btnGroup.addButton(self.core_no)

        self.active_btnGroup = QtWidgets.QButtonGroup(self)
        self.active_btnGroup.setObjectName("active_btnGroup")
        self.active_btnGroup.addButton(self.active_yes)
        self.active_btnGroup.addButton(self.active_no)

        self.sale_btnGroup = QtWidgets.QButtonGroup(self)
        self.sale_btnGroup.setObjectName("sale_btnGroup")
        self.sale_btnGroup.addButton(self.sale_yes)
        self.sale_btnGroup.addButton(self.sale_no)

        self.offer_btnGroup = QtWidgets.QButtonGroup(self)
        self.offer_btnGroup.setObjectName("offer_btnGroup")
        self.offer_btnGroup.addButton(self.offer_yes)
        self.offer_btnGroup.addButton(self.offer_no)

        self.feat_btnGroup = QtWidgets.QButtonGroup(self)
        self.feat_btnGroup.setObjectName("feat_btnGroup")
        self.feat_btnGroup.addButton(self.feat_yes)
        self.feat_btnGroup.addButton(self.feat_no)



        self.retranslateUi()
        self.cat_options.setCurrentIndex(0)
        self.upload_new_button.clicked.connect(self.uploadProduct)
        self.save_templ_button.clicked.connect(self.saveProduct)
        self.cancel_new_button.clicked.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.img_names = {}

        self.img_upload_btn.clicked.connect(self.insertImages)

        # checks to see if 'Category' option has been changed
        self.cat_options.currentTextChanged.connect(self.changedCat)

        # context menu assignment for image thumbnails
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("newListing", "List a New Product"))
        self.newproduct_lbl.setText(_translate("newListing", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create New Product</span></p></body></html>"))
        self.name_lbl.setText(_translate("newListing", "Product Name*"))
        self.desc_lbl.setText(_translate("newListing", "Product Description*"))
        self.cat_lbl.setText(_translate("newListing", "Product Category*"))
        self.cat_options.setItemText(0, _translate("newListing", "Airboat"))
        self.cat_options.setItemText(1, _translate("newListing", "Aircraft For Sale"))
        self.cat_options.setItemText(2, _translate("newListing", "Airframe"))
        self.cat_options.setItemText(3, _translate("newListing", "Art"))
        self.cat_options.setItemText(4, _translate("newListing", "Avionics"))
        self.cat_options.setItemText(5, _translate("newListing", "Electrical"))
        self.cat_options.setItemText(6, _translate("newListing", "Experimental"))
        self.cat_options.setItemText(7, _translate("newListing", "Hardware & Tools"))
        self.cat_options.setItemText(8, _translate("newListing", "Landing Gear"))
        self.cat_options.setItemText(9, _translate("newListing", "Misc"))
        self.cat_options.setItemText(10, _translate("newListing", "Pilot Supplies"))
        self.cat_options.setItemText(11, _translate("newListing", "Powerplant"))
        self.cat_options.setItemText(12, _translate("newListing", "Wheels & Brakes"))
        self.subcat_options.setItemText(0, _translate("newListing", "---"))
        self.cond_lbl.setText(_translate("newListing", "Product Condition*"))
        self.cond_options.setItemText(0, _translate("newListing", "As Removed"))
        self.cond_options.setItemText(1, _translate("newListing", "Serviceable"))
        self.cond_options.setItemText(2, _translate("newListing", "Overhauled"))
        self.cond_options.setItemText(3, _translate("newListing", "New Stock"))
        self.cond_options.setItemText(4, _translate("newListing", "Repairable"))
        self.cond_options.setItemText(5, _translate("newListing", "New Surplus (NOS)"))
        self.cond_options.setItemText(6, _translate("newListing", "Beyond Repair"))
        self.cond_options.setItemText(7, _translate("newListing", "Unknown"))
        self.cond_options.setItemText(8, _translate("newListing", "Core"))
        self.qty_lbl.setText(_translate("newListing", "Qty Available*"))
        self.mpn_lbl.setText(_translate("newListing", "Part Number"))
        self.ampn_lbl.setText(_translate("newListing", "Alt Part Number"))
        self.sn_lbl.setText(_translate("newListing", "Serial Number"))
        self.sku_lbl.setText(_translate("newListing", "SKU"))
        self.mfr_lbl.setText(_translate("newListing", "Manufacturer"))
        self.price_lbl.setText(_translate("newListing", "Price*"))
        self.ship_lbl.setText(_translate("newListing", "Shipping Cost*"))
        self.core_lbl.setText(_translate("newListing", "Has Core Charge?"))
        self.core_yes.setText(_translate("newListing", "Yes"))
        self.core_no.setText(_translate("newListing", "No"))
        self.img_lbl.setText(_translate("newListing", "Product Images"))
        self.img_upload_btn.setText(_translate("newListing", "Choose Files"))
        self.active_lbl.setText(_translate("newListing", "Active"))
        self.active_yes.setText(_translate("newListing", "Yes"))
        self.active_no.setText(_translate("newListing", "No"))
        self.onsale_lbl.setText(_translate("newListing", "On Sale"))
        self.sale_yes.setText(_translate("newListing", "Yes"))
        self.sale_no.setText(_translate("newListing", "No"))
        self.offer_lbl.setText(_translate("newListing", "Allow Best Offer"))
        self.offer_yes.setText(_translate("newListing", "Yes"))
        self.offer_no.setText(_translate("newListing", "No"))
        self.feat_lbl.setText(_translate("newListing", "Featured"))
        self.feat_yes.setText(_translate("newListing", "Yes"))
        self.feat_no.setText(_translate("newListing", "No"))
        self.img_groupbox.setTitle(_translate("newListing", "Product Images"))
        self.upload_new_button.setText(_translate("newListing", "Upload"))
        self.save_templ_button.setText(_translate("newListing", "Upload Later"))
        self.cancel_new_button.setText(_translate("newListing", "Cancel"))

    def changedCat(self):
        # clears and displays relevant subcategories
        self.subcat_options.clear()
        #adds appropriate subcategories to subcat widget
        if self.cat_options.currentText() == 'Airboat':
            self.subcat_options.addItems(airboat_subcats)
        if self.cat_options.currentText() == 'Aircraft For Sale':
            self.subcat_options.addItems(aircraft_for_sale_subcats)
        if self.cat_options.currentText() == 'Airframe':
            self.subcat_options.addItems(airframe_subcats)
        if self.cat_options.currentText() == 'Avionics':
            self.subcat_options.addItems(avionics_subcats)
        if self.cat_options.currentText() == 'Electrical':
            self.subcat_options.addItems(electrical_subcats)
        if self.cat_options.currentText() == 'Hardware & Tools':
            self.subcat_options.addItems(hardware_subcats)
        if self.cat_options.currentText() == 'Landing Gear':
            self.subcat_options.addItems(gear_subcats)
        if self.cat_options.currentText() == 'Pilot Supplies':
            self.subcat_options.addItems(pilot_supp_subcats)
        if self.cat_options.currentText() == 'Powerplant':
            self.subcat_options.addItems(powerplant_subcats)

    def contextMenuEvent(self, event):
        #creates a context menu for image thumbnails
        self.menu2 = QtWidgets.QMenu(self)

        #creating actions for context menu
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

        #show context menu at cursor location
        self.menu2.popup(QtGui.QCursor.pos())
        w = QtWidgets.QApplication.widgetAt(QtGui.QCursor.pos())

    def defaultPhotoContext(self, event):
        #method for setting default image
        #gets image widget at cursor location
        pos = QtGui.QCursor.pos()
        w = QtWidgets.QApplication.widgetAt(pos)

        #instance temporary image holder lists / temporary img
        temp_list =[]
        temp = self.img_names.get(w.objectName())

        #remove selected image from dict and populate temp list
        del self.img_names[w.objectName()]
        for labels, imgs in self.img_names.items():
            temp_list.append(imgs)
        self.img_names.clear()

        #reinsert temp img
        temp_list.insert(0, temp)

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
            pixmap = QPixmap(temp_list[img])
            pixmap = QPixmap(pixmap.scaled(97, 97))
            if col == 2:
                col = 0
                row += 1
            w = self.gridLayout.itemAtPosition(row, col).widget()
            self.img_names[w.objectName()]=temp_list[img]
            w.setPixmap(QPixmap(pixmap))
            col += 1

    def removePhotoContext(self, event):
        #get lbl at cursor, and remove from images dict
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
        img, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Images", (QtCore.QDir.homePath()))
        pixmap = QPixmap(img)
        pixmap = QPixmap(pixmap.scaled(97, 97))
        w.setPixmap(pixmap)
        self.img_names[w.objectName()]=img

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

    def processForm(self, img_names):

        # processing data from text fields
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
            'Active': '',
            'OnSale': '',
            'AllowBestOffer': '',
            'Featured': '',
        }

        try:
            item_form['productImage'] = ('filename', open(self.img_names['img1_lbl'], 'rb'),
                             ('image/' + str(imghdr.what(self.img_names['img1_lbl']))))
        except:
            item_form['productImage'] = ''

        # processing button choices
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
            if self.subcat_options.currentText() == 'Airboats':
                item_form['CategoryID'] = '25'
            if self.subcat_options.currentText() == 'Engines':
                item_form['CategoryID'] = '22'
            if self.subcat_options.currentText() == 'Hulls':
                item_form['CategoryID'] = '24'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '26'
            if self.subcat_options.currentText() == 'Parts':
                item_form['CategoryID'] = '23'
        if self.cat_options.currentText() == 'Aircraft For Sale':
            item_form['CategoryID'] = '1'
            if self.subcat_options.currentText() == 'Aircraft for Sale':
                item_form['CategoryID'] = '13'
            if self.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '16'
            if self.subcat_options.currentText() == 'Helicopters':
                item_form['CategoryID'] = '17'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '21'
            if self.subcat_options.currentText() == 'Projects':
                item_form['CategoryID'] = '12'
            if self.subcat_options.currentText() == 'Singles':
                item_form['CategoryID'] = '18'
            if self.subcat_options.currentText() == 'Twins':
                item_form['CategoryID'] = '19'
        if self.cat_options.currentText() == 'Airframe':
            item_form['CategoryID'] = '3'
            if self.subcat_options.currentText() == 'Aerobatic':
                item_form['CategoryID'] = '28'
            if self.subcat_options.currentText() == 'Aeronca':
                item_form['CategoryID'] = '27'
            if self.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '29'
            if self.subcat_options.currentText() == 'Antique':
                item_form['CategoryID'] = '30'
            if self.subcat_options.currentText() == 'Beechcraft':
                item_form['CategoryID'] = '31'
            if self.subcat_options.currentText() == 'Bellanca':
                item_form['CategoryID'] = '32'
            if self.subcat_options.currentText() == 'Cessna':
                item_form['CategoryID'] = '33'
            if self.subcat_options.currentText() == 'Cirrus':
                item_form['CategoryID'] = '34'
            if self.subcat_options.currentText() == 'Control Surfaces':
                item_form['CategoryID'] = '35'
            if self.subcat_options.currentText() == 'General Parts':
                item_form['CategoryID'] = '117'
            if self.subcat_options.currentText() == 'Helicopter':
                item_form['CategoryID'] = '37'
            if self.subcat_options.currentText() == 'Interior':
                item_form['CategoryID'] = '38'
            if self.subcat_options.currentText() == 'Luscombe':
                item_form['CategoryID'] = '39'
            if self.subcat_options.currentText() == 'Mooney':
                item_form['CategoryID'] = '40'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '44'
            if self.subcat_options.currentText() == 'Piper':
                item_form['CategoryID'] = '41'
            if self.subcat_options.currentText() == 'Taylorcraft':
                item_form['CategoryID'] = '42'
            if self.subcat_options.currentText() == 'Warbird':
                item_form['CategoryID'] = '43'
        if self.cat_options.currentText() == 'Art':
            item_form['CategoryID'] = '4'
        if self.cat_options.currentText() == 'Avionics':
            item_form['CategoryID'] = '5'
            if self.subcat_options.currentText() == 'Antennas':
                item_form['CategoryID'] = '45'
            if self.subcat_options.currentText() == 'Audio Panels':
                item_form['CategoryID'] = '46'
            if self.subcat_options.currentText() == 'AutoPilot':
                item_form['CategoryID'] = '47'
            if self.subcat_options.currentText() == 'ELTs':
                item_form['CategoryID'] = '48'
            if self.subcat_options.currentText() == 'Engine Monitors':
                item_form['CategoryID'] = '49'
            if self.subcat_options.currentText() == 'GPS':
                item_form['CategoryID'] = '50'
            if self.subcat_options.currentText() == 'Indicators':
                item_form['CategoryID'] = '51'
            if self.subcat_options.currentText() == 'Intercoms':
                item_form['CategoryID'] = '52'
            if self.subcat_options.currentText() == 'Nav/Coms':
                item_form['CategoryID'] = '53'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '59'
            if self.subcat_options.currentText() == 'Packages':
                item_form['CategoryID'] = '54'
            if self.subcat_options.currentText() == 'Pitot Tubes':
                item_form['CategoryID'] = '55'
            if self.subcat_options.currentText() == 'Transponders':
                item_form['CategoryID'] = '56'
            if self.subcat_options.currentText() == 'Trays & Connectors':
                item_form['CategoryID'] = '57'
            if self.subcat_options.currentText() == 'Weather Systems':
                item_form['CategoryID'] = '58'
        if self.cat_options.currentText() == 'Electrical':
            item_form['CategoryID'] = '6'
            if self.subcat_options.currentText() == 'Batteries':
                item_form['CategoryID'] = '60'
            if self.subcat_options.currentText() == 'Lighting':
                item_form['CategoryID'] = '61'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '62'
        if self.cat_options.currentText() == 'Experimental':
            item_form['CategoryID'] = '8'
        if self.cat_options.currentText() == 'Hardware & Tools':
            item_form['CategoryID'] = '7'
            if self.subcat_options.currentText() == 'Jacks':
                item_form['CategoryID'] = '63'
            if self.subcat_options.currentText() == 'Nuts & Bolts':
                item_form['CategoryID'] = '64'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '68'
            if self.subcat_options.currentText() == 'Rivets':
                item_form['CategoryID'] = '65'
            if self.subcat_options.currentText() == 'Testing Equipment':
                item_form['CategoryID'] = '67'
            if self.subcat_options.currentText() == 'Tools':
                item_form['CategoryID'] = '66'
        if self.cat_options.currentText() == 'Landing Gear':
            item_form['CategoryID'] = '14'
            if self.subcat_options.currentText() == 'Amphibian':
                item_form['CategoryID'] = '69'
            if self.subcat_options.currentText() == 'Skis':
                item_form['CategoryID'] = '70'
            if self.subcat_options.currentText() == 'Tailwheel':
                item_form['CategoryID'] = '71'
            if self.subcat_options.currentText() == 'Tires & Tubes':
                item_form['CategoryID'] = '72'
            if self.subcat_options.currentText() == 'Wheels & Brakes':
                item_form['CategoryID'] = '73'
        if self.cat_options.currentText() == 'Misc':
            item_form['CategoryID'] = '9'
        if self.cat_options.currentText() == 'Pilot Supplies':
            item_form['CategoryID'] = '15'
            if self.subcat_options.currentText() == 'Aviator Accessories':
                item_form['CategoryID'] = '74'
            if self.subcat_options.currentText() == 'Bags':
                item_form['CategoryID'] = '75'
            if self.subcat_options.currentText() == 'Books':
                item_form['CategoryID'] = '76'
            if self.subcat_options.currentText() == 'Collectibles':
                item_form['CategoryID'] = '77'
            if self.subcat_options.currentText() == 'Covers & Accessories':
                item_form['CategoryID'] = '78'
            if self.subcat_options.currentText() == 'Headsets':
                item_form['CategoryID'] = '79'
            if self.subcat_options.currentText() == 'Manuals':
                item_form['CategoryID'] = '80'
            if self.subcat_options.currentText() == 'Oils, Liquids, & Sprays':
                item_form['CategoryID'] = '81'
            if self.subcat_options.currentText() == 'Other':
                item_form['CategoryID'] = '86'
            if self.subcat_options.currentText() == 'Pilot Wear':
                item_form['CategoryID'] = '82'
            if self.subcat_options.currentText() == 'Safety':
                item_form['CategoryID'] = '83'
            if self.subcat_options.currentText() == 'Stickers & Decals':
                item_form['CategoryID'] = '84'
            if self.subcat_options.currentText() == 'Tow':
                item_form['CategoryID'] = '85'
        if self.cat_options.currentText() == 'Powerplant':
            item_form['CategoryID'] = '10'
            if self.subcat_options.currentText() == 'Engine Parts':
                item_form['CategoryID'] = '88'
            if self.subcat_options.currentText() == 'Engines':
                item_form['CategoryID'] = '87'
            if self.subcat_options.currentText() == 'Environmental':
                item_form['CategoryID'] = '118'
            if self.subcat_options.currentText() == 'Exhaust':
                item_form['CategoryID'] = '89'
            if self.subcat_options.currentText() == 'Fuel System':
                item_form['CategoryID'] = '90'
            if self.subcat_options.currentText() == 'General Parts':
                item_form['CategoryID'] = '116'
            if self.subcat_options.currentText() == 'Propellers':
                item_form['CategoryID'] = '91'
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

        return (item_form, self.img_names)


    def uploadProduct(self):
        item_form, img_names = self.processForm(self.img_names)
        validate_code = logic_scripts.validateForm(item_form)
        if validate_code == 0:
            return
        else:
            QtWidgets.QMessageBox.warning(self, 'Product Error', 'Please complete required field: ' + validate_code, QtWidgets.QMessageBox.Ok)
            return

    def saveProduct(self):
        item_form, img_names = self.processForm(self.img_names)
        validate_code = logic_scripts.validateForm(item_form)
        if validate_code == 0:
            NetworkSession = main.getNetworkSession()
            logic_scripts.submitItem(item_form, img_names, NetworkSession)
        else:
            QtWidgets.QMessageBox.warning(self, 'Product Error', 'Please complete required field: ' + validate_code,
                                          QtWidgets.QMessageBox.Ok)
            return

    def reject(self):
        self.done(0)