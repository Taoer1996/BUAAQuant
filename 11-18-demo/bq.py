# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 661)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.RunButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RunButton.sizePolicy().hasHeightForWidth())
        self.RunButton.setSizePolicy(sizePolicy)
        self.RunButton.setObjectName("RunButton")
        self.horizontalLayout.addWidget(self.RunButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.BeginDate = QtWidgets.QDateEdit(self.centralWidget)
        self.BeginDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 1), QtCore.QTime(0, 0, 0)))
        self.BeginDate.setDate(QtCore.QDate(2016, 1, 1))
        self.BeginDate.setObjectName("BeginDate")
        self.horizontalLayout_2.addWidget(self.BeginDate)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.EndDate = QtWidgets.QDateEdit(self.centralWidget)
        self.EndDate.setDate(QtCore.QDate(2016, 10, 1))
        self.EndDate.setObjectName("EndDate")
        self.horizontalLayout_2.addWidget(self.EndDate)
        spacerItem3 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.TrainButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TrainButton.sizePolicy().hasHeightForWidth())
        self.TrainButton.setSizePolicy(sizePolicy)
        self.TrainButton.setObjectName("TrainButton")
        self.horizontalLayout_2.addWidget(self.TrainButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.webView = QtWebKitWidgets.QWebView(self.centralWidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout_2.addWidget(self.webView)
        self.OutputText = QtWidgets.QTextEdit(self.centralWidget)
        self.OutputText.setObjectName("OutputText")
        self.verticalLayout_2.addWidget(self.OutputText)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1067, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveButton.setText(_translate("MainWindow", "SAVE"))
        self.RunButton.setText(_translate("MainWindow", "RUN"))
        self.label.setText(_translate("MainWindow", "BeginDate"))
        self.BeginDate.setDisplayFormat(_translate("MainWindow", "yyyy/M/d"))
        self.label_2.setText(_translate("MainWindow", "EndDate"))
        self.EndDate.setDisplayFormat(_translate("MainWindow", "yyyy/M/d"))
        self.TrainButton.setText(_translate("MainWindow", "TRAIN_HMM"))

from PyQt5 import QtWebKitWidgets