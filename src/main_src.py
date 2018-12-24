#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.6
#|*****************************************************
# # -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from src.utils.create_files import CreateFiles 
from src.utils import constants, messages, utils
import logging.handlers
import sys, os, base64
from time import sleep
import requests, urllib.request
from bs4 import BeautifulSoup
################################################################################
################################################################################
################################################################################
class MainSrc():
    def __init__(self, qtObj, form):
        self.qtObj = qtObj
        self.form = form
################################################################################
################################################################################
################################################################################
    def init(self):
        self._check_dirs()
        self._setup_logging()
        self._check_files()
        self._check_new_program_version()
        self._get_all_configs_from_settings_file()
        self._update_arcdps()
        self._set_arcdps_tab()
        sys.excepthook = utils.log_uncaught_exceptions

        if self.useTheme:
            self.form.setStyleSheet(open(constants.style_qss_filename,"r").read())
        
        if self.gw2Path is None or self.gw2Path == "":
            self._disable_form()
            find_gw2_exec_msg = messages.find_gw2_exec
            utils.show_message_box("info", find_gw2_exec_msg)
            self._get_gw2_file_name()
        else:
            self._enable_form()
            
        self._set_all_configs_on_form_from_settings_file()
        self._register_form_events()
        self.qtObj.main_tabWidget.setCurrentIndex(0)
        self.qtObj.findGw2File_button.setFocus()
################################################################################
################################################################################
################################################################################
    def _check_dirs(self):
        if not os.path.exists(constants.program_path):
            os.makedirs(constants.program_path)  
#         if not os.path.exists(constants.data_path):
#             os.makedirs(constants.data_path)              
#         if not os.path.exists(constants.logs_path):
#             os.makedirs(constants.logs_path)  
################################################################################
################################################################################
################################################################################
    def _setup_logging(self):
        logger = logging.getLogger()
        logger.setLevel(constants.LOG_LEVEL)
        file_hdlr = logging.handlers.RotatingFileHandler(
            filename=constants.error_logs_filename,
            maxBytes=10 * 1024 * 1024,
            encoding="utf-8",
            backupCount=5,
            mode='a')
        file_hdlr.setFormatter(constants.LOG_FORMATTER)
        logger.addHandler(file_hdlr)
        self.log = logging.getLogger(__name__)
################################################################################
################################################################################
################################################################################
    def _check_files(self):
        createFiles = CreateFiles(self.log)
        if not os.path.exists(constants.settings_filename):
            createFiles.create_settings_file()
        if not os.path.exists(constants.style_qss_filename):
            createFiles.create_style_file()
################################################################################
################################################################################
################################################################################
    def _enable_form(self):
        self.qtObj.startGw2_button.setEnabled(True)
        self.qtObj.currentParam_groupBox.setEnabled(True)
        self.qtObj.main_tabWidget.setTabEnabled(0,True)
        self.qtObj.main_tabWidget.setTabEnabled(1,True)
        self.qtObj.main_tabWidget.setTabEnabled(2,True)
        self.qtObj.main_tabWidget.setTabEnabled(3,True)
################################################################################
################################################################################
################################################################################
    def _disable_form(self):
        self.qtObj.startGw2_button.setEnabled(False)
        self.qtObj.currentParam_groupBox.setEnabled(False)
        self.qtObj.main_tabWidget.setTabEnabled(0,False)
        self.qtObj.main_tabWidget.setTabEnabled(1,False)
        self.qtObj.main_tabWidget.setTabEnabled(2,False)
        self.qtObj.main_tabWidget.setTabEnabled(3,False)
################################################################################
################################################################################
################################################################################  
    def _register_form_events(self):
        # buttons
        self.qtObj.findGw2File_button.clicked.connect(lambda: self._get_gw2_file_name())
        self.qtObj.daFile_button.clicked.connect(lambda: self._get_dat_file_name())
        self.qtObj.startGw2_button.clicked.connect(lambda: self._start_gw2())
        # port
        self.qtObj.port80_radioButton.clicked.connect(lambda: self._set_port())
        self.qtObj.port443_radioButton.clicked.connect(lambda: self._set_port())
        self.qtObj.port6112_radioButton.clicked.connect(lambda: self._set_port())
        # arcdps
        self.qtObj.arcdps_yes_radioButton.clicked.connect(lambda: self._set_arcdps())
        self.qtObj.arcdps_no_radioButton.clicked.connect(lambda: self._set_arcdps())
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
################################################################################
################################################################################
    def _get_all_configs_from_settings_file(self):
        # Configs
        useTheme = utils.get_file_settings("Configs", "useTheme")
        if useTheme is None:
            self.useTheme = True
        else:
            self.useTheme = useTheme
        
        # GW2
        self.gw2Path            = utils.get_file_settings("GW2", "gw2Path")
        self.port               = utils.get_file_settings("GW2", "port")
        self.arcdps             = utils.get_file_settings("GW2", "arcdps")
        # Parameters1
        self.autologin          = utils.get_file_settings("Parameters1", "autologin")
        self.bits32             = utils.get_file_settings("Parameters1", "32bits")
        self.bmp                = utils.get_file_settings("Parameters1", "bmp")
        self.mapLoadinfo        = utils.get_file_settings("Parameters1", "mapLoadinfo")
        self.mce                = utils.get_file_settings("Parameters1", "mce")
        self.dx9single          = utils.get_file_settings("Parameters1", "dx9single")
        self.forwardrenderer    = utils.get_file_settings("Parameters1", "forwardrenderer")
        self.gw2Log             = utils.get_file_settings("Parameters1", "log")
        self.nodelta            = utils.get_file_settings("Parameters1", "nodelta")
        self.nomusic            = utils.get_file_settings("Parameters1", "nomusic")
        self.noui               = utils.get_file_settings("Parameters1", "noui")
        self.nosound            = utils.get_file_settings("Parameters1", "nosound")
        self.prefreset          = utils.get_file_settings("Parameters1", "prefreset")
        self.shareArchive       = utils.get_file_settings("Parameters1", "shareArchive")
        self.uispanallmonitors  = utils.get_file_settings("Parameters1", "uispanallmonitors")
        self.useOldFov          = utils.get_file_settings("Parameters1", "useOldFov")
        self.windowed           = utils.get_file_settings("Parameters1", "windowed")
        self.umbra              = utils.get_file_settings("Parameters1", "umbra")
        # Parameters2
        self.assetsrv           = utils.get_file_settings("Parameters2", "assetsrv")
        self.authsrv            = utils.get_file_settings("Parameters2", "authsrv")
        self.portal             = utils.get_file_settings("Parameters2", "portal") 
        self.datFile            = utils.get_file_settings("Parameters2", "datFile") 
        self.useDatFile         = utils.get_file_settings("Parameters2", "useDatFile")  
        self.verify             = utils.get_file_settings("Parameters2", "verify")  
        self.repair             = utils.get_file_settings("Parameters2", "repair")  
        self.diag               = utils.get_file_settings("Parameters2", "diag")  
        self.uninstall          = utils.get_file_settings("Parameters2", "uninstall")      
################################################################################
################################################################################
################################################################################    
    def _set_all_configs_on_form_from_settings_file(self):
        self.current_parameters_list = list()
        self.current_parameters_list.append(f"-clientport:{self.port}")
        if self.port == 80:
            self.qtObj.port80_radioButton.setChecked(True)
            self.qtObj.port443_radioButton.setChecked(False)
            self.qtObj.port6112_radioButton.setChecked(False)
        elif self.port == 443:  
            self.qtObj.port80_radioButton.setChecked(False)
            self.qtObj.port443_radioButton.setChecked(True)
            self.qtObj.port6112_radioButton.setChecked(False)
        else:
            self.qtObj.port80_radioButton.setChecked(False)
            self.qtObj.port443_radioButton.setChecked(False)
            self.qtObj.port6112_radioButton.setChecked(True)
            
        if str(self.arcdps).lower() == "true":
            self.qtObj.arcdps_yes_radioButton.setChecked(True)
            self.qtObj.arcdps_no_radioButton.setChecked(False)
        else:
            self.qtObj.arcdps_yes_radioButton.setChecked(False)
            self.qtObj.arcdps_no_radioButton.setChecked(True)
        
        # Parameters1
        if str(self.autologin).lower() == "true":
            self.current_parameters_list.append("-autologin")
            self.qtObj.autologin_checkBox.setChecked(True)
        else:
            self.qtObj.autologin_checkBox.setChecked(False)

        if str(self.bits32).lower() == "true":
            self.current_parameters_list.append("-32")
            self.qtObj.bit32_checkBox.setChecked(True)
        else:
            self.qtObj.bit32_checkBox.setChecked(False)
            
        if str(self.bmp).lower() == "true":
            self.current_parameters_list.append("-bmp")
            self.qtObj.bmp_checkBox.setChecked(True)
        else:
            self.qtObj.bmp_checkBox.setChecked(False)
            
        if str(self.mapLoadinfo).lower() == "true":
            self.current_parameters_list.append("-mapLoadinfo")
            self.qtObj.mapLoadinfo_checkBox.setChecked(True)
        else:
            self.qtObj.mapLoadinfo_checkBox.setChecked(False)
            
        if str(self.mce).lower() == "true":
            self.current_parameters_list.append("-mce")
            self.qtObj.mce_checkBox.setChecked(True)
        else:
            self.qtObj.mce_checkBox.setChecked(False)
            
        if str(self.dx9single).lower() == "true":
            self.current_parameters_list.append("-dx9single")
            self.qtObj.dx9single_checkBox.setChecked(True)
        else:
            self.qtObj.dx9single_checkBox.setChecked(False)
            
        if str(self.forwardrenderer).lower() == "true":
            self.current_parameters_list.append("-forwardrenderer")
            self.qtObj.forwardrenderer_checkBox.setChecked(True)
        else:
            self.qtObj.forwardrenderer_checkBox.setChecked(False)
            
        if str(self.gw2Log).lower() == "true":
            self.current_parameters_list.append("-log")
            self.qtObj.log_checkBox.setChecked(True)
        else:
            self.qtObj.log_checkBox.setChecked(False)
            
        if str(self.nodelta).lower() == "true":
            self.current_parameters_list.append("-nodelta")
            self.qtObj.nodelta_checkBox.setChecked(True)
        else:
            self.qtObj.nodelta_checkBox.setChecked(False)
            
        if str(self.nomusic).lower() == "true":
            self.current_parameters_list.append("-nomusic")
            self.qtObj.nomusic_checkBox.setChecked(True)
        else:
            self.qtObj.nomusic_checkBox.setChecked(False)
            
        if str(self.noui).lower() == "true":
            self.current_parameters_list.append("-noui")
            self.qtObj.noui_checkBox.setChecked(True)
        else:
            self.qtObj.noui_checkBox.setChecked(False)
            
        if str(self.nosound).lower() == "true":
            self.current_parameters_list.append("-nosound")
            self.qtObj.nosound_checkBox.setChecked(True)
        else:
            self.qtObj.nosound_checkBox.setChecked(False)
            
        if str(self.prefreset).lower() == "true":
            self.current_parameters_list.append("-prefreset")
            self.qtObj.prefreset_checkBox.setChecked(True)
        else:
            self.qtObj.prefreset_checkBox.setChecked(False)
            
        if str(self.shareArchive).lower() == "true":
            self.current_parameters_list.append("-shareArchive")
            self.qtObj.shareArchive_checkBox.setChecked(True)
        else:
            self.qtObj.shareArchive_checkBox.setChecked(False)

        if str(self.uispanallmonitors).lower() == "true":
            self.current_parameters_list.append("-uispanallmonitors")
            self.qtObj.uispanallmonitors_checkBox.setChecked(True)
        else:
            self.qtObj.uispanallmonitors_checkBox.setChecked(False)

        if str(self.useOldFov).lower() == "true":
            self.current_parameters_list.append("-useOldFov")
            self.qtObj.useOldFov_checkBox.setChecked(True)
        else:
            self.qtObj.useOldFov_checkBox.setChecked(False)

        if str(self.windowed).lower() == "true":
            self.current_parameters_list.append("-windowed")
            self.qtObj.windowed_checkBox.setChecked(True)
        else:
            self.qtObj.windowed_checkBox.setChecked(False)

        if str(self.umbra).lower() == "true":
            self.current_parameters_list.append("-umbra gpu")
            self.qtObj.umbra_checkBox.setChecked(True)
        else:
            self.qtObj.umbra_checkBox.setChecked(False)

        # Parameters2
        if self.assetsrv is not None and self.assetsrv != "":
            self.current_parameters_list.append(f"-assetsrv {self.assetsrv}")
            assetsrv_text = str(self.qtObj.assetsrv_textEdit.toPlainText())
            if assetsrv_text == "":
                self.qtObj.assetsrv_textEdit.setText(str(self.assetsrv))
  
        if self.authsrv is not None and self.authsrv != "":
            self.current_parameters_list.append(f"-authsrv {self.authsrv}")
            authsrv_text = str(self.qtObj.authsrv_textEdit.toPlainText())
            if authsrv_text == "":
                self.qtObj.authsrv_textEdit.setText(str(self.authsrv))    
       
        if self.portal is not None and self.portal != "":
            self.current_parameters_list.append(f"-portal {self.portal}") 
            portal_text = str(self.qtObj.portal_textEdit.toPlainText())
            if portal_text == "":
                self.qtObj.portal_textEdit.setText(str(self.portal)) 
            
        if (str(self.useDatFile).lower() == "true"):
            if (self.datFile is not None) and (self.datFile != ""):
                self.qtObj.dat_checkBox.setChecked(True)
                self.current_parameters_list.append(f"-dat {self.datFile}")
                dat_checkBox_text = str(self.qtObj.dat_checkBox.text())
                if dat_checkBox_text == "":
                    self.qtObj.dat_checkBox.setText(str(self.datFile))                 
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.useDatFile = False
                utils.set_file_settings("Parameters2", "usedatfile", str(self.useDatFile))
                
        if (self.datFile is not None) and (self.datFile != ""):
                self.qtObj.dat_checkBox.setText(str(self.datFile))
        
        #Other Utilities
        if str(self.verify).lower() == "true":
            self.current_parameters_list.append("-verify")
            self.qtObj.verify_checkBox.setChecked(True)
        else:
            self.qtObj.verify_checkBox.setChecked(False)

        if str(self.repair).lower() == "true":
            self.current_parameters_list.append("-repair")
            self.qtObj.repair_checkBox.setChecked(True)
        else:
            self.qtObj.repair_checkBox.setChecked(False)
            
        if str(self.diag).lower() == "true":
            self.current_parameters_list.append("-diag")
            self.qtObj.diag_checkBox.setChecked(True)
        else:
            self.qtObj.diag_checkBox.setChecked(False)            
            
        if str(self.uninstall).lower() == "true":
            self.current_parameters_list.append("-uninstall")
            self.qtObj.uninstall_checkBox.setChecked(True)
        else:
            self.qtObj.uninstall_checkBox.setChecked(False)  
        
        self.current_parameters = str(' '.join(self.current_parameters_list))
        self.qtObj.current_param_label.setText(str(self.current_parameters))
        if self.qtObj.gw2Path_label.text() == "":
            self.qtObj.gw2Path_label.setText(str(self.gw2Path))
################################################################################
################################################################################
################################################################################
    def _get_gw2_file_name(self):
        path = str(utils.open_get_filename(self))
        file_name = None
        if path is not "":
            file_name = str(path.split("/")[-1])
            gw2_names = constants.gw2_64_bit_exec_name
            
            for value in gw2_names:
                if value.lower() == file_name.lower():
                    self.qtObj.gw2Path_label.setText(path)
                    self.gw2Path = path
                    self._enable_form()
                    utils.set_file_settings("GW2", "gw2path", f"\"{self.gw2Path}\"") 
                    return

        if str(self.gw2Path) == "":
            self._disable_form()
            self.qtObj.gw2Path_label.clear()
            self.qtObj.gw2Path_label.setText(messages.need_find_gw2)
            self.qtObj.findGw2File_button.setFocus()

        if file_name is not None:
            if file_name.lower() == "gw2.exe":
                utils.show_message_box("error", str(messages.gw2_32bit_not_supported))
                return
            
            not_valid_gw2_msg = f"\"{file_name}\" {messages.not_valid_gw2}"
            utils.show_message_box("error", not_valid_gw2_msg)
################################################################################
################################################################################
################################################################################
    def _get_dat_file_name(self):
        path = str(utils.open_get_filename(self))
        if path is not "":
            filename = str(path.split("/")[-1])
            file_extension = str(filename.split(".")[-1])
            if file_extension == "dat":
                self.qtObj.dat_checkBox.setChecked(True)
                self.qtObj.dat_checkBox.setText(path)
                self.datFile = path
                self.useDatFile = True
                utils.set_file_settings("Parameters2", "datfile", f"\"{self.datFile}\"")
                utils.set_file_settings("Parameters2", "usedatfile", f"\"{self.usedatfile}\"")
                self._set_all_configs_on_form_from_settings_file() 
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.qtObj.dat_checkBox.setText("")
                self.datFile = ""
                self.useDatFile = False
                utils.set_file_settings("Parameters2", "datfile", f"\"{self.datFile}\"")
                utils.set_file_settings("Parameters2", "usedatfile", f"\"{self.usedatfile}\"")
                self._set_all_configs_on_form_from_settings_file() 
                message = f"\"{filename}\" is not a valid dat file!!!"
                utils.show_message_box("error", message)  
################################################################################
################################################################################
################################################################################
    def _set_parameters1(self):
        if self.qtObj.autologin_checkBox.isChecked():
            self.autologin = True
        else:
            self.autologin = False
        utils.set_file_settings("Parameters1", "autologin", str(self.autologin))
            
        if self.qtObj.bit32_checkBox.isChecked():
            self.bits32 = True
        else:
            self.bits32 = False
        utils.set_file_settings("Parameters1", "32bits", str(self.bits32))            
            
        if self.qtObj.bmp_checkBox.isChecked():
            self.bmp = True
        else:
            self.bmp = False
        utils.set_file_settings("Parameters1", "bmp", str(self.bmp))             
            
        if self.qtObj.mapLoadinfo_checkBox.isChecked():
            self.mapLoadinfo = True
        else:
            self.mapLoadinfo = False
        utils.set_file_settings("Parameters1", "mapLoadinfo", str(self.mapLoadinfo))               
            
        if self.qtObj.mce_checkBox.isChecked():
            self.mce = True
        else:
            self.mce = False
        utils.set_file_settings("Parameters1", "mce", str(self.mce))             
            
        if self.qtObj.dx9single_checkBox.isChecked():
            self.dx9single = True
        else:
            self.dx9single = False
        utils.set_file_settings("Parameters1", "dx9single", str(self.dx9single))            

        if self.qtObj.forwardrenderer_checkBox.isChecked():
            self.forwardrenderer = True
        else:
            self.forwardrenderer = False
        utils.set_file_settings("Parameters1", "forwardrenderer", str(self.forwardrenderer)) 

        if self.qtObj.log_checkBox.isChecked():
            self.gw2Log = True
        else:
            self.gw2Log = False
        utils.set_file_settings("Parameters1", "log", str(self.gw2Log)) 

        if self.qtObj.nodelta_checkBox.isChecked():
            self.nodelta = True
        else:
            self.nodelta = False
        utils.set_file_settings("Parameters1", "nodelta", str(self.nodelta)) 

        if self.qtObj.nomusic_checkBox.isChecked():
            self.nomusic = True
        else:
            self.nomusic = False
        utils.set_file_settings("Parameters1", "nomusic", str(self.nomusic)) 

        if self.qtObj.noui_checkBox.isChecked():
            self.noui = True
        else:
            self.noui = False
        utils.set_file_settings("Parameters1", "noui", str(self.noui)) 

        if self.qtObj.nosound_checkBox.isChecked():
            self.nosound = True
        else:
            self.nosound = False
        utils.set_file_settings("Parameters1", "nosound", str(self.nosound)) 

        if self.qtObj.prefreset_checkBox.isChecked():
            self.prefreset = True
        else:
            self.prefreset = False
        utils.set_file_settings("Parameters1", "prefreset", str(self.prefreset)) 

        if self.qtObj.shareArchive_checkBox.isChecked():
            self.shareArchive = True
        else:
            self.shareArchive = False
        utils.set_file_settings("Parameters1", "shareArchive", str(self.shareArchive)) 

        if self.qtObj.uispanallmonitors_checkBox.isChecked():
            self.uispanallmonitors = True
        else:
            self.uispanallmonitors = False
        utils.set_file_settings("Parameters1", "uispanallmonitors", str(self.uispanallmonitors)) 

        if self.qtObj.useOldFov_checkBox.isChecked():
            self.useOldFov = True
        else:
            self.useOldFov = False
        utils.set_file_settings("Parameters1", "useOldFov", str(self.useOldFov)) 

        if self.qtObj.windowed_checkBox.isChecked():
            self.windowed = True
        else:
            self.windowed = False
        utils.set_file_settings("Parameters1", "windowed", str(self.windowed)) 

        if self.qtObj.umbra_checkBox.isChecked():
            self.umbra = True
        else:
            self.umbra = False
        utils.set_file_settings("Parameters1", "umbra", str(self.umbra)) 
                    
        self._set_all_configs_on_form_from_settings_file()
################################################################################
################################################################################
################################################################################
    def _set_parameters2(self):
        if self.qtObj.dat_checkBox.isChecked():
            if (self.datFile is not None) and (self.datFile != ""):
                self.useDatFile = True
            else:
                self.qtObj.dat_checkBox.setChecked(False)
                self.useDatFile = False
        else:
            self.qtObj.dat_checkBox.setChecked(False)
            self.useDatFile = False
        utils.set_file_settings("Parameters2", "usedatfile", str(self.useDatFile))
            
        if self.qtObj.verify_checkBox.isChecked():
            self.verify = True
        else:
            self.verify = False
        utils.set_file_settings("Parameters2", "verify", str(self.verify)) 
                
        if self.qtObj.repair_checkBox.isChecked():
            self.repair = True
        else:
            self.repair = False
        utils.set_file_settings("Parameters2", "repair", str(self.repair))  
        
        if self.qtObj.diag_checkBox.isChecked():
            self.diag = True
        else:
            self.diag = False
        utils.set_file_settings("Parameters2", "diag", str(self.diag))          
        
        if self.qtObj.uninstall_checkBox.isChecked():
            self.uninstall = True
        else:
            self.uninstall = False
        utils.set_file_settings("Parameters2", "uninstall", str(self.uninstall))           
        
        self._set_all_configs_on_form_from_settings_file()
################################################################################
################################################################################
################################################################################
    def _set_assetsrv(self):
        assetsrv_textEdit = str(self.qtObj.assetsrv_textEdit.toPlainText())
        if assetsrv_textEdit is not None and assetsrv_textEdit != "":
            self.assetsrv = assetsrv_textEdit
        else:
            self.assetsrv = ""
        utils.set_file_settings("Parameters2", "assetsrv", f"\"{self.assetsrv}\"")
        self._set_all_configs_on_form_from_settings_file()   
################################################################################
################################################################################
################################################################################
    def _set_authsrv(self):
        authsrv_textEdit = str(self.qtObj.authsrv_textEdit.toPlainText())
        if authsrv_textEdit is not None and authsrv_textEdit != "":
            self.authsrv = authsrv_textEdit
        else:
            self.authsrv = ""
        utils.set_file_settings("Parameters2", "authsrv", f"\"{self.authsrv}\"")
        self._set_all_configs_on_form_from_settings_file()       
################################################################################
################################################################################
################################################################################
    def _set_portal(self):
        portal_textEdit = str(self.qtObj.portal_textEdit.toPlainText())
        if portal_textEdit is not None and portal_textEdit != "":
            self.portal = portal_textEdit
        else:
            self.portal = ""
        utils.set_file_settings("Parameters2", "portal", f"\"{self.portal}\"")
        self._set_all_configs_on_form_from_settings_file()          
################################################################################
################################################################################
################################################################################
    def _set_port(self):
        if self.qtObj.port80_radioButton.isChecked():
            self.port = 80
        elif self.qtObj.port443_radioButton.isChecked():
            self.port = 443
        else:
            self.port = 6112
        utils.set_file_settings("GW2", "port", str(self.port))    
        self._set_all_configs_on_form_from_settings_file()       
################################################################################
################################################################################
################################################################################
    def _set_arcdps(self):
        self.qtObj.main_tabWidget.setCurrentIndex(2)
        if self.qtObj.arcdps_yes_radioButton.isChecked():
            self.arcdps = True
            self._update_arcdps()
        else:
            self.arcdps = False
            utils.remove_arcdps_files(self)
        utils.set_file_settings("GW2", "arcdps", str(self.arcdps))
################################################################################
################################################################################
################################################################################
    def _update_arcdps(self):
        gw2_dir_path        = os.path.dirname(self.gw2Path)
        d3d9_url            = constants.d3d9_url
        md5sum_url          = constants.md5sum_url
        buildTemplate_url   = constants.buildTemplate_url
        extras_url          = constants.extras_url      
        d3d9_path           = f"{gw2_dir_path}/bin64/d3d9.dll"
        template_path       = f"{gw2_dir_path}/bin64/d3d9_arcdps_buildtemplates.dll"
        extras_path         = f"{gw2_dir_path}/bin64/d3d9_arcdps_extras.dll"
        
        if str(self.arcdps).lower() == "true":
            arcdps_404_msg          = messages.arcdps_404
            arcdps_timeout_msg      = messages.arcdps_timeout
            arcdps_new_version_msg  = messages.arcdps_new_version
            arcdps_updating_msg     = messages.arcdps_updating
            arcdps_installing_msg   = messages.arcdps_installing
            
            if not os.path.exists(f"{gw2_dir_path}/bin64/"):
                os.makedirs(f"{gw2_dir_path}/bin64/") 
            
            if os.path.isfile(d3d9_path):
                self._disable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)
                
                try:
                    req_d3d9_md5 = ""
                    utils.show_progress_bar(self, arcdps_new_version_msg, 0)
                    req = requests.get(md5sum_url)
                    utils.show_progress_bar(self, arcdps_new_version_msg, 15)
                    if req.status_code == 200:
                        req_d3d9_md5 = str(req.text.split()[0])
                    else:
                        utils.show_message_box("error", arcdps_timeout_msg)
                        self.log.error(arcdps_timeout_msg)
                        utils.show_progress_bar(self, arcdps_updating_msg, 100)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)    
                        return
                #except Exception as e:
                except requests.exceptions.ConnectionError as e:
                    self.log.error(f"{e} {md5sum_url}")
                    utils.show_progress_bar(self, arcdps_updating_msg, 100)
                    self._enable_form()
                    self.qtObj.main_tabWidget.setCurrentIndex(2)
                    return                     
                    
                current_d3d9_md5 = utils.md5Checksum(d3d9_path)
                if req_d3d9_md5 != current_d3d9_md5:
                    utils.show_progress_bar(self, arcdps_updating_msg, 30)
                    utils.backup_arcdps_files(self, "backup")

                    #try d3d9_url
                    try:
                        utils.show_progress_bar(self, arcdps_updating_msg, 45)
                        urllib.request.urlretrieve(d3d9_url, d3d9_path)
                    except urllib.request.HTTPError as e:
                        utils.remove_arcdps_files(self)
                        utils.backup_arcdps_files(self, "revert_backup")
                        utils.show_message_box("error", arcdps_404_msg)
                        self.log.error(f"{e} {d3d9_url}")
                        utils.show_progress_bar(self, arcdps_updating_msg, 100)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)
                        return

                    #try buildTemplate_url
                    try:
                        urllib.request.urlretrieve(buildTemplate_url, template_path)
                        utils.show_progress_bar(self, arcdps_updating_msg, 60)       
                    except urllib.request.HTTPError as e:
                        utils.remove_arcdps_files(self)
                        utils.backup_arcdps_files(self, "revert_backup")
                        utils.show_message_box("error", arcdps_404_msg)
                        self.log.error(f"{e} {buildTemplate_url}")
                        utils.show_progress_bar(self, arcdps_updating_msg, 100)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)
                        return

                    #try extras_url
                    try:
                        urllib.request.urlretrieve(extras_url, extras_path)
                        utils.show_progress_bar(self, arcdps_updating_msg, 75)       
                    except urllib.request.HTTPError as e:
                        utils.remove_arcdps_files(self)
                        utils.backup_arcdps_files(self, "revert_backup")
                        utils.show_message_box("error", arcdps_404_msg)
                        self.log.error(f"{e} {extras_url}")
                        utils.show_progress_bar(self, arcdps_updating_msg, 100)
                        self._enable_form()
                        self.qtObj.main_tabWidget.setCurrentIndex(2)
                        return

                    utils.show_progress_bar(self, arcdps_updating_msg, 90)
                    utils.remove_arcdps_backup_files(self)
                    
                utils.show_progress_bar(self, arcdps_updating_msg, 100)
                self._enable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)
            else:
                utils.show_progress_bar(self, arcdps_installing_msg, 0)
                utils.remove_arcdps_files(self)
                arcdps_url = constants.arcdps_url
                self._disable_form()
                
                #check arcdps website is up
                try:
                    utils.show_progress_bar(self, arcdps_installing_msg, 15)
                    requests.get(arcdps_url)
                    utils.show_progress_bar(self, arcdps_installing_msg, 30)
                except requests.exceptions.ConnectionError as e:
                    self.log.error(f"{e} {arcdps_url}")
                    utils.show_progress_bar(self, arcdps_installing_msg, 100)
                    self._enable_form()
                    return
                
                #try d3d9_url
                try:
                    utils.show_progress_bar(self, arcdps_installing_msg, 40)
                    urllib.request.urlretrieve(d3d9_url, d3d9_path)
                    utils.show_progress_bar(self, arcdps_installing_msg, 50) 
                except urllib.request.HTTPError as e:
                    utils.remove_arcdps_files(self)
                    utils.show_message_box("error", arcdps_404_msg)
                    self.log.error(f"{e} {d3d9_url}")
                    
                #try buildTemplate_url
                try:
                    utils.show_progress_bar(self, arcdps_installing_msg, 60)
                    urllib.request.urlretrieve(buildTemplate_url, template_path)
                    utils.show_progress_bar(self, arcdps_installing_msg, 70)
                except urllib.request.HTTPError as e:
                    utils.remove_arcdps_files(self)
                    utils.show_message_box("error", arcdps_404_msg)
                    self.log.error(f"{e} {buildTemplate_url}")                    
                    
                #try extras_url
                try:
                    utils.show_progress_bar(self, arcdps_installing_msg, 80)
                    urllib.request.urlretrieve(extras_url, extras_path)
                    utils.show_progress_bar(self, arcdps_installing_msg, 90)
                except urllib.request.HTTPError as e:
                    utils.remove_arcdps_files(self)
                    utils.show_message_box("error", arcdps_404_msg)
                    self.log.error(f"{e} {extras_url}")                     
                    
                utils.show_progress_bar(self, arcdps_installing_msg, 100)
                self._enable_form()
                self.qtObj.main_tabWidget.setCurrentIndex(2)
################################################################################
################################################################################
################################################################################
    def _set_arcdps_tab(self):
        arcdps_url = constants.arcdps_url
        arcdps_ref = "<p align=\"left\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"\
                    +f"margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"{arcdps_url}"\
                    +f"\"><span style=\" font-size:9pt; text-decoration: underline; color:#FFFFFF;\">{arcdps_url}"\
                    +"</span></a></p>"
        
        self.qtObj.arcdps_disclamer_label.setText(messages.arcdps_disclamer)
        self.qtObj.arcps_url_textBrowser.setHtml(arcdps_ref)
        
        try:
            response = requests.get(arcdps_url)
            if response.status_code != 200: 
                self.log.error(messages.arcdps_error_dl)
            else:
                html = str(response.text)
                soup = BeautifulSoup(html, "html.parser")
                body = soup.body
                blist = str(body).split("<b>")
                
                for content in blist:
                    if content.startswith('changes'):
                        changes = content.replace("changes</b><br/>","").replace("<br/>","").replace("     ","")
                    if content.startswith('download'):
                        version = content.split("</a>")[1].split("<br/>")[0].strip(" (").strip(")")
                        
                self.qtObj.arcdps_webpage_textEdit.setPlainText(changes.strip())
                self.qtObj.arcdps_current_version_label.setText(version.strip())
        except requests.exceptions.ConnectionError as e:
            self.log.error(f"{messages.arcdps_unreacheable} {e}")
            utils.show_message_box("error", messages.arcdps_unreacheable)
            self.qtObj.arcdps_webpage_textEdit.setPlainText(messages.arcdps_unreacheable)
            self.qtObj.arcdps_current_version_label.setText("---")
################################################################################
################################################################################
################################################################################
    def _check_new_program_version(self):
        remote_version_filename = constants.remote_version_filename
        client_version = constants.VERSION
        program_new_version_msg = messages.checking_new_version
        
        try:
            utils.show_progress_bar(self, program_new_version_msg, 0)
            req = requests.get(remote_version_filename)
            utils.show_progress_bar(self, program_new_version_msg, 25)
            if req.status_code == 200: 
                req = req.json()
                encode_msg = str(req['content'])
                remote_version = str(base64.b64decode(encode_msg))
                remote_version = remote_version.replace("b","")
                remote_version = remote_version.replace("'","")
                
                utils.show_progress_bar(self, program_new_version_msg, 50)
                if remote_version[-2:] == "\\n" or remote_version[-2:] == "\n":
                    remote_version = remote_version[:-2] #getting rid of \n at the end of line
                
                utils.show_progress_bar(self, program_new_version_msg, 75)
                if remote_version != client_version:
                    utils.show_progress_bar(self, program_new_version_msg, 100)
                    new_version_window_title = f"Version {remote_version} available for download"
                    
                    msg = f"""{messages.new_version_available}
                        \nYour version: v{client_version}\nNew version: v{remote_version}
                        \n{messages.check_downloaded_dir}
                        \n{messages.confirm_download}"""
    
                    icon = QtWidgets.QMessageBox.Question
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setIcon(icon)
                    msgBox.setWindowTitle(new_version_window_title)
                    msgBox.setInformativeText(msg)
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    msgBox.setDefaultButton(QtWidgets.QMessageBox.Yes)
                    reply = msgBox.exec_()
    
                    if reply == QtWidgets.QMessageBox.Yes:
                        pb_dl_new_version_msg = messages.dl_new_version
                        program_url = constants.github_exe_program_url
                        user_download_path = utils.get_download_path()
                        downloaded_program_path = f"{user_download_path}\{constants.exe_program_name}"
                        
                        try:
                            utils.show_progress_bar(self, pb_dl_new_version_msg, 50)
                            urllib.request.urlretrieve(program_url, downloaded_program_path)
                            utils.show_progress_bar(self, pb_dl_new_version_msg, 100)
                            
                            utils.show_message_box("Warning", f"{messages.info_dl_new_version}\n{downloaded_program_path}")
                            sys.exit()
                        except Exception as e:
                            utils.show_progress_bar(self, pb_dl_new_version_msg, 100)
                            self.log.error(f"{messages.error_dl_new_version} {e}")
                            utils.show_message_box("error", messages.error_dl_new_version)
                    else:
                        new_title = f"{constants.FULL_PROGRAM_NAME} ({new_version_window_title})"
                        _translate = QtCore.QCoreApplication.translate
                        self.form.setWindowTitle(_translate("Main", new_title))
            else:
                utils.show_progress_bar(self, program_new_version_msg, 100)
                print(f"\n{messages.remote_version_file_not_found}\n")
        except requests.exceptions.ConnectionError as e:
            utils.show_progress_bar(self, program_new_version_msg, 100)
            self.log.error(f"{messages.dl_new_version_timeout} {e}")
            utils.show_message_box("error", messages.dl_new_version_timeout)
################################################################################
################################################################################
################################################################################
    def _start_gw2(self):
        program = str(self.gw2Path)
        working_directory = os.path.dirname(self.gw2Path)
        arguments = self.current_parameters_list
        myProcess = QtCore.QProcess()
        myProcess.setWorkingDirectory(working_directory)
        myProcess.setProgram(program)  
        myProcess.setArguments(arguments)
        myProcess.startDetached()
        myProcess.started.connect(self._gw2_process_started())
################################################################################
################################################################################
################################################################################
    def _gw2_process_started(self):
        self._disable_form()
        sleep(constants.exit_timer)
        sys.exit()    
################################################################################
################################################################################
################################################################################
