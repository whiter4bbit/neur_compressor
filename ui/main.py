# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Oct 13 02:00:49 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 699)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 851, 281))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.srcScrollArea = QtGui.QScrollArea(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcScrollArea.sizePolicy().hasHeightForWidth())
        self.srcScrollArea.setSizePolicy(sizePolicy)
        self.srcScrollArea.setWidgetResizable(True)
        self.srcScrollArea.setObjectName("srcScrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.srcScrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 418, 275))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.srcScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comprScrollArea = QtGui.QScrollArea(self.splitter)
        self.comprScrollArea.setWidgetResizable(True)
        self.comprScrollArea.setObjectName("comprScrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.comprScrollArea)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 418, 275))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.comprScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.teachW1ProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.teachW1ProgressBar.setGeometry(QtCore.QRect(430, 300, 431, 23))
        self.teachW1ProgressBar.setProperty("value", QtCore.QVariant(24))
        self.teachW1ProgressBar.setObjectName("teachW1ProgressBar")
        self.teachW2ProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.teachW2ProgressBar.setGeometry(QtCore.QRect(430, 330, 431, 23))
        self.teachW2ProgressBar.setProperty("value", QtCore.QVariant(24))
        self.teachW2ProgressBar.setObjectName("teachW2ProgressBar")
        self.teachButton = QtGui.QPushButton(self.centralwidget)
        self.teachButton.setGeometry(QtCore.QRect(310, 330, 114, 27))
        self.teachButton.setObjectName("teachButton")
        self.debugEdit = QtGui.QTextEdit(self.centralwidget)
        self.debugEdit.setGeometry(QtCore.QRect(10, 360, 851, 291))
        self.debugEdit.setObjectName("debugEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 24))
        self.menubar.setObjectName("menubar")
        self.menuImage = QtGui.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuImage.addAction(self.actionOpen)
        self.menubar.addAction(self.menuImage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.teachButton.setText(QtGui.QApplication.translate("MainWindow", "Teach", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImage.setTitle(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))

