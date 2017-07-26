# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch-iv-analysis.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_batch_iv_analysis(object):
    def setupUi(self, batch_iv_analysis):
        batch_iv_analysis.setObjectName("batch_iv_analysis")
        batch_iv_analysis.resize(783, 641)
        self.centralwidget = QtWidgets.QWidget(batch_iv_analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tehTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tehTabs.setObjectName("tehTabs")
        self.resultsTabs = QtWidgets.QWidget()
        self.resultsTabs.setObjectName("resultsTabs")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.resultsTabs)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.resultsTabs)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(92)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tehTabs.addTab(self.resultsTabs, "")
        self.plotTab = QtWidgets.QWidget()
        self.plotTab.setObjectName("plotTab")
        self.tehTabs.addTab(self.plotTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.settingsTab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.attemptCharEqnFitLabel = QtWidgets.QLabel(self.settingsTab)
        self.attemptCharEqnFitLabel.setObjectName("attemptCharEqnFitLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.attemptCharEqnFitLabel)
        self.attemptCharEqnFitCheckBox = QtWidgets.QCheckBox(self.settingsTab)
        self.attemptCharEqnFitCheckBox.setChecked(True)
        self.attemptCharEqnFitCheckBox.setObjectName("attemptCharEqnFitCheckBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.attemptCharEqnFitCheckBox)
        self.doFastAndSloppyMathLabel = QtWidgets.QLabel(self.settingsTab)
        self.doFastAndSloppyMathLabel.setObjectName("doFastAndSloppyMathLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.doFastAndSloppyMathLabel)
        self.doFastAndSloppyMathCheckBox = QtWidgets.QCheckBox(self.settingsTab)
        self.doFastAndSloppyMathCheckBox.setObjectName("doFastAndSloppyMathCheckBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doFastAndSloppyMathCheckBox)
        self.lowerVoltageCutoffLabel = QtWidgets.QLabel(self.settingsTab)
        self.lowerVoltageCutoffLabel.setObjectName("lowerVoltageCutoffLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lowerVoltageCutoffLabel)
        self.lowerVoltageCutoffLineEdit = QtWidgets.QLineEdit(self.settingsTab)
        self.lowerVoltageCutoffLineEdit.setObjectName("lowerVoltageCutoffLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lowerVoltageCutoffLineEdit)
        self.upperVoltageCutoffLabel = QtWidgets.QLabel(self.settingsTab)
        self.upperVoltageCutoffLabel.setObjectName("upperVoltageCutoffLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.upperVoltageCutoffLabel)
        self.upperVoltageCutoffLineEdit = QtWidgets.QLineEdit(self.settingsTab)
        self.upperVoltageCutoffLineEdit.setObjectName("upperVoltageCutoffLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.upperVoltageCutoffLineEdit)
        self.fitMethodLabel = QtWidgets.QLabel(self.settingsTab)
        self.fitMethodLabel.setObjectName("fitMethodLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fitMethodLabel)
        self.fitMethodComboBox = QtWidgets.QComboBox(self.settingsTab)
        self.fitMethodComboBox.setObjectName("fitMethodComboBox")
        self.fitMethodComboBox.addItem("")
        self.fitMethodComboBox.addItem("")
        self.fitMethodComboBox.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fitMethodComboBox)
        self.verbosityLabel = QtWidgets.QLabel(self.settingsTab)
        self.verbosityLabel.setObjectName("verbosityLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.verbosityLabel)
        self.verbositySpinBox = QtWidgets.QSpinBox(self.settingsTab)
        self.verbositySpinBox.setMaximum(2)
        self.verbositySpinBox.setObjectName("verbositySpinBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.verbositySpinBox)
        self.analysisThreadsLabel = QtWidgets.QLabel(self.settingsTab)
        self.analysisThreadsLabel.setObjectName("analysisThreadsLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.analysisThreadsLabel)
        self.analysisThreadsSpinBox = QtWidgets.QSpinBox(self.settingsTab)
        self.analysisThreadsSpinBox.setMinimum(1)
        self.analysisThreadsSpinBox.setProperty("value", 1)
        self.analysisThreadsSpinBox.setObjectName("analysisThreadsSpinBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.analysisThreadsSpinBox)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.resetSettingsButton = QtWidgets.QPushButton(self.settingsTab)
        self.resetSettingsButton.setObjectName("resetSettingsButton")
        self.verticalLayout_4.addWidget(self.resetSettingsButton, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.tehTabs.addTab(self.settingsTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Rsh_ub = QtWidgets.QLineEdit(self.tab)
        self.Rsh_ub.setGeometry(QtCore.QRect(250, 190, 113, 32))
        self.Rsh_ub.setObjectName("Rsh_ub")
        self.Rsh_lb = QtWidgets.QLineEdit(self.tab)
        self.Rsh_lb.setGeometry(QtCore.QRect(120, 190, 113, 32))
        self.Rsh_lb.setObjectName("Rsh_lb")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 61, 20))
        self.label_3.setObjectName("label_3")
        self.I0_lb = QtWidgets.QLineEdit(self.tab)
        self.I0_lb.setGeometry(QtCore.QRect(120, 40, 113, 32))
        self.I0_lb.setObjectName("I0_lb")
        self.n_ub = QtWidgets.QLineEdit(self.tab)
        self.n_ub.setGeometry(QtCore.QRect(250, 240, 113, 32))
        self.n_ub.setObjectName("n_ub")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(290, 10, 41, 20))
        self.label.setObjectName("label")
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(20, 220, 351, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 41, 20))
        self.label_2.setObjectName("label_2")
        self.n_lb = QtWidgets.QLineEdit(self.tab)
        self.n_lb.setGeometry(QtCore.QRect(120, 240, 113, 32))
        self.n_lb.setObjectName("n_lb")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 81, 20))
        self.label_7.setObjectName("label_7")
        self.I0_ub = QtWidgets.QLineEdit(self.tab)
        self.I0_ub.setGeometry(QtCore.QRect(250, 40, 113, 32))
        self.I0_ub.setObjectName("I0_ub")
        self.Rs_lb = QtWidgets.QLineEdit(self.tab)
        self.Rs_lb.setGeometry(QtCore.QRect(120, 140, 113, 32))
        self.Rs_lb.setObjectName("Rs_lb")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(20, 120, 351, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(20, 70, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Rs_ub = QtWidgets.QLineEdit(self.tab)
        self.Rs_ub.setGeometry(QtCore.QRect(250, 140, 113, 32))
        self.Rs_ub.setObjectName("Rs_ub")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(120, 20, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(233, 20, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 71, 20))
        self.label_5.setObjectName("label_5")
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(20, 170, 351, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Iph_ub = QtWidgets.QLineEdit(self.tab)
        self.Iph_ub.setGeometry(QtCore.QRect(250, 90, 113, 32))
        self.Iph_ub.setObjectName("Iph_ub")
        self.Iph_lb = QtWidgets.QLineEdit(self.tab)
        self.Iph_lb.setGeometry(QtCore.QRect(120, 90, 113, 32))
        self.Iph_lb.setObjectName("Iph_lb")
        self.tehTabs.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tehTabs, 1, 0, 1, 1)
        batch_iv_analysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(batch_iv_analysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        batch_iv_analysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(batch_iv_analysis)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        batch_iv_analysis.setStatusBar(self.statusbar)
        self.tehDock = QtWidgets.QDockWidget(batch_iv_analysis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tehDock.sizePolicy().hasHeightForWidth())
        self.tehDock.setSizePolicy(sizePolicy)
        self.tehDock.setMinimumSize(QtCore.QSize(93, 118))
        self.tehDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.tehDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.tehDock.setObjectName("tehDock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.eventLog = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.eventLog.setObjectName("eventLog")
        self.gridLayout_2.addWidget(self.eventLog, 0, 0, 1, 1)
        self.tehDock.setWidget(self.dockWidgetContents)
        batch_iv_analysis.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.tehDock)
        self.actionQuit = QtWidgets.QAction(batch_iv_analysis)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen = QtWidgets.QAction(batch_iv_analysis)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(batch_iv_analysis)
        self.actionSave.setObjectName("actionSave")
        self.actionClear_Table = QtWidgets.QAction(batch_iv_analysis)
        self.actionClear_Table.setEnabled(True)
        self.actionClear_Table.setObjectName("actionClear_Table")
        self.actionFsadf = QtWidgets.QAction(batch_iv_analysis)
        self.actionFsadf.setObjectName("actionFsadf")
        self.actionSet_Bounds = QtWidgets.QAction(batch_iv_analysis)
        self.actionSet_Bounds.setObjectName("actionSet_Bounds")
        self.actionWatch = QtWidgets.QAction(batch_iv_analysis)
        self.actionWatch.setObjectName("actionWatch")
        self.actionEnable_Watching = QtWidgets.QAction(batch_iv_analysis)
        self.actionEnable_Watching.setCheckable(True)
        self.actionEnable_Watching.setChecked(False)
        self.actionEnable_Watching.setObjectName("actionEnable_Watching")
        self.actionWatch_2 = QtWidgets.QAction(batch_iv_analysis)
        self.actionWatch_2.setObjectName("actionWatch_2")
        self.actionFit_Constraints = QtWidgets.QAction(batch_iv_analysis)
        self.actionFit_Constraints.setObjectName("actionFit_Constraints")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionWatch_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionClear_Table)
        self.menuTools.addAction(self.actionEnable_Watching)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(batch_iv_analysis)
        self.tehTabs.setCurrentIndex(0)
        self.fitMethodComboBox.setCurrentIndex(2)
        self.actionQuit.triggered.connect(batch_iv_analysis.close)
        QtCore.QMetaObject.connectSlotsByName(batch_iv_analysis)

    def retranslateUi(self, batch_iv_analysis):
        _translate = QtCore.QCoreApplication.translate
        batch_iv_analysis.setWindowTitle(_translate("batch_iv_analysis", "batch-iv-analysis"))
        self.tableWidget.setSortingEnabled(True)
        self.tehTabs.setTabText(self.tehTabs.indexOf(self.resultsTabs), _translate("batch_iv_analysis", "Results"))
        self.tehTabs.setTabText(self.tehTabs.indexOf(self.plotTab), _translate("batch_iv_analysis", "Plots"))
        self.attemptCharEqnFitLabel.setText(_translate("batch_iv_analysis", "Attempt Char. Eqn. Fit"))
        self.doFastAndSloppyMathLabel.setText(_translate("batch_iv_analysis", "Do Fast and Sloppy Math"))
        self.lowerVoltageCutoffLabel.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Any data points below this voltage will be ignored</p></body></html>"))
        self.lowerVoltageCutoffLabel.setText(_translate("batch_iv_analysis", "Lower Voltage Cutoff"))
        self.lowerVoltageCutoffLineEdit.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Any data points below this voltage will be ignored</p></body></html>"))
        self.lowerVoltageCutoffLineEdit.setText(_translate("batch_iv_analysis", "-inf"))
        self.upperVoltageCutoffLabel.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Any data points above this voltage will be ignored</p></body></html>"))
        self.upperVoltageCutoffLabel.setText(_translate("batch_iv_analysis", "Upper Voltage Cutoff"))
        self.upperVoltageCutoffLineEdit.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Any data points above this voltage will be ignored</p></body></html>"))
        self.upperVoltageCutoffLineEdit.setText(_translate("batch_iv_analysis", "inf"))
        self.fitMethodLabel.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Fit method to use in scipy.optimize.least_squares routine</p></body></html>"))
        self.fitMethodLabel.setText(_translate("batch_iv_analysis", "Fit Method"))
        self.fitMethodComboBox.setToolTip(_translate("batch_iv_analysis", "<html><head/><body><p>Fit method to use in scipy.optimize.least_squares routine</p></body></html>"))
        self.fitMethodComboBox.setItemText(0, _translate("batch_iv_analysis", "Trust Region Reflective"))
        self.fitMethodComboBox.setItemText(1, _translate("batch_iv_analysis", "dogleg"))
        self.fitMethodComboBox.setItemText(2, _translate("batch_iv_analysis", "Levenberg-Marquardt"))
        self.verbosityLabel.setText(_translate("batch_iv_analysis", "Verbosity"))
        self.analysisThreadsLabel.setText(_translate("batch_iv_analysis", "Analysis Threads"))
        self.resetSettingsButton.setText(_translate("batch_iv_analysis", "Reset Defaults"))
        self.tehTabs.setTabText(self.tehTabs.indexOf(self.settingsTab), _translate("batch_iv_analysis", "Settings"))
        self.Rsh_ub.setText(_translate("batch_iv_analysis", "inf"))
        self.Rsh_lb.setText(_translate("batch_iv_analysis", "0"))
        self.label_3.setText(_translate("batch_iv_analysis", "I_0 [A]"))
        self.I0_lb.setText(_translate("batch_iv_analysis", "0"))
        self.n_ub.setText(_translate("batch_iv_analysis", "inf"))
        self.label_6.setText(_translate("batch_iv_analysis", "R_sh [ohm]"))
        self.label.setText(_translate("batch_iv_analysis", "Upper"))
        self.label_2.setText(_translate("batch_iv_analysis", "Lower"))
        self.n_lb.setText(_translate("batch_iv_analysis", "0"))
        self.label_7.setText(_translate("batch_iv_analysis", "n"))
        self.I0_ub.setText(_translate("batch_iv_analysis", "inf"))
        self.Rs_lb.setText(_translate("batch_iv_analysis", "0"))
        self.Rs_ub.setText(_translate("batch_iv_analysis", "inf"))
        self.label_4.setText(_translate("batch_iv_analysis", "I_Ph [A]"))
        self.label_5.setText(_translate("batch_iv_analysis", "R_s [ohm]"))
        self.Iph_ub.setText(_translate("batch_iv_analysis", "inf"))
        self.Iph_lb.setText(_translate("batch_iv_analysis", "0"))
        self.tehTabs.setTabText(self.tehTabs.indexOf(self.tab), _translate("batch_iv_analysis", "Constraints"))
        self.menuFile.setTitle(_translate("batch_iv_analysis", "File"))
        self.menuTools.setTitle(_translate("batch_iv_analysis", "Tools"))
        self.tehDock.setWindowTitle(_translate("batch_iv_analysis", "Event Log"))
        self.actionQuit.setText(_translate("batch_iv_analysis", "Quit"))
        self.actionQuit.setShortcut(_translate("batch_iv_analysis", "Ctrl+Q"))
        self.actionOpen.setText(_translate("batch_iv_analysis", "Open"))
        self.actionOpen.setShortcut(_translate("batch_iv_analysis", "Ctrl+O"))
        self.actionSave.setText(_translate("batch_iv_analysis", "Export"))
        self.actionSave.setShortcut(_translate("batch_iv_analysis", "Ctrl+S"))
        self.actionClear_Table.setText(_translate("batch_iv_analysis", "Clear Table"))
        self.actionClear_Table.setShortcut(_translate("batch_iv_analysis", "Ctrl+Backspace"))
        self.actionFsadf.setText(_translate("batch_iv_analysis", "fsadf"))
        self.actionSet_Bounds.setText(_translate("batch_iv_analysis", "Set Bounds"))
        self.actionWatch.setText(_translate("batch_iv_analysis", "Watch"))
        self.actionWatch.setShortcut(_translate("batch_iv_analysis", "Ctrl+W"))
        self.actionEnable_Watching.setText(_translate("batch_iv_analysis", "Enable Watching"))
        self.actionEnable_Watching.setShortcut(_translate("batch_iv_analysis", "Ctrl+E"))
        self.actionWatch_2.setText(_translate("batch_iv_analysis", "Watch"))
        self.actionWatch_2.setShortcut(_translate("batch_iv_analysis", "Ctrl+W"))
        self.actionFit_Constraints.setText(_translate("batch_iv_analysis", "Fit Constraints"))

