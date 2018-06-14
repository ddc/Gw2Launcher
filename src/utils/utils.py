#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.5
#|*****************************************************
# # -*- coding: utf-8 -*-

import ast, sys, os, json
import logging, hashlib
from time import sleep
from src.utils import constants
from configparser import ConfigParser
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets
################################################################################
################################################################################
################################################################################
class Object():
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
################################################################################
################################################################################
################################################################################
def get_file_settings(section, config_name):
    settings_filename = constants.settings_filename
    parser = ConfigParser(allow_no_value=True)
    parser.read(settings_filename)
    try:
        value = ast.literal_eval(parser.get(section, config_name))
    except ValueError:
        value = parser.get(section, config_name)
    except SyntaxError:
        value = None
    return value
################################################################################
################################################################################
################################################################################
def set_file_settings(section, config_name, value):
    settings_filename = constants.settings_filename
    parser = ConfigParser(allow_no_value=True)
    parser.read(settings_filename)
    parser.set(section, config_name, value)
    with open(settings_filename, 'w') as configfile:
        parser.write(configfile)
################################################################################
################################################################################
################################################################################          
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger(__name__)
    stderr_hdlr = logging.StreamHandler(stream=sys.stdout)
    stderr_hdlr.setLevel(constants.LOG_LEVEL)
    stderr_hdlr.setFormatter(constants.LOG_FORMATTER)
    logger.addHandler(stderr_hdlr)
    if issubclass(exc_type, KeyboardInterrupt)\
    or issubclass(exc_type, EOFError):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.exception("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
################################################################################
################################################################################
################################################################################
def open_get_filename(self):
    filename = QFileDialog.getOpenFileName(None, 'Open file')[0]
    if filename is '':
        return ''
    else:
        return str(filename)
################################################################################
################################################################################
################################################################################   
def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
################################################################################
################################################################################
################################################################################ 
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
################################################################################
################################################################################
################################################################################            
def show_message_box(typeMsg, message):
    if typeMsg.lower() == "error":
        icon = QtWidgets.QMessageBox.Critical
    elif typeMsg.lower() == "warning":
        icon = QtWidgets.QMessageBox.Warning        
    else:
        icon = QtWidgets.QMessageBox.Information
        
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setWindowTitle(typeMsg.capitalize())
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()
################################################################################
################################################################################
################################################################################
def show_progress_bar(self, message, value):
    self.progressBar = QtWidgets.QProgressBar()
    _translate = QtCore.QCoreApplication.translate
    self.progressBar.setObjectName("progressBar")
    self.progressBar.setGeometry(QtCore.QRect(180, 150, 350, 25))
    self.progressBar.setMinimumSize(QtCore.QSize(350, 25))
    self.progressBar.setMaximumSize(QtCore.QSize(350, 25))
    self.progressBar.setSizeIncrement(QtCore.QSize(350, 25))
    self.progressBar.setBaseSize(QtCore.QSize(350, 25))
    self.progressBar.setMinimum(0)
    self.progressBar.setMaximum(100)
    self.progressBar.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
    self.progressBar.setFormat(_translate("Main",  message+"%p%"))
    self.progressBar.show()

    QtWidgets.QApplication.processEvents()
    self.progressBar.setValue(value)
    #sleep(3)
    
    if value == 100:
        self.progressBar.hide()
################################################################################
################################################################################
################################################################################    
    