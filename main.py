#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.6
#|*****************************************************
# # -*- coding: utf-8 -*-

from src.utils import constants
from src.main_src import MainSrc
from PyQt5 import QtCore, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(670, 550)
        Main.setMinimumSize(QtCore.QSize(670, 550))
        Main.setMaximumSize(QtCore.QSize(670, 550))
        Main.setSizeIncrement(QtCore.QSize(670, 550))
        Main.setBaseSize(QtCore.QSize(670, 550))
        self.gw2Path_label = QtWidgets.QLabel(Main)
        self.gw2Path_label.setGeometry(QtCore.QRect(180, 10, 461, 29))
        self.gw2Path_label.setText("")
        self.gw2Path_label.setObjectName("gw2Path_label")
        self.findGw2File_button = QtWidgets.QPushButton(Main)
        self.findGw2File_button.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.findGw2File_button.setObjectName("findGw2File_button")
        self.startGw2_button = QtWidgets.QPushButton(Main)
        self.startGw2_button.setGeometry(QtCore.QRect(20, 470, 131, 71))
        self.startGw2_button.setObjectName("startGw2_button")
        self.main_tabWidget = QtWidgets.QTabWidget(Main)
        self.main_tabWidget.setGeometry(QtCore.QRect(20, 50, 631, 411))
        self.main_tabWidget.setUsesScrollButtons(False)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.parameters1_tab = QtWidgets.QWidget()
        self.parameters1_tab.setObjectName("parameters1_tab")
        self.port_groupBox = QtWidgets.QGroupBox(self.parameters1_tab)
        self.port_groupBox.setGeometry(QtCore.QRect(540, 0, 81, 91))
        self.port_groupBox.setObjectName("port_groupBox")
        self.port80_radioButton = QtWidgets.QRadioButton(self.port_groupBox)
        self.port80_radioButton.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.port80_radioButton.setObjectName("port80_radioButton")
        self.port443_radioButton = QtWidgets.QRadioButton(self.port_groupBox)
        self.port443_radioButton.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.port443_radioButton.setObjectName("port443_radioButton")
        self.port6112_radioButton = QtWidgets.QRadioButton(self.port_groupBox)
        self.port6112_radioButton.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.port6112_radioButton.setObjectName("port6112_radioButton")
        self.bit32_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.bit32_checkBox.setGeometry(QtCore.QRect(10, 330, 301, 20))
        self.bit32_checkBox.setObjectName("bit32_checkBox")
        self.autologin_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.autologin_checkBox.setGeometry(QtCore.QRect(10, 10, 181, 20))
        self.autologin_checkBox.setObjectName("autologin_checkBox")
        self.mapLoadinfo_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.mapLoadinfo_checkBox.setGeometry(QtCore.QRect(10, 70, 411, 20))
        self.mapLoadinfo_checkBox.setObjectName("mapLoadinfo_checkBox")
        self.mce_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.mce_checkBox.setGeometry(QtCore.QRect(10, 90, 421, 20))
        self.mce_checkBox.setObjectName("mce_checkBox")
        self.dx9single_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.dx9single_checkBox.setGeometry(QtCore.QRect(10, 110, 451, 20))
        self.dx9single_checkBox.setObjectName("dx9single_checkBox")
        self.forwardrenderer_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.forwardrenderer_checkBox.setGeometry(QtCore.QRect(10, 130, 481, 20))
        self.forwardrenderer_checkBox.setObjectName("forwardrenderer_checkBox")
        self.log_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.log_checkBox.setGeometry(QtCore.QRect(10, 150, 411, 20))
        self.log_checkBox.setObjectName("log_checkBox")
        self.nodelta_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.nodelta_checkBox.setGeometry(QtCore.QRect(10, 170, 391, 20))
        self.nodelta_checkBox.setObjectName("nodelta_checkBox")
        self.nomusic_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.nomusic_checkBox.setGeometry(QtCore.QRect(10, 190, 331, 20))
        self.nomusic_checkBox.setObjectName("nomusic_checkBox")
        self.noui_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.noui_checkBox.setGeometry(QtCore.QRect(10, 210, 481, 20))
        self.noui_checkBox.setObjectName("noui_checkBox")
        self.nosound_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.nosound_checkBox.setGeometry(QtCore.QRect(10, 230, 311, 20))
        self.nosound_checkBox.setObjectName("nosound_checkBox")
        self.prefreset_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.prefreset_checkBox.setGeometry(QtCore.QRect(10, 250, 241, 20))
        self.prefreset_checkBox.setObjectName("prefreset_checkBox")
        self.shareArchive_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.shareArchive_checkBox.setGeometry(QtCore.QRect(10, 270, 551, 20))
        self.shareArchive_checkBox.setObjectName("shareArchive_checkBox")
        self.uispanallmonitors_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.uispanallmonitors_checkBox.setGeometry(QtCore.QRect(10, 290, 551, 20))
        self.uispanallmonitors_checkBox.setObjectName("uispanallmonitors_checkBox")
        self.useOldFov_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.useOldFov_checkBox.setGeometry(QtCore.QRect(10, 310, 321, 20))
        self.useOldFov_checkBox.setObjectName("useOldFov_checkBox")
        self.windowed_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.windowed_checkBox.setGeometry(QtCore.QRect(10, 50, 391, 20))
        self.windowed_checkBox.setObjectName("windowed_checkBox")
        self.umbra_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.umbra_checkBox.setGeometry(QtCore.QRect(10, 350, 421, 20))
        self.umbra_checkBox.setObjectName("umbra_checkBox")
        self.bmp_checkBox = QtWidgets.QCheckBox(self.parameters1_tab)
        self.bmp_checkBox.setGeometry(QtCore.QRect(10, 30, 441, 20))
        self.bmp_checkBox.setObjectName("bmp_checkBox")
        self.main_tabWidget.addTab(self.parameters1_tab, "")
        self.parameters2_tab = QtWidgets.QWidget()
        self.parameters2_tab.setObjectName("parameters2_tab")
        self.dat_checkBox = QtWidgets.QCheckBox(self.parameters2_tab)
        self.dat_checkBox.setGeometry(QtCore.QRect(100, 180, 461, 31))
        self.dat_checkBox.setText("")
        self.dat_checkBox.setObjectName("dat_checkBox")
        self.dat_label = QtWidgets.QLabel(self.parameters2_tab)
        self.dat_label.setGeometry(QtCore.QRect(10, 160, 421, 16))
        self.dat_label.setObjectName("dat_label")
        self.daFile_button = QtWidgets.QPushButton(self.parameters2_tab)
        self.daFile_button.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.daFile_button.setObjectName("daFile_button")
        self.authsrv_label = QtWidgets.QLabel(self.parameters2_tab)
        self.authsrv_label.setGeometry(QtCore.QRect(10, 60, 421, 16))
        self.authsrv_label.setObjectName("authsrv_label")
        self.assetsrv_label = QtWidgets.QLabel(self.parameters2_tab)
        self.assetsrv_label.setGeometry(QtCore.QRect(10, 10, 421, 16))
        self.assetsrv_label.setObjectName("assetsrv_label")
        self.diag_checkBox = QtWidgets.QCheckBox(self.parameters2_tab)
        self.diag_checkBox.setGeometry(QtCore.QRect(20, 290, 331, 20))
        self.diag_checkBox.setObjectName("diag_checkBox")
        self.repair_checkBox = QtWidgets.QCheckBox(self.parameters2_tab)
        self.repair_checkBox.setGeometry(QtCore.QRect(20, 270, 391, 20))
        self.repair_checkBox.setObjectName("repair_checkBox")
        self.portal_label = QtWidgets.QLabel(self.parameters2_tab)
        self.portal_label.setGeometry(QtCore.QRect(10, 110, 411, 16))
        self.portal_label.setObjectName("portal_label")
        self.uninstall_checkBox = QtWidgets.QCheckBox(self.parameters2_tab)
        self.uninstall_checkBox.setGeometry(QtCore.QRect(20, 310, 511, 20))
        self.uninstall_checkBox.setObjectName("uninstall_checkBox")
        self.verify_checkBox = QtWidgets.QCheckBox(self.parameters2_tab)
        self.verify_checkBox.setGeometry(QtCore.QRect(20, 250, 211, 20))
        self.verify_checkBox.setObjectName("verify_checkBox")
        self.utilities_groupBox = QtWidgets.QGroupBox(self.parameters2_tab)
        self.utilities_groupBox.setGeometry(QtCore.QRect(10, 220, 581, 141))
        self.utilities_groupBox.setObjectName("utilities_groupBox")
        self.assetsrv_textEdit = QtWidgets.QPlainTextEdit(self.parameters2_tab)
        self.assetsrv_textEdit.setGeometry(QtCore.QRect(10, 30, 120, 20))
        self.assetsrv_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.assetsrv_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.assetsrv_textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.assetsrv_textEdit.setObjectName("assetsrv_textEdit")
        self.authsrv_textEdit = QtWidgets.QPlainTextEdit(self.parameters2_tab)
        self.authsrv_textEdit.setGeometry(QtCore.QRect(10, 80, 120, 20))
        self.authsrv_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.authsrv_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.authsrv_textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.authsrv_textEdit.setObjectName("authsrv_textEdit")
        self.portal_textEdit = QtWidgets.QPlainTextEdit(self.parameters2_tab)
        self.portal_textEdit.setGeometry(QtCore.QRect(10, 130, 120, 20))
        self.portal_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.portal_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.portal_textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.portal_textEdit.setObjectName("portal_textEdit")
        self.dat_checkBox.raise_()
        self.dat_label.raise_()
        self.daFile_button.raise_()
        self.authsrv_label.raise_()
        self.assetsrv_label.raise_()
        self.portal_label.raise_()
        self.utilities_groupBox.raise_()
        self.repair_checkBox.raise_()
        self.diag_checkBox.raise_()
        self.uninstall_checkBox.raise_()
        self.verify_checkBox.raise_()
        self.assetsrv_textEdit.raise_()
        self.authsrv_textEdit.raise_()
        self.portal_textEdit.raise_()
        self.main_tabWidget.addTab(self.parameters2_tab, "")
        self.arcDps_tab = QtWidgets.QWidget()
        self.arcDps_tab.setObjectName("arcDps_tab")
        self.arcdps_groupBox = QtWidgets.QGroupBox(self.arcDps_tab)
        self.arcdps_groupBox.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.arcdps_groupBox.setObjectName("arcdps_groupBox")
        self.arcdps_yes_radioButton = QtWidgets.QRadioButton(self.arcdps_groupBox)
        self.arcdps_yes_radioButton.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.arcdps_yes_radioButton.setObjectName("arcdps_yes_radioButton")
        self.arcdps_no_radioButton = QtWidgets.QRadioButton(self.arcdps_groupBox)
        self.arcdps_no_radioButton.setGeometry(QtCore.QRect(60, 20, 51, 20))
        self.arcdps_no_radioButton.setObjectName("arcdps_no_radioButton")
        self.arcdps_disclamer_label = QtWidgets.QLabel(self.arcDps_tab)
        self.arcdps_disclamer_label.setGeometry(QtCore.QRect(160, 10, 431, 41))
        self.arcdps_disclamer_label.setText("")
        self.arcdps_disclamer_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.arcdps_disclamer_label.setWordWrap(True)
        self.arcdps_disclamer_label.setOpenExternalLinks(True)
        self.arcdps_disclamer_label.setObjectName("arcdps_disclamer_label")
        self.arcdps_current_version_label = QtWidgets.QLabel(self.arcDps_tab)
        self.arcdps_current_version_label.setGeometry(QtCore.QRect(20, 80, 111, 20))
        self.arcdps_current_version_label.setText("")
        self.arcdps_current_version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arcdps_current_version_label.setObjectName("arcdps_current_version_label")
        self.arcdps_latest_version_label = QtWidgets.QLabel(self.arcDps_tab)
        self.arcdps_latest_version_label.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.arcdps_latest_version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arcdps_latest_version_label.setObjectName("arcdps_latest_version_label")
        self.arcdps_webpage_textEdit = QtWidgets.QPlainTextEdit(self.arcDps_tab)
        self.arcdps_webpage_textEdit.setGeometry(QtCore.QRect(10, 110, 601, 261))
        self.arcdps_webpage_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.arcdps_webpage_textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.arcdps_webpage_textEdit.setReadOnly(True)
        self.arcdps_webpage_textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.arcdps_webpage_textEdit.setObjectName("arcdps_webpage_textEdit")
        self.arcps_url_textBrowser = QtWidgets.QTextBrowser(self.arcDps_tab)
        self.arcps_url_textBrowser.setGeometry(QtCore.QRect(240, 60, 241, 21))
        self.arcps_url_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.arcps_url_textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.arcps_url_textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.arcps_url_textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.arcps_url_textBrowser.setOpenExternalLinks(True)
        self.arcps_url_textBrowser.setObjectName("arcps_url_textBrowser")
        self.main_tabWidget.addTab(self.arcDps_tab, "")
        self.about_tab = QtWidgets.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.about_textBrowser = QtWidgets.QTextBrowser(self.about_tab)
        self.about_textBrowser.setGeometry(QtCore.QRect(0, 0, 631, 381))
        self.about_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.about_textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.about_textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.about_textBrowser.setUndoRedoEnabled(False)
        self.about_textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.about_textBrowser.setOpenExternalLinks(True)
        self.about_textBrowser.setObjectName("about_textBrowser")
        self.main_tabWidget.addTab(self.about_tab, "")
        self.currentParam_groupBox = QtWidgets.QGroupBox(Main)
        self.currentParam_groupBox.setGeometry(QtCore.QRect(160, 460, 491, 81))
        self.currentParam_groupBox.setObjectName("currentParam_groupBox")
        self.current_param_label = QtWidgets.QLabel(self.currentParam_groupBox)
        self.current_param_label.setGeometry(QtCore.QRect(10, 20, 471, 51))
        self.current_param_label.setText("")
        self.current_param_label.setTextFormat(QtCore.Qt.AutoText)
        self.current_param_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.current_param_label.setWordWrap(True)
        self.current_param_label.setObjectName("current_param_label")

        self.retranslateUi(Main)
        self.main_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

        mainSrc = MainSrc(self, Main)
        mainSrc.init()
        
    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", constants.FULL_PROGRAM_NAME))
        self.findGw2File_button.setText(_translate("Main", "Find Gw2 Executable"))
        self.startGw2_button.setText(_translate("Main", "Start Gw2"))
        self.port_groupBox.setTitle(_translate("Main", "Port"))
        self.port80_radioButton.setText(_translate("Main", "80"))
        self.port443_radioButton.setText(_translate("Main", "443"))
        self.port6112_radioButton.setText(_translate("Main", "6112"))
        self.bit32_checkBox.setText(_translate("Main", "Force the game to run in 32-bit mode. (-32)"))
        self.autologin_checkBox.setText(_translate("Main", "Autologin. (-autologin)"))
        self.mapLoadinfo_checkBox.setText(_translate("Main", "Show diagnostic information during map loads. (-mapLoadinfo)"))
        self.mce_checkBox.setText(_translate("Main", "Start the client with Windows Media Center compatibility. (-mce)"))
        self.dx9single_checkBox.setText(_translate("Main", "Enable the Direct3D 9c renderer in single-threaded mode. (-dx9single)"))
        self.forwardrenderer_checkBox.setText(_translate("Main", "Use Forward Rendering instead of Deferred Rendering. (-forwardrenderer)"))
        self.log_checkBox.setText(_translate("Main", "Enable the creation of a log file, used mostly by Support. (-log)"))
        self.nodelta_checkBox.setText(_translate("Main", "Disable delta patching when updating game files. (-nodelta)"))
        self.nomusic_checkBox.setText(_translate("Main", "Disable music and background music. (-nomusic)"))
        self.noui_checkBox.setText(_translate("Main", "Disable the interface. Does the same thing as pressing Ctrl+Shift+H. (-noui)"))
        self.nosound_checkBox.setText(_translate("Main", "Disable audio system completely. (-nosound)"))
        self.prefreset_checkBox.setText(_translate("Main", "Reset game settings. (-prefreset)"))
        self.shareArchive_checkBox.setText(_translate("Main", "Gw2.dat file will be shared and can be accessed from other processes. (-shareArchive)"))
        self.uispanallmonitors_checkBox.setText(_translate("Main", "Spread user interface across all monitors in a triple monitor setup. (-uispanallmonitors)"))
        self.useOldFov_checkBox.setText(_translate("Main", "Restore the original field-of-view. (-useOldFov)"))
        self.windowed_checkBox.setText(_translate("Main", "Force Guild Wars 2 to run in windowed mode. (-windowed)"))
        self.umbra_checkBox.setText(_translate("Main", "Force the use of Umbra\'s GPU accelerated culling. (-umbra gpu)"))
        self.bmp_checkBox.setText(_translate("Main", "Force the game to create lossless screenshots as .BMP files. (-bmp)"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.parameters1_tab), _translate("Main", "Parameters I"))
        self.dat_label.setText(_translate("Main", "Use the specified .dat file instead of the default GW2.dat file. (-dat )"))
        self.daFile_button.setText(_translate("Main", ".dat File"))
        self.authsrv_label.setText(_translate("Main", "IP or DNS that can be used to connect to a login server. (-authsrv)"))
        self.assetsrv_label.setText(_translate("Main", "IP-address or DNS-name to use for downloading assets. (-assetsrv)"))
        self.diag_checkBox.setText(_translate("Main", "Create a diagnostic file (NetworkDiag.log) (-diag)"))
        self.repair_checkBox.setText(_translate("Main", "Check files for errors and repairs them as needed. (-repair)"))
        self.portal_label.setText(_translate("Main", "IP or DNS to use for connecting to a portal/gate server. (-portal)"))
        self.uninstall_checkBox.setText(_translate("Main", "Delete the contents of the Guild Wars 2 folder except GW2.EXE itself. (-uninstall)"))
        self.verify_checkBox.setText(_translate("Main", "Verify the .dat file. (-verify)"))
        self.utilities_groupBox.setTitle(_translate("Main", "Other Utilities"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.parameters2_tab), _translate("Main", "Parameters II"))
        self.arcdps_groupBox.setTitle(_translate("Main", "Use ArcDps"))
        self.arcdps_yes_radioButton.setText(_translate("Main", "YES"))
        self.arcdps_no_radioButton.setText(_translate("Main", "NO"))
        self.arcdps_latest_version_label.setText(_translate("Main", "Latest Version"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.arcDps_tab), _translate("Main", "ArcDps"))
        self.about_textBrowser.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Guild Wars 2 Utilities</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Implemented using Python3 and QT5.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Developed as an open source project and hosted on GitHub.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">More info about Guild Wars 2 command line arguments on wiki:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://wiki.guildwars2.com/wiki/Command_line_arguments/\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Gw2 Wiki</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Acknowledgements:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.deltaconnected.com/arcdps\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Arcdps</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pypi.org/project/beautifulsoup4\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Beautifulsoup4</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.guildwars2.com\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Guild Wars 2</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pyinstaller.readthedocs.io/en/stable/installation.html\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">PyInstaller</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.python.org/downloads\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Python3</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.qt.io\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">QT5</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Developed by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Discord: Hadesz#1223</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Gw2 ID: Hadesz.7508</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:hadesz456@gmail.com\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Email</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Hadesz1/Gw2Utils/releases/latest\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Download</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=CTYZ8TK5MJV76\"><span style=\" font-size:9pt; text-decoration: underline; color:#8b0000;\">Donations</span></a></p></body></html>"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.about_tab), _translate("Main", "About"))
        self.currentParam_groupBox.setTitle(_translate("Main", "Current Parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

