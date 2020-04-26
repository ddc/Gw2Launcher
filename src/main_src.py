#! /usr/bin/env python3
# |*****************************************************
# * Copyright         : Copyright (C) 2019
# * Author            : ddc
# * License           : GPL v3
# * Python            : 3.6
# |*****************************************************
# # -*- coding: utf-8 -*-

import logging.handlers
import os
import sys
from time import sleep

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QDesktopServices
from bs4 import BeautifulSoup

from src.utils import constants, messages, utilities
from src.utils.create_files import CreateFiles


class MainSrc:
    def __init__(self, qtObj, form):
        self.qtObj = qtObj
        self.form = form
        self.configs = None
        self.new_version_msg = None

    ################################################################################
    def init(self):
        pb = utilities.ProgressBar(messages.initializing, 0)
        self._check_dirs()
        self._setup_logging()
        sys.excepthook = utilities.log_uncaught_exceptions
        self._check_files()
        self.configs = utilities.get_all_ini_file_settings(constants.SETTINGS_FILENAME)
        if self.configs['useTheme'] is None:
            self.configs['useTheme'] = True
        pb.setValue(100)

        pb = utilities.ProgressBar(messages.checking_new_version, 25)
        self._check_new_program_version()
        pb.setValue(100)

        pb = utilities.ProgressBar(messages.arcdps_new_version, 50)
        self._check_arcdps_installed()
        if self.configs['gw2Path'] is not None:
            self._update_arcdps()
        pb.setValue(100)

        pb = utilities.ProgressBar(messages.get_arcdps_html, 75)
        self._set_arcdps_tab()
        pb.setValue(100)

        if self.configs['useTheme']:
            self.form.setStyleSheet(open(constants.STYLE_QSS_FILENAME, "r").read())

        if self.configs['gw2Path'] is None or self.configs['gw2Path'] == "":
            self._disable_form()
            find_gw2_exec_msg = messages.find_gw2_exec
            utilities.show_message_window("info", "INFO", find_gw2_exec_msg)
            self._get_gw2_file_name()
        else:
            self._enable_form()

        self._set_all_configs_on_form_from_settings_file()
        self._register_form_events()
        self.qtObj.main_tabWidget.setCurrentIndex(0)
        self.qtObj.findGw2File_button.setFocus()

    ################################################################################
    def _check_dirs(self):
        if not os.path.exists(constants.PROGRAM_PATH):
            os.makedirs(constants.PROGRAM_PATH)

    ################################################################################
    def _setup_logging(self):
        logger = logging.getLogger()
        logger.setLevel(constants.LOG_LEVEL)
        file_hdlr = logging.handlers.RotatingFileHandler(
            filename=constants.ERROR_LOGS_FILENAME,
            maxBytes=10 * 1024 * 1024,
            encoding="utf-8",
            backupCount=5,
            mode='a')
        file_hdlr.setFormatter(constants.LOG_FORMATTER)
        logger.addHandler(file_hdlr)
        self.log = logging.getLogger(__name__)

    ################################################################################
    def _check_files(self):
        create_files = CreateFiles(self.log)
        if not os.path.exists(constants.SETTINGS_FILENAME):
            create_files.create_settings_file()
        if not os.path.exists(constants.STYLE_QSS_FILENAME):
            create_files.create_style_file()

    ################################################################################
    def _check_new_program_version(self):
        self.qtObj.updateAvail_label.clear()
        self.qtObj.update_button.setVisible(False)
        self.client_version = constants.VERSION
        new_version_obj = utilities.check_new_program_version(self)
        if new_version_obj.new_version_available:
            self.new_version = new_version_obj.new_version
            self.new_version_msg = new_version_obj.new_version_msg
            self.qtObj.update_button.setFocus()
            self.qtObj.updateAvail_label.clear()
            self.qtObj.updateAvail_label.setText(new_version_obj.new_version_msg)
            self.qtObj.update_button.setVisible(True)

    ################################################################################
    @staticmethod
    def _update_program():
        href = QtCore.QUrl(constants.GITHUB_LATEST_VERSION_URL)
        QDesktopServices.openUrl(href)

    ################################################################################
    @staticmethod
    def _donate_clicked():
        href = QtCore.QUrl(constants.PAYPAL_URL)
        QDesktopServices.openUrl(href)

    ################################################################################
    def _enable_form(self):
        self.qtObj.startGw2_button.setEnabled(True)
        self.qtObj.currentParam_groupBox.setEnabled(True)
        num_pages = self.qtObj.main_tabWidget.count()
        for x in range(0, num_pages):
            self.qtObj.main_tabWidget.setTabEnabled(x, True)

    ################################################################################
    def _disable_form(self):
        self.qtObj.startGw2_button.setEnabled(False)
        self.qtObj.currentParam_groupBox.setEnabled(False)
        num_pages = self.qtObj.main_tabWidget.count()
        for x in range(0, num_pages):
            self.qtObj.main_tabWidget.setTabEnabled(x, False)

    ################################################################################
    def _register_form_events(self):
        # buttons
        self.qtObj.findGw2File_button.clicked.connect(lambda: self._get_gw2_file_name())
        self.qtObj.daFile_button.clicked.connect(lambda: self._get_dat_file_name())
        self.qtObj.startGw2_button.clicked.connect(lambda: self._start_gw2())
        self.qtObj.update_button.clicked.connect(lambda: self._update_program())
        self.qtObj.paypal_button.clicked.connect(lambda: self._donate_clicked())
        # port
        self.qtObj.port80_radioButton.clicked.connect(lambda: self._set_port())
        self.qtObj.port443_radioButton.clicked.connect(lambda: self._set_port())
        self.qtObj.port6112_radioButton.clicked.connect(lambda: self._set_port())
        # arcdps
        self.qtObj.arcdps_no_radioButton.clicked.connect(lambda: self._set_arcdps())
        self.qtObj.arcdps_yes_radioButton.clicked.connect(lambda: self._set_arcdps())
        # Parameters1
        self.qtObj.autologin_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.bit32_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.bmp_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.mapLoadinfo_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.mce_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.dx9single_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.forwardrenderer_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.log_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.nodelta_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.nomusic_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.noui_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.nosound_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.prefreset_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.shareArchive_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.uispanallmonitors_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.useOldFov_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.windowed_checkBox.clicked.connect(lambda: self._set_parameters1())
        self.qtObj.umbra_checkBox.clicked.connect(lambda: self._set_parameters1())
        # Parameters2
        self.qtObj.dat_checkBox.clicked.connect(lambda: self._set_parameters2())
        self.qtObj.verify_checkBox.clicked.connect(lambda: self._set_parameters2())
        self.qtObj.repair_checkBox.clicked.connect(lambda: self._set_parameters2())
        self.qtObj.diag_checkBox.clicked.connect(lambda: self._set_parameters2())
        self.qtObj.uninstall_checkBox.clicked.connect(lambda: self._set_parameters2())
        # text changed
        self.qtObj.assetsrv_textEdit.textChanged.connect(lambda: self._set_assetsrv())
        self.qtObj.authsrv_textEdit.textChanged.connect(lambda: self._set_authsrv())
        self.qtObj.portal_textEdit.textChanged.connect(lambda: self._set_portal())

    ################################################################################
    def _set_all_configs_on_form_from_settings_file(self):
        self.current_parameters_list = list()
        self.current_parameters_list.append(f"-clientport:{self.configs['port']}")
        if int(self.configs['port']) == 80:
            self.qtObj.port80_radioButton.setChecked(True)
            self.qtObj.port443_radioButton.setChecked(False)
            self.qtObj.port6112_radioButton.setChecked(False)
        elif int(self.configs['port']) == 443:
            self.qtObj.port80_radioButton.setChecked(False)
            self.qtObj.port443_radioButton.setChecked(True)
            self.qtObj.port6112_radioButton.setChecked(False)
        else:
            self.qtObj.port80_radioButton.setChecked(False)
            self.qtObj.port443_radioButton.setChecked(False)
            self.qtObj.port6112_radioButton.setChecked(True)

        if str(self.configs['arcdps']).lower() == "true":
            self.qtObj.arcdps_yes_radioButton.setChecked(True)
            self.qtObj.arcdps_no_radioButton.setChecked(False)
        else:
            self.qtObj.arcdps_yes_radioButton.setChecked(False)
            self.qtObj.arcdps_no_radioButton.setChecked(True)

        # Parameters1
        if str(self.configs['autologin']).lower() == "true":
            self.current_parameters_list.append("-autologin")
            self.qtObj.autologin_checkBox.setChecked(True)
        else:
            self.qtObj.autologin_checkBox.setChecked(False)

        if str(self.configs['32bits']).lower() == "true":
            self.current_parameters_list.append("-32")
            self.qtObj.bit32_checkBox.setChecked(True)
        else:
            self.qtObj.bit32_checkBox.setChecked(False)

        if str(self.configs['bmp']).lower() == "true":
            self.current_parameters_list.append("-bmp")
            self.qtObj.bmp_checkBox.setChecked(True)
        else:
            self.qtObj.bmp_checkBox.setChecked(False)

        if str(self.configs['mapLoadinfo']).lower() == "true":
            self.current_parameters_list.append("-mapLoadinfo")
            self.qtObj.mapLoadinfo_checkBox.setChecked(True)
        else:
            self.qtObj.mapLoadinfo_checkBox.setChecked(False)

        if str(self.configs['mce']).lower() == "true":
            self.current_parameters_list.append("-mce")
            self.qtObj.mce_checkBox.setChecked(True)
        else:
            self.qtObj.mce_checkBox.setChecked(False)

        if str(self.configs['dx9single']).lower() == "true":
            self.current_parameters_list.append("-dx9single")
            self.qtObj.dx9single_checkBox.setChecked(True)
        else:
            self.qtObj.dx9single_checkBox.setChecked(False)

        if str(self.configs["forwardrenderer"]).lower() == "true":
            self.current_parameters_list.append("-forwardrenderer")
            self.qtObj.forwardrenderer_checkBox.setChecked(True)
        else:
            self.qtObj.forwardrenderer_checkBox.setChecked(False)

        if str(self.configs['log']).lower() == "true":
            self.current_parameters_list.append("-log")
            self.qtObj.log_checkBox.setChecked(True)
        else:
            self.qtObj.log_checkBox.setChecked(False)

        if str(self.configs['nodelta']).lower() == "true":
            self.current_parameters_list.append("-nodelta")
            self.qtObj.nodelta_checkBox.setChecked(True)
        else:
            self.qtObj.nodelta_checkBox.setChecked(False)

        if str(self.configs['nomusic']).lower() == "true":
            self.current_parameters_list.append("-nomusic")
            self.qtObj.nomusic_checkBox.setChecked(True)
        else:
            self.qtObj.nomusic_checkBox.setChecked(False)

        if str(self.configs['noui']).lower() == "true":
            self.current_parameters_list.append("-noui")
            self.qtObj.noui_checkBox.setChecked(True)
        else:
            self.qtObj.noui_checkBox.setChecked(False)

        if str(self.configs['nosound']).lower() == "true":
            self.current_parameters_list.append("-nosound")
            self.qtObj.nosound_checkBox.setChecked(True)
        else:
            self.qtObj.nosound_checkBox.setChecked(False)

        if str(self.configs['prefreset']).lower() == "true":
            self.current_parameters_list.append("-prefreset")
            self.qtObj.prefreset_checkBox.setChecked(True)
        else:
            self.qtObj.prefreset_checkBox.setChecked(False)

        if str(self.configs['shareArchive']).lower() == "true":
            self.current_parameters_list.append("-shareArchive")
            self.qtObj.shareArchive_checkBox.setChecked(True)
        else:
            self.qtObj.shareArchive_checkBox.setChecked(False)

        if str(self.configs['uispanallmonitors']).lower() == "true":
            self.current_parameters_list.append("-uispanallmonitors")
            self.qtObj.uispanallmonitors_checkBox.setChecked(True)
        else:
            self.qtObj.uispanallmonitors_checkBox.setChecked(False)

        if str(self.configs['useOldFov']).lower() == "true":
            self.current_parameters_list.append("-useOldFov")
            self.qtObj.useOldFov_checkBox.setChecked(True)
        else:
            self.qtObj.useOldFov_checkBox.setChecked(False)

        if str(self.configs['windowed']).lower() == "true":
            self.current_parameters_list.append("-windowed")
            self.qtObj.windowed_checkBox.setChecked(True)
        else:
            self.qtObj.windowed_checkBox.setChecked(False)

        if str(self.configs['umbra']).lower() == "true":
            self.current_parameters_list.append("-umbra gpu")
            self.qtObj.umbra_checkBox.setChecked(True)
        else:
            self.qtObj.umbra_checkBox.setChecked(False)

        # Parameters2
        if self.configs['assetsrv'] is not None and self.configs['assetsrv'] != "":
            self.current_parameters_list.append(f"-assetsrv {self.configs['assetsrv']}")
            assetsrv_text = str(self.qtObj.assetsrv_textEdit.toPlainText())
            if assetsrv_text == "":
                self.qtObj.assetsrv_textEdit.setText(str(self.configs['assetsrv']))

        if self.configs['authsrv'] is not None and self.configs['authsrv'] != "":
            self.current_parameters_list.append(f"-authsrv {self.configs['authsrv']}")
            authsrv_text = str(self.qtObj.authsrv_textEdit.toPlainText())
            if authsrv_text == "":
                self.qtObj.authsrv_textEdit.setText(str(self.configs['authsrv']))

        if self.configs['portal'] is not None and self.configs['portal'] != "":
            self.current_parameters_list.append(f"-portal {self.configs['portal']}")
            portal_text = str(self.qtObj.portal_textEdit.toPlainText())
            if portal_text == "":
                self.qtObj.portal_textEdit.setText(str(self.configs['portal']))

        if str(self.configs['useDatFile']).lower() == "true":
            if (self.configs['datFile'] is not None) and (self.configs['datFile'] != ""):
                self.qtObj.dat_checkBox.setChecked(True)
                self.current_parameters_list.append(f"-dat {self.configs['datFile']}")
                dat_checkBox_text = str(self.qtObj.dat_checkBox.text())
                if dat_checkBox_text == "":
                    self.qtObj.dat_checkBox.setText(str(self.configs['datFile']))
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.configs['useDatFile'] = False
                utilities.set_file_settings("Parameters2", "usedatfile", str(self.configs['useDatFile']))

        if (self.configs['datFile'] is not None) and (self.configs['datFile'] != ""):
            self.qtObj.dat_checkBox.setText(str(self.configs['datFile']))

        # Other Utilities
        if str(self.configs['verify']).lower() == "true":
            self.current_parameters_list.append("-verify")
            self.qtObj.verify_checkBox.setChecked(True)
        else:
            self.qtObj.verify_checkBox.setChecked(False)

        if str(self.configs['repair']).lower() == "true":
            self.current_parameters_list.append("-repair")
            self.qtObj.repair_checkBox.setChecked(True)
        else:
            self.qtObj.repair_checkBox.setChecked(False)

        if str(self.configs['diag']).lower() == "true":
            self.current_parameters_list.append("-diag")
            self.qtObj.diag_checkBox.setChecked(True)
        else:
            self.qtObj.diag_checkBox.setChecked(False)

        if str(self.configs['uninstall']).lower() == "true":
            self.current_parameters_list.append("-uninstall")
            self.qtObj.uninstall_checkBox.setChecked(True)
        else:
            self.qtObj.uninstall_checkBox.setChecked(False)

        self.current_parameters = str(' '.join(self.current_parameters_list))
        self.qtObj.current_param_label.setText(str(self.current_parameters))
        if self.qtObj.gw2Path_label.text() == "":
            self.qtObj.gw2Path_label.setText(str(self.configs['gw2Path']))

    ################################################################################
    def _get_gw2_file_name(self):
        path = str(utilities.dialog_get_file_path())
        if path != "":
            file_name = str(path.split("\\")[-1])
            gw2_name = constants.GW2_64_BIT_EXEC_NAME

            if gw2_name.lower() == file_name.lower():
                self.qtObj.gw2Path_label.setText(path)
                self.configs['gw2Path'] = path
                self._enable_form()
                utilities.set_file_settings("GW2", "gw2Path", f"\"{path}\"")
            elif file_name.lower() == "gw2.exe":
                utilities.show_message_window("error", "ERROR", str(messages.gw2_32bit_not_supported))
            else:
                not_valid_gw2_msg = f"\"{file_name}\" {messages.not_valid_gw2}"
                utilities.show_message_window("error", "ERROR", not_valid_gw2_msg)

        if str(self.configs['gw2Path']) == "" or self.configs['gw2Path'] is None:
            self._disable_form()
            self.qtObj.gw2Path_label.clear()
            self.qtObj.gw2Path_label.setText(messages.need_find_gw2)
            self.qtObj.findGw2File_button.setFocus()

    ################################################################################
    def _get_dat_file_name(self):
        path = str(utilities.dialog_get_file_path())
        if path != "":
            filename = str(path.split("\\")[-1])
            file_extension = str(filename.split(".")[-1])
            final_values = {}
            final_values['Parameters2'] = {}
            if file_extension == "dat":
                self.qtObj.dat_checkBox.setChecked(True)
                self.qtObj.dat_checkBox.setText(path)
                self.configs['datFile'] = path
                self.configs['useDatFile'] = True
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.qtObj.dat_checkBox.setText("")
                self.configs['datFile'] = ""
                self.configs['useDatFile'] = False
                message = f"\"{filename}\" is not a valid dat file!!!"
                utilities.show_message_window("error", "ERROR", message)

            final_values['Parameters2']['datFile'] = str(self.configs['datFile'])
            final_values['Parameters2']['useDatFile'] = str(self.configs['useDatFile'])
            utilities.set_all_ini_file_settings(constants.SETTINGS_FILENAME, final_values)
            self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_parameters1(self):
        final_values = {}
        final_values['Parameters1'] = {}

        if self.qtObj.autologin_checkBox.isChecked():
            self.configs['autologin'] = True
        else:
            self.configs['autologin'] = False
        final_values['Parameters1']['autologin'] = str(self.configs['autologin'])

        if self.qtObj.bit32_checkBox.isChecked():
            self.configs['32bits'] = True
        else:
            self.configs['32bits'] = False
        final_values['Parameters1']['32bits'] = str(self.configs['32bits'])

        if self.qtObj.bmp_checkBox.isChecked():
            self.configs['bmp'] = True
        else:
            self.configs['bmp'] = False
        final_values['Parameters1']['bmp'] = str(self.configs['bmp'])

        if self.qtObj.mapLoadinfo_checkBox.isChecked():
            self.configs['mapLoadinfo'] = True
        else:
            self.configs['mapLoadinfo'] = False
        final_values['Parameters1']['mapLoadinfo'] = str(self.configs['mapLoadinfo'])

        if self.qtObj.mce_checkBox.isChecked():
            self.configs['mce'] = True
        else:
            self.configs['mce'] = False
        final_values['Parameters1']['mce'] = str(self.configs['mce'])

        if self.qtObj.dx9single_checkBox.isChecked():
            self.configs['dx9single'] = True
        else:
            self.configs['dx9single'] = False
        final_values['Parameters1']['dx9single'] = str(self.configs['dx9single'])

        if self.qtObj.forwardrenderer_checkBox.isChecked():
            self.configs["forwardrenderer"] = True
        else:
            self.configs["forwardrenderer"] = False
        final_values['Parameters1']['forwardrenderer'] = str(self.configs['forwardrenderer'])

        if self.qtObj.log_checkBox.isChecked():
            self.configs['log'] = True
        else:
            self.configs['log'] = False
        final_values['Parameters1']['log'] = str(self.configs['log'])

        if self.qtObj.nodelta_checkBox.isChecked():
            self.configs['nodelta'] = True
        else:
            self.configs['nodelta'] = False
        final_values['Parameters1']['nodelta'] = str(self.configs['nodelta'])

        if self.qtObj.nomusic_checkBox.isChecked():
            self.configs['nomusic'] = True
        else:
            self.configs['nomusic'] = False
        final_values['Parameters1']['nomusic'] = str(self.configs['nomusic'])

        if self.qtObj.noui_checkBox.isChecked():
            self.configs['noui'] = True
        else:
            self.configs['noui'] = False
        final_values['Parameters1']['noui'] = str(self.configs['noui'])

        if self.qtObj.nosound_checkBox.isChecked():
            self.configs['nosound'] = True
        else:
            self.configs['nosound'] = False
        final_values['Parameters1']['nosound'] = str(self.configs['nosound'])

        if self.qtObj.prefreset_checkBox.isChecked():
            self.configs['prefreset'] = True
        else:
            self.configs['prefreset'] = False
        final_values['Parameters1']['prefreset'] = str(self.configs['prefreset'])

        if self.qtObj.shareArchive_checkBox.isChecked():
            self.configs['shareArchive'] = True
        else:
            self.configs['shareArchive'] = False
        final_values['Parameters1']['shareArchive'] = str(self.configs['shareArchive'])

        if self.qtObj.uispanallmonitors_checkBox.isChecked():
            self.configs['uispanallmonitors'] = True
        else:
            self.configs['uispanallmonitors'] = False
        final_values['Parameters1']['uispanallmonitors'] = str(self.configs['uispanallmonitors'])

        if self.qtObj.useOldFov_checkBox.isChecked():
            self.configs['useOldFov'] = True
        else:
            self.configs['useOldFov'] = False
        final_values['Parameters1']['useOldFov'] = str(self.configs['useOldFov'])

        if self.qtObj.windowed_checkBox.isChecked():
            self.configs['windowed'] = True
        else:
            self.configs['windowed'] = False
        final_values['Parameters1']['windowed'] = str(self.configs['windowed'])

        if self.qtObj.umbra_checkBox.isChecked():
            self.configs['umbra'] = True
        else:
            self.configs['umbra'] = False
        final_values['Parameters1']['umbra'] = str(self.configs['umbra'])

        utilities.set_all_ini_file_settings(constants.SETTINGS_FILENAME, final_values)
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_parameters2(self):
        final_values = {}
        final_values['Parameters2'] = {}

        if self.qtObj.dat_checkBox.isChecked():
            if (self.configs['datFile'] is not None) and (self.configs['datFile'] != ""):
                self.configs['useDatFile'] = True
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.configs['useDatFile'] = False
        else:
            self.qtObj.dat_checkBox.setChecked(False)
            self.configs['useDatFile'] = False
        final_values['Parameters2']['useDatFile'] = str(self.configs['useDatFile'])

        if self.qtObj.verify_checkBox.isChecked():
            self.configs['verify'] = True
        else:
            self.configs['verify'] = False
        final_values['Parameters2']['verify'] = str(self.configs['verify'])

        if self.qtObj.repair_checkBox.isChecked():
            self.configs['repair'] = True
        else:
            self.configs['repair'] = False
        final_values['Parameters2']['repair'] = str(self.configs['repair'])

        if self.qtObj.diag_checkBox.isChecked():
            self.configs['diag'] = True
        else:
            self.configs['diag'] = False
        final_values['Parameters2']['diag'] = str(self.configs['diag'])

        if self.qtObj.uninstall_checkBox.isChecked():
            self.configs['uninstall'] = True
        else:
            self.configs['uninstall'] = False
        final_values['Parameters2']['uninstall'] = str(self.configs['uninstall'])

        utilities.set_all_ini_file_settings(constants.SETTINGS_FILENAME, final_values)
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_assetsrv(self):
        assetsrv_textEdit = str(self.qtObj.assetsrv_textEdit.toPlainText())

        if assetsrv_textEdit is not None and assetsrv_textEdit != "":
            self.configs['assetsrv'] = assetsrv_textEdit
        else:
            self.configs['assetsrv'] = ""

        utilities.set_file_settings("Parameters2", "assetsrv", f"\"{self.configs['assetsrv']}\"")
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_authsrv(self):
        authsrv_textEdit = str(self.qtObj.authsrv_textEdit.toPlainText())

        if authsrv_textEdit is not None and authsrv_textEdit != "":
            self.configs['authsrv'] = authsrv_textEdit
        else:
            self.configs['authsrv'] = ""

        utilities.set_file_settings("Parameters2", "authsrv", f"\"{self.configs['authsrv']}\"")
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_portal(self):
        portal_textEdit = str(self.qtObj.portal_textEdit.toPlainText())

        if portal_textEdit is not None and portal_textEdit != "":
            self.configs['portal'] = portal_textEdit
        else:
            self.configs['portal'] = ""

        utilities.set_file_settings("Parameters2", "portal", f"\"{self.configs['portal']}\"")
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_port(self):
        if self.qtObj.port80_radioButton.isChecked():
            self.configs['port'] = 80
        elif self.qtObj.port443_radioButton.isChecked():
            self.configs['port'] = 443
        else:
            self.configs['port'] = 6112

        utilities.set_file_settings("GW2", "port", str(self.configs['port']))
        self._set_all_configs_on_form_from_settings_file()

    ################################################################################
    def _set_arcdps(self):
        self.qtObj.main_tabWidget.setCurrentIndex(2)
        window_type = None
        window_title = None
        msg = None

        if self.qtObj.arcdps_yes_radioButton.isChecked():
            if self._update_arcdps():
                window_type = "information"
                window_title = "Installed"
                msg = messages.arcdps_installed
                self.configs['arcdps'] = True
            else:
                window_type = "error"
                window_title = "ERROR"
                msg = messages.arcdps_error_install
                self.configs['arcdps'] = False
                self.qtObj.arcdps_yes_radioButton.setChecked(False)
                self.qtObj.arcdps_no_radioButton.setChecked(True)
        elif self.qtObj.arcdps_no_radioButton.isChecked():
            if utilities.remove_arcdps_files(self):
                window_type = "information"
                window_title = "Removed"
                msg = messages.arcdps_removed
                self.configs['arcdps'] = False
            else:
                window_type = "error"
                window_title = "ERROR"
                msg = messages.arcdps_error_remove
                self.configs['arcdps'] = True
                self.qtObj.arcdps_yes_radioButton.setChecked(True)
                self.qtObj.arcdps_no_radioButton.setChecked(False)

        utilities.set_file_settings("GW2", "arcdps", str(self.configs['arcdps']))
        utilities.show_message_window(window_type, window_title, msg)

    ################################################################################
    def _check_arcdps_installed(self):
        gw2_dir_path = ""
        if self.configs['gw2Path'] is not None:
            gw2_dir_path = os.path.dirname(self.configs['gw2Path'])

        if os.path.exists(f"{gw2_dir_path}\\bin64\\"):
            d3d9_path = f"{gw2_dir_path}\\bin64\\d3d9.dll"
            if os.path.isfile(d3d9_path):
                self.configs['arcdps'] = True
                self.qtObj.arcdps_yes_radioButton.setChecked(True)
                self.qtObj.arcdps_no_radioButton.setChecked(False)
                utilities.set_file_settings("GW2", "arcdps", str(self.configs['arcdps']))
                return

        self.configs['arcdps'] = False
        self.qtObj.arcdps_yes_radioButton.setChecked(False)
        self.qtObj.arcdps_no_radioButton.setChecked(True)
        utilities.set_file_settings("GW2", "arcdps", str(self.configs['arcdps']))

    ################################################################################
    def _update_arcdps(self):
        gw2_dir_path = os.path.dirname(self.configs['gw2Path'])
        d3d9_url = constants.D3D9_URL
        md5sum_url = constants.MD5SUM_URL
        d3d9_path = f"{gw2_dir_path}{constants.D3D9_PATH}"

        if self.qtObj.arcdps_yes_radioButton.isChecked():
            if not os.path.exists(f"{gw2_dir_path}\\bin64\\"):
                os.makedirs(f"{gw2_dir_path}\\bin64\\")

            if os.path.isfile(d3d9_path):
                self._disable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)

                try:
                    req_d3d9_md5 = ""
                    req = requests.get(md5sum_url, stream=True, timeout=1)
                    if req.status_code == 200:
                        req_d3d9_md5 = str(req.text.split()[0])
                    else:
                        utilities.show_message_window("error", "ERROR", messages.arcdps_timeout)
                        self.log.error(messages.arcdps_timeout)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)
                        return False
                # except requests.exceptions.ConnectionError as e:
                except Exception as e:
                    self.log.error(f"{e} {md5sum_url}")
                    self._enable_form()
                    self.qtObj.main_tabWidget.setCurrentIndex(2)
                    return False

                current_d3d9_md5 = utilities.md5Checksum(d3d9_path)
                if req_d3d9_md5 != current_d3d9_md5:
                    utilities.backup_arcdps_files(self, "backup")

                    # try D3D9_URL
                    try:
                        r = requests.get(d3d9_url)
                        with open(d3d9_path, 'wb') as outfile:
                            outfile.write(r.content)
                    except requests.HTTPError as e:
                        utilities.remove_arcdps_files(self)
                        utilities.backup_arcdps_files(self, "revert_backup")
                        self.log.error(f"{e} {d3d9_url}")
                        utilities.show_message_window("error", "ERROR", messages.arcdps_404)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)
                        return False

                    utilities.remove_arcdps_backup_files(self)

                self._enable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)
                return True
            else:
                utilities.remove_arcdps_files(self)
                arcdps_url = constants.ARCDPS_URL
                self._disable_form()

                # check arcdps website is up
                try:
                    requests.get(arcdps_url)
                except requests.exceptions.ConnectionError as e:
                    self.log.error(f"{e} {arcdps_url}")
                    self._enable_form()
                    return False

                # try D3D9_URL
                try:
                    r = requests.get(d3d9_url)
                    with open(d3d9_path, 'wb') as outfile:
                        outfile.write(r.content)
                except requests.HTTPError as e:
                    utilities.remove_arcdps_files(self)
                    self.log.error(f"{e} {d3d9_url}")
                    utilities.show_message_window("error", "ERROR", messages.arcdps_404)
                    self._enable_form()
                    return False

                utilities.remove_arcdps_backup_files(self)

                self._enable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)
                return True

    ################################################################################
    def _set_arcdps_tab(self):
        arcdps_url = constants.ARCDPS_URL
        arcdps_ref = "<p align=\"left\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;" \
                     + f"margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"{arcdps_url}" \
                     + f"\"><span style=\" font-size:9pt; text-decoration: underline; color:#FFFFFF;\">{arcdps_url}" \
                     + "</span></a></p>"

        self.qtObj.arcdps_disclamer_label.setText(messages.arcdps_disclamer)
        self.qtObj.arcps_url_textBrowser.setHtml(arcdps_ref)

        try:
            response = requests.get(arcdps_url, stream=True, timeout=1)
            if response.status_code != 200:
                self.log.error(messages.arcdps_error_dl)
            else:
                html = str(response.text)
                soup = BeautifulSoup(html, "html.parser")
                body = soup.body
                blist = str(body).split("<b>")

                for content in blist:
                    if content.startswith('changes'):
                        changes = content.replace("changes</b><br/>", "").replace("<br/>", "").replace("     ", "")
                        version = content.split()[1].replace(":", "")
                    # if content.startswith('download'):
                    #     version = content.split("</a>")[1].split("<br/>")[0].strip(" (").strip(")")

                self.qtObj.arcdps_webpage_textEdit.setPlainText(changes.strip())
                self.qtObj.arcdps_current_version_label.setText(version.strip())
        # except requests.exceptions.ConnectionError as e:
        except Exception as e:
            self.log.error(f"{messages.arcdps_unreacheable} {e}")
            utilities.show_message_window("error", "ERROR", messages.arcdps_unreacheable)
            self.qtObj.arcdps_webpage_textEdit.setPlainText(messages.arcdps_unreacheable)
            self.qtObj.arcdps_current_version_label.setText("---")

    ################################################################################
    def _start_gw2(self):
        if os.path.exists(self.configs['gw2Path']):
            program = str(self.configs['gw2Path'])
            working_directory = os.path.dirname(self.configs['gw2Path'])
            arguments = self.current_parameters_list
            my_process = QtCore.QProcess()
            my_process.setWorkingDirectory(working_directory)
            my_process.setProgram(program)
            my_process.setArguments(arguments)
            my_process.startDetached()
            my_process.started.connect(self._gw2_process_started())
        else:
            utilities.show_message_window("error", "ERROR",
                                          f"{messages.gw2_not_found}\n"
                                          f"{self.configs['gw2Path']}\n\n"
                                          f"{messages.gw2_uninstalled}\n"
                                          f"{messages.find_gw2_exec}")

    ################################################################################
    def _gw2_process_started(self):
        self._disable_form()
        sleep(constants.EXIT_TIMER)
        sys.exit()
