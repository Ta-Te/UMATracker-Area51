# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window_base.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(813, 500)
        MainWindowBase.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsBox.sizePolicy().hasHeightForWidth())
        self.graphicsBox.setSizePolicy(sizePolicy)
        self.graphicsBox.setObjectName("graphicsBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.graphicsBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputGraphicsView = QtWidgets.QGraphicsView(self.graphicsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.inputGraphicsView.sizePolicy().hasHeightForWidth())
        self.inputGraphicsView.setSizePolicy(sizePolicy)
        self.inputGraphicsView.setAcceptDrops(False)
        self.inputGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.inputGraphicsView.setObjectName("inputGraphicsView")
        self.verticalLayout_2.addWidget(self.inputGraphicsView)
        self.videoPlaybackWidget = VideoPlaybackWidget(self.graphicsBox)
        self.videoPlaybackWidget.setObjectName("videoPlaybackWidget")
        self.verticalLayout_2.addWidget(self.videoPlaybackWidget)
        self.horizontalLayout.addWidget(self.graphicsBox)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.regionTableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.regionTableWidget.setObjectName("regionTableWidget")
        self.regionTableWidget.setColumnCount(0)
        self.regionTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.regionTableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addRegionButton = QtWidgets.QToolButton(self.groupBox)
        self.addRegionButton.setObjectName("addRegionButton")
        self.horizontalLayout_2.addWidget(self.addRegionButton)
        self.removeRegionButton = QtWidgets.QToolButton(self.groupBox)
        self.removeRegionButton.setObjectName("removeRegionButton")
        self.horizontalLayout_2.addWidget(self.removeRegionButton)
        self.upRegionButton = QtWidgets.QToolButton(self.groupBox)
        self.upRegionButton.setText("")
        self.upRegionButton.setObjectName("upRegionButton")
        self.horizontalLayout_2.addWidget(self.upRegionButton)
        self.downRegionButton = QtWidgets.QToolButton(self.groupBox)
        self.downRegionButton.setText("")
        self.downRegionButton.setObjectName("downRegionButton")
        self.horizontalLayout_2.addWidget(self.downRegionButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.radiusSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.radiusSpinBox.setMinimum(1.0)
        self.radiusSpinBox.setMaximum(1000.0)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.horizontalLayout_3.addWidget(self.radiusSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)
        self.actionOpenVideo = QtWidgets.QAction(MainWindowBase)
        self.actionOpenVideo.setObjectName("actionOpenVideo")
        self.actionOpenImage = QtWidgets.QAction(MainWindowBase)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionOpenBlockData = QtWidgets.QAction(MainWindowBase)
        self.actionOpenBlockData.setObjectName("actionOpenBlockData")
        self.actionSaveBlockData = QtWidgets.QAction(MainWindowBase)
        self.actionSaveBlockData.setObjectName("actionSaveBlockData")
        self.actionQuit = QtWidgets.QAction(MainWindowBase)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSaveFilterData = QtWidgets.QAction(MainWindowBase)
        self.actionSaveFilterData.setObjectName("actionSaveFilterData")
        self.actionOpenCSVFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenCSVFile.setObjectName("actionOpenCSVFile")
        self.actionCreateBackground = QtWidgets.QAction(MainWindowBase)
        self.actionCreateBackground.setObjectName("actionCreateBackground")
        self.actionEnable_Disable = QtWidgets.QAction(MainWindowBase)
        self.actionEnable_Disable.setObjectName("actionEnable_Disable")
        self.actionCalculate = QtWidgets.QAction(MainWindowBase)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actionSaveCSVFile = QtWidgets.QAction(MainWindowBase)
        self.actionSaveCSVFile.setObjectName("actionSaveCSVFile")
        self.actionTrackingPathColor = QtWidgets.QAction(MainWindowBase)
        self.actionTrackingPathColor.setObjectName("actionTrackingPathColor")
        self.actionCoordinates = QtWidgets.QAction(MainWindowBase)
        self.actionCoordinates.setCheckable(True)
        self.actionCoordinates.setChecked(True)
        self.actionCoordinates.setObjectName("actionCoordinates")
        self.actionPoints = QtWidgets.QAction(MainWindowBase)
        self.actionPoints.setCheckable(True)
        self.actionPoints.setChecked(True)
        self.actionPoints.setObjectName("actionPoints")
        self.actionRegions = QtWidgets.QAction(MainWindowBase)
        self.actionRegions.setCheckable(True)
        self.actionRegions.setChecked(True)
        self.actionRegions.setObjectName("actionRegions")
        self.actionLines = QtWidgets.QAction(MainWindowBase)
        self.actionLines.setCheckable(True)
        self.actionLines.setChecked(True)
        self.actionLines.setObjectName("actionLines")
        self.actionSaveArea51ObjectsFile = QtWidgets.QAction(MainWindowBase)
        self.actionSaveArea51ObjectsFile.setObjectName("actionSaveArea51ObjectsFile")
        self.actionOpenArea51ObjectsFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenArea51ObjectsFile.setObjectName("actionOpenArea51ObjectsFile")
        self.menuFiles.addAction(self.actionOpenVideo)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionOpenCSVFile)
        self.menuFiles.addAction(self.actionSaveCSVFile)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionOpenArea51ObjectsFile)
        self.menuFiles.addAction(self.actionSaveArea51ObjectsFile)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionCalculate)
        self.menuSettings.addAction(self.actionTrackingPathColor)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCoordinates)
        self.menuSettings.addAction(self.actionPoints)
        self.menuSettings.addAction(self.actionLines)
        self.menuSettings.addAction(self.actionRegions)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindowBase)
        self.actionQuit.triggered.connect(MainWindowBase.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
        self.graphicsBox.setTitle(_translate("MainWindowBase", "Video"))
        self.groupBox.setTitle(_translate("MainWindowBase", "Settings"))
        self.label_2.setText(_translate("MainWindowBase", "Objects:"))
        self.addRegionButton.setText(_translate("MainWindowBase", "+"))
        self.removeRegionButton.setText(_translate("MainWindowBase", "-"))
        self.label.setText(_translate("MainWindowBase", "Radius"))
        self.menuFiles.setTitle(_translate("MainWindowBase", "Files"))
        self.menuRun.setTitle(_translate("MainWindowBase", "Run"))
        self.menuSettings.setTitle(_translate("MainWindowBase", "View"))
        self.actionOpenVideo.setText(_translate("MainWindowBase", "Open Video"))
        self.actionOpenImage.setText(_translate("MainWindowBase", "Open Image"))
        self.actionOpenBlockData.setText(_translate("MainWindowBase", "Open Block Data"))
        self.actionSaveBlockData.setText(_translate("MainWindowBase", "Save Block Data"))
        self.actionQuit.setText(_translate("MainWindowBase", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindowBase", "Ctrl+Q"))
        self.actionSaveFilterData.setText(_translate("MainWindowBase", "Save Filter Data"))
        self.actionOpenCSVFile.setText(_translate("MainWindowBase", "Open Data"))
        self.actionCreateBackground.setText(_translate("MainWindowBase", "Create"))
        self.actionEnable_Disable.setText(_translate("MainWindowBase", "Enable/Disable"))
        self.actionCalculate.setText(_translate("MainWindowBase", "Calculate"))
        self.actionSaveCSVFile.setText(_translate("MainWindowBase", "Save Data"))
        self.actionTrackingPathColor.setText(_translate("MainWindowBase", "Tracking Path Color"))
        self.actionCoordinates.setText(_translate("MainWindowBase", "Coordinates"))
        self.actionPoints.setText(_translate("MainWindowBase", "Points"))
        self.actionRegions.setText(_translate("MainWindowBase", "Regions"))
        self.actionLines.setText(_translate("MainWindowBase", "Lines"))
        self.actionSaveArea51ObjectsFile.setText(_translate("MainWindowBase", "Save Area51 Objects File"))
        self.actionOpenArea51ObjectsFile.setText(_translate("MainWindowBase", "Open Area51 Objects File"))

from .video_playback_widget import VideoPlaybackWidget
