# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J:\Projects\OCR\ocr-gui-demo\guiocr\widgets\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 689)
        MainWindow.setStyleSheet("QWidget{\n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"}\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBoxLanguage = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxLanguage.setPlaceholderText("")
        self.comboBoxLanguage.setFrame(False)
        self.comboBoxLanguage.setObjectName("comboBoxLanguage")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxLanguage)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.checkBox_ocr = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ocr.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_ocr.setChecked(True)
        self.checkBox_ocr.setObjectName("checkBox_ocr")
        self.horizontalLayout_4.addWidget(self.checkBox_ocr)
        # self.checkBox_det = QtWidgets.QCheckBox(self.groupBox)
        # self.checkBox_det.setObjectName("checkBox_det")
        # self.horizontalLayout_4.addWidget(self.checkBox_det)
        # self.checkBox_recog = QtWidgets.QCheckBox(self.groupBox)
        # self.checkBox_recog.setObjectName("checkBox_recog")
        # self.horizontalLayout_4.addWidget(self.checkBox_recog)
        # self.checkBox_layoutparser = QtWidgets.QCheckBox(self.groupBox)
        # self.checkBox_layoutparser.setCheckable(True)
        # self.checkBox_layoutparser.setObjectName("checkBox_layoutparser")
        # self.horizontalLayout_4.addWidget(self.checkBox_layoutparser)
        self.btnStartProcess = QtWidgets.QPushButton(self.groupBox)
        self.btnStartProcess.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnStartProcess.setFont(font)
        self.btnStartProcess.setAutoFillBackground(False)
        self.btnStartProcess.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 160, 230) ;\n"
"border-radius: 5px;\n"
"height: 28;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px bold;\n"
"margin: 2px 2px;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"border: 2px solid rgb(0, 160, 230);\n"
"color: black\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 255, 40);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/zsy/.designer/icons/done_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStartProcess.setIcon(icon)
        self.btnStartProcess.setFlat(False)
        self.btnStartProcess.setObjectName("btnStartProcess")
        self.horizontalLayout_4.addWidget(self.btnStartProcess)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnOpenImg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenImg.sizePolicy().hasHeightForWidth())
        self.btnOpenImg.setSizePolicy(sizePolicy)
        self.btnOpenImg.setMinimumSize(QtCore.QSize(0, 0))
        self.btnOpenImg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnOpenImg.setObjectName("btnOpenImg")
        self.verticalLayout_5.addWidget(self.btnOpenImg)
        self.btnOpenDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenDir.setObjectName("btnOpenDir")
        self.verticalLayout_5.addWidget(self.btnOpenDir)
        # self.btnEditShape = QtWidgets.QPushButton(self.centralwidget)
        # self.btnEditShape.setObjectName("btnEditShape")
        # self.verticalLayout_5.addWidget(self.btnEditShape)
        # self.btnAddShape = QtWidgets.QPushButton(self.centralwidget)
        # self.btnAddShape.setObjectName("btnAddShape")
        # self.verticalLayout_5.addWidget(self.btnAddShape)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.verticalLayout_5.addWidget(self.btnNext)
        self.btnPrev = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrev.setObjectName("btnPrev")
        self.verticalLayout_5.addWidget(self.btnPrev)
        # self.btnBrightness = QtWidgets.QPushButton(self.centralwidget)
        # self.btnBrightness.setObjectName("btnBrightness")
        # self.verticalLayout_5.addWidget(self.btnBrightness)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.scrollAreaCanvas = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaCanvas.setWidgetResizable(True)
        self.scrollAreaCanvas.setObjectName("scrollAreaCanvas")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 741, 528))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaCanvas.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollAreaCanvas)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidgetResult = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetResult.setObjectName("tabWidgetResult")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollAreaLabellist = QtWidgets.QScrollArea(self.tab)
        self.scrollAreaLabellist.setWidgetResizable(True)
        self.scrollAreaLabellist.setObjectName("scrollAreaLabellist")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 251, 451))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaLabellist.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollAreaLabellist)
        self.tabWidgetResult.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listWidgetResults = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetResults.setSelectionRectVisible(False)
        self.listWidgetResults.setObjectName("listWidgetResults")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidgetResults.addItem(item)
        self.verticalLayout_6.addWidget(self.listWidgetResults)
        self.btnCopyAll = QtWidgets.QPushButton(self.tab_2)
        self.btnCopyAll.setObjectName("btnCopyAll")
        self.verticalLayout_6.addWidget(self.btnCopyAll)
        self.btnSaveAll = QtWidgets.QPushButton(self.tab_2)
        self.btnSaveAll.setObjectName("btnSaveAll")
        self.verticalLayout_6.addWidget(self.btnSaveAll)
        self.tabWidgetResult.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidgetResult)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidgetResult.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "demo"))
        self.groupBox.setTitle(_translate("MainWindow", "任务配置"))
        self.label_3.setText(_translate("MainWindow", "1. 选择语言模型："))
        self.comboBoxLanguage.setCurrentText(_translate("MainWindow", "ch"))
        self.comboBoxLanguage.setItemText(0, _translate("MainWindow", "ch"))
        self.comboBoxLanguage.setItemText(1, _translate("MainWindow", "en"))
        self.comboBoxLanguage.setItemText(2, _translate("MainWindow", "fr"))
        self.comboBoxLanguage.setItemText(3, _translate("MainWindow", "german"))
        self.comboBoxLanguage.setItemText(4, _translate("MainWindow", "korean"))
        self.comboBoxLanguage.setItemText(5, _translate("MainWindow", "japan"))
        self.label_2.setText(_translate("MainWindow", "2. 功能选型："))
        self.checkBox_ocr.setText(_translate("MainWindow", "文本检测+识别"))
        # self.checkBox_det.setText(_translate("MainWindow", "文本检测"))
        # self.checkBox_recog.setText(_translate("MainWindow", "文本识别"))
        # self.checkBox_layoutparser.setText(_translate("MainWindow", "版面分析"))
        self.btnStartProcess.setText(_translate("MainWindow", "开始"))
        self.btnOpenImg.setText(_translate("MainWindow", "打开图片"))
        self.btnOpenDir.setText(_translate("MainWindow", "打开文件夹"))
        # self.btnEditShape.setText(_translate("MainWindow", "编辑区域"))
        # self.btnAddShape.setText(_translate("MainWindow", "添加区域"))
        self.btnNext.setText(_translate("MainWindow", "下一个"))
        self.btnPrev.setText(_translate("MainWindow", "上一个"))
        # self.btnBrightness.setText(_translate("MainWindow", "调节亮度"))
        self.label.setText(_translate("MainWindow", "识别结果"))
        self.tabWidgetResult.setTabText(self.tabWidgetResult.indexOf(self.tab), _translate("MainWindow", "区域"))
        __sortingEnabled = self.listWidgetResults.isSortingEnabled()
        self.listWidgetResults.setSortingEnabled(False)
        item = self.listWidgetResults.item(0)
        item.setText(_translate("MainWindow", "测试1"))
        self.listWidgetResults.setSortingEnabled(__sortingEnabled)
        self.btnCopyAll.setText(_translate("MainWindow", "复制到剪贴板"))
        self.btnSaveAll.setText(_translate("MainWindow", "保存"))
        self.tabWidgetResult.setTabText(self.tabWidgetResult.indexOf(self.tab_2), _translate("MainWindow", "文本"))
