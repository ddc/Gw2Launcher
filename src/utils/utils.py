#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.6
#|*****************************************************
# # -*- coding: utf-8 -*-

import ast, sys, os, json, base64
import logging, hashlib
from src.utils import constants, messages
from configparser import ConfigParser
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets
import ctypes.wintypes
import requests, urllib.request
################################################################################
################################################################################
################################################################################
class Object():
    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent=4)
    def toDict(self):
        jsonString = json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent=4)
        jsonDict = json.loads(jsonString)
        return jsonDict
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
    #except SyntaxError:
    #    value = None
    except Exception as e:
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
def get_my_documents_path():
    if constants.IS_WINDOWS:
        CSIDL_PERSONAL = 5 #My Documents
        SHGFP_TYPE_CURRENT = 0
         
        buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
         
        return str(buf.value)
    else:
        return str(os.path.expanduser("~/Documents"))
################################################################################
################################################################################
################################################################################    
def remove_arcdps_files(self):
    gw2_dir_path        = os.path.dirname(self.gw2Path)
    d3d9_path           = f"{gw2_dir_path}{constants.d3d9_path}"
    template_path       = f"{gw2_dir_path}{constants.template_path}"
    extras_path         = f"{gw2_dir_path}{constants.extras_path}"
    
    try:
        if os.path.isfile(d3d9_path):
            os.remove(d3d9_path)
        if os.path.isfile(template_path):
            os.remove(template_path)
        if os.path.isfile(extras_path):
            os.remove(extras_path)
        success = True
    except OSError as e:
        self.log.error(f"{e}")
        success = False
    
    return success
################################################################################
################################################################################
################################################################################
def remove_arcdps_backup_files(self):
    gw2_dir_path        = os.path.dirname(self.gw2Path)
    d3d9_bak_path       = f"{gw2_dir_path}{constants.d3d9_bak_path}"
    template_bak_path   = f"{gw2_dir_path}{constants.template_bak_path}"
    extras_bak_path     = f"{gw2_dir_path}{constants.extras_bak_path}" 

    try:
        if os.path.isfile(d3d9_bak_path):
            os.remove(d3d9_bak_path)
        if os.path.isfile(template_bak_path):
            os.remove(template_bak_path)
        if os.path.isfile(extras_bak_path):
            os.remove(extras_bak_path)
        success = True
    except OSError as e:
        self.log.error(f"{e}")
        success = False
    
    return success
################################################################################
################################################################################
################################################################################
def backup_arcdps_files(self, type_backup:str):
    gw2_dir_path        = os.path.dirname(self.gw2Path)
    d3d9_path           = f"{gw2_dir_path}{constants.d3d9_path}"
    template_path       = f"{gw2_dir_path}{constants.template_path}"
    extras_path         = f"{gw2_dir_path}{constants.extras_path}"
    d3d9_bak_path       = f"{gw2_dir_path}{constants.d3d9_bak_path}"
    template_bak_path   = f"{gw2_dir_path}{constants.template_bak_path}"
    extras_bak_path     = f"{gw2_dir_path}{constants.extras_bak_path}" 
        
    if type_backup == "backup":
        if os.path.isfile(d3d9_path):
            os.rename(d3d9_path, d3d9_bak_path) 
        if os.path.isfile(template_path):
            os.rename(template_path, template_bak_path) 
        if os.path.isfile(extras_path):
            os.rename(extras_path, extras_bak_path) 
    elif type_backup == "revert_backup":
        if os.path.isfile(d3d9_bak_path):
            os.rename(d3d9_bak_path, d3d9_path) 
        if os.path.isfile(template_bak_path):
            os.rename(template_bak_path, template_path) 
        if os.path.isfile(extras_bak_path):
            os.rename(extras_bak_path, extras_path)
################################################################################
################################################################################
################################################################################
def show_ok_window(self, icon, window_title:str, msg:str):
    #icons can be Information, Warning, Critical, Question
    #icon = QtWidgets.QMessageBox.Information
    if icon is None:
        icon = QtWidgets.QMessageBox.Information
    
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setWindowTitle(window_title)
    msgBox.setInformativeText(msg)
    
    if icon == QtWidgets.QMessageBox.Question:
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Yes)    
    else:
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
    
    reply = msgBox.exec_()
    return reply
################################################################################
################################################################################
################################################################################
def check_new_program_version(self):
    remote_version_filename = constants.remote_version_filename
    client_version = constants.VERSION
    program_new_version_msg = messages.checking_new_version
    
    try:
        show_progress_bar(self, program_new_version_msg, 0)
        req = requests.get(remote_version_filename)
        show_progress_bar(self, program_new_version_msg, 25)
        if req.status_code == 200: 
            remote_version = req.text
            
            show_progress_bar(self, program_new_version_msg, 50)
            if remote_version[-2:] == "\\n" or remote_version[-2:] == "\n":
                remote_version = remote_version[:-2] #getting rid of \n at the end of line
            
            show_progress_bar(self, program_new_version_msg, 75)
            if remote_version != client_version:
                show_progress_bar(self, program_new_version_msg, 100)
                
                icon = QtWidgets.QMessageBox.Question
                new_version_window_title = f"Version {remote_version} available for download"
                msg = f"""{messages.new_version_available}
                    \nYour version: v{client_version}\nNew version: v{remote_version}
                    \n{messages.check_downloaded_dir}
                    \n{messages.confirm_download}"""
                reply = show_ok_window(self, icon, new_version_window_title, msg)
            
                if reply == QtWidgets.QMessageBox.Yes:
                    pb_dl_new_version_msg = messages.dl_new_version
                    program_url = constants.github_exe_program_url
                    user_download_path = get_download_path()
                    downloaded_program_path = f"{user_download_path}\{constants.exe_program_name}"
                    
                    try:
                        show_progress_bar(self, pb_dl_new_version_msg, 50)
                        urllib.request.urlretrieve(program_url, downloaded_program_path)
                        show_progress_bar(self, pb_dl_new_version_msg, 100)
                        
                        show_message_box("Info", f"{messages.info_dl_completed}\n{downloaded_program_path}")
                        sys.exit()
                    except Exception as e:
                        show_progress_bar(self, pb_dl_new_version_msg, 100)
                        self.log.error(f"{messages.error_dl_new_version} {e}")
                        show_message_box("error", messages.error_dl_new_version)
                else:
                    new_title = f"{constants.full_program_name} ({new_version_window_title})"
                    _translate = QtCore.QCoreApplication.translate
                    self.form.setWindowTitle(_translate("Main", new_title))
            show_progress_bar(self, program_new_version_msg, 100)
        else:
            show_progress_bar(self, program_new_version_msg, 100)
            self.log.error(f"{messages.error_check_new_version}\n{messages.remote_version_file_not_found} code:{req.status_code}")
            icon = QtWidgets.QMessageBox.Critical
            window_title = "ERROR"
            msg = f"{messages.error_check_new_version}"        
            show_ok_window(self, icon, window_title, msg)
    except requests.exceptions.ConnectionError as e:
        show_progress_bar(self, program_new_version_msg, 100)
        self.log.error(f"{messages.dl_new_version_timeout} {e}")
        show_message_box("error", messages.dl_new_version_timeout)
################################################################################
################################################################################
################################################################################

