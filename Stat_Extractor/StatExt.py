# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatExt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statExtract(object):
    def setupUi(self, statExtract):
        statExtract.setObjectName("statExtract")
        statExtract.resize(508, 351)
        statExtract.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(statExtract)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("NHL \'94")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.titleLayout.addWidget(self.title)
        self.verticalLayout_2.addLayout(self.titleLayout)
        self.romLayout = QtWidgets.QHBoxLayout()
        self.romLayout.setObjectName("romLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.romLayout.addItem(spacerItem)
        self.romBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.romBtn.setFont(font)
        self.romBtn.setObjectName("romBtn")
        self.romLayout.addWidget(self.romBtn)
        self.romLabel = QtWidgets.QLabel(self.centralwidget)
        self.romLabel.setObjectName("romLabel")
        self.romLayout.addWidget(self.romLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.romLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.romLayout)
        self.perLayout = QtWidgets.QHBoxLayout()
        self.perLayout.setObjectName("perLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.perLayout.addItem(spacerItem2)
        self.perLabel = QtWidgets.QLabel(self.centralwidget)
        self.perLabel.setObjectName("perLabel")
        self.perLayout.addWidget(self.perLabel)
        self.perLength = QtWidgets.QSpinBox(self.centralwidget)
        self.perLength.setSuffix("")
        self.perLength.setMinimum(1)
        self.perLength.setMaximum(60)
        self.perLength.setProperty("value", 5)
        self.perLength.setObjectName("perLength")
        self.perLayout.addWidget(self.perLength)
        self.tmLabel = QtWidgets.QLabel(self.centralwidget)
        self.tmLabel.setObjectName("tmLabel")
        self.perLayout.addWidget(self.tmLabel)
        self.numTeams = QtWidgets.QSpinBox(self.centralwidget)
        self.numTeams.setMaximum(32)
        self.numTeams.setProperty("value", 28)
        self.numTeams.setObjectName("numTeams")
        self.perLayout.addWidget(self.numTeams)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.perLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.perLayout)
        self.stateLayout = QtWidgets.QHBoxLayout()
        self.stateLayout.setObjectName("stateLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stateLayout.addItem(spacerItem4)
        self.stateBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stateBtn.setFont(font)
        self.stateBtn.setObjectName("stateBtn")
        self.stateLayout.addWidget(self.stateBtn)
        self.stateLabel = QtWidgets.QLabel(self.centralwidget)
        self.stateLabel.setObjectName("stateLabel")
        self.stateLayout.addWidget(self.stateLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stateLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.stateLayout)
        self.stateTypeLayout = QtWidgets.QHBoxLayout()
        self.stateTypeLayout.setObjectName("stateTypeLayout")
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stateTypeLayout.addItem(spacerItem6)
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setObjectName("typeLabel")
        self.stateTypeLayout.addWidget(self.typeLabel)
        self.typeGPGX = QtWidgets.QRadioButton(self.centralwidget)
        self.typeGPGX.setChecked(True)
        self.typeGPGX.setObjectName("typeGPGX")
        self.stateTypeLayout.addWidget(self.typeGPGX)
        self.typeSNES9x = QtWidgets.QRadioButton(self.centralwidget)
        self.typeSNES9x.setObjectName("typeSNES9x")
        self.stateTypeLayout.addWidget(self.typeSNES9x)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stateTypeLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.stateTypeLayout)
        self.extractLayout = QtWidgets.QHBoxLayout()
        self.extractLayout.setObjectName("extractLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.extractLayout.addItem(spacerItem8)
        self.extBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.extBtn.setFont(font)
        self.extBtn.setObjectName("extBtn")
        self.extractLayout.addWidget(self.extBtn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.extractLayout.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.extractLayout)
        statExtract.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(statExtract)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        statExtract.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(statExtract)
        self.statusbar.setObjectName("statusbar")
        statExtract.setStatusBar(self.statusbar)
        self.actionLoad_ROM = QtWidgets.QAction(statExtract)
        self.actionLoad_ROM.setObjectName("actionLoad_ROM")
        self.actionLoad_Save_State = QtWidgets.QAction(statExtract)
        self.actionLoad_Save_State.setObjectName("actionLoad_Save_State")
        self.actionQuit = QtWidgets.QAction(statExtract)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExtract_to_CSV = QtWidgets.QAction(statExtract)
        self.actionExtract_to_CSV.setEnabled(False)
        self.actionExtract_to_CSV.setObjectName("actionExtract_to_CSV")
        self.actionAbout = QtWidgets.QAction(statExtract)
        self.actionAbout.setObjectName("actionAbout")
        self.actionInstructions = QtWidgets.QAction(statExtract)
        self.actionInstructions.setObjectName("actionInstructions")
        self.menuFile.addAction(self.actionLoad_ROM)
        self.menuFile.addAction(self.actionLoad_Save_State)
        self.menuFile.addAction(self.actionExtract_to_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(statExtract)
        QtCore.QMetaObject.connectSlotsByName(statExtract)

    def retranslateUi(self, statExtract):
        _translate = QtCore.QCoreApplication.translate
        statExtract.setWindowTitle(_translate("statExtract", "NHL \'94 Stat Extractor"))
        self.title.setText(_translate("statExtract", "NHL94 Offline Stat Extractor"))
        self.romBtn.setText(_translate("statExtract", "Choose ROM..."))
        self.romLabel.setText(_translate("statExtract", "No ROM Loaded."))
        self.perLabel.setText(_translate("statExtract", "Period Length (min):"))
        self.tmLabel.setText(_translate("statExtract", "# of Teams in ROM: "))
        self.stateBtn.setText(_translate("statExtract", "Choose State..."))
        self.stateLabel.setText(_translate("statExtract", "No State Loaded."))
        self.typeLabel.setText(_translate("statExtract", "State Type:"))
        self.typeGPGX.setText(_translate("statExtract", "RA-GPGX"))
        self.typeSNES9x.setText(_translate("statExtract", "RA-Snes9x"))
        self.extBtn.setText(_translate("statExtract", "Extract to XLS..."))
        self.menuFile.setTitle(_translate("statExtract", "File"))
        self.menuHelp.setTitle(_translate("statExtract", "Help"))
        self.actionLoad_ROM.setText(_translate("statExtract", "Load ROM..."))
        self.actionLoad_Save_State.setText(_translate("statExtract", "Load Save State..."))
        self.actionQuit.setText(_translate("statExtract", "Quit"))
        self.actionExtract_to_CSV.setText(_translate("statExtract", "Extract to XLS..."))
        self.actionAbout.setText(_translate("statExtract", "About..."))
        self.actionInstructions.setText(_translate("statExtract", "Instructions..."))