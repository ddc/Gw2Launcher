#! /usr/bin/env python3
# |*****************************************************
# * Copyright         : Copyright (C) 2019
# * Author            : ddc
# * License           : GPL v3
# * Python            : 3.6
# |*****************************************************
# # -*- coding: utf-8 -*-

import sys
import os
import json
import logging
import hashlib
import datetime
from src.utils import constants, messages
import configparser
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtWidgets
import requests
import urllib.request

_date_formatter = "%b/%d/%Y"
_time_formatter = "%H:%M:%S"


class Object:
    def __init__(self):
        self.created = str(datetime.datetime.now().strftime(f"{_date_formatter} {_time_formatter}"))

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def toDict(self):
        json_string = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_dict = json.loads(json_string)
        return json_dict


################################################################################
def get_all_ini_file_settings(file_name: str):
    dictionary = {}
    parser = configparser.ConfigParser(delimiters='=', allow_no_value=True)
    parser.optionxform = str  # this wont change all values to lowercase
    parser._interpolation = configparser.ExtendedInterpolation()
    parser.read(file_name)
    for section in parser.sections():
        # dictionary[section] = {}
        for option in parser.options(section):
            try:
                value = parser.get(section, option).replace("\"", "")
            except Exception:
                value = None
            if value is not None and len(value) == 0:
                value = None

            # dictionary[section][option] = value
            dictionary[option] = value
    return dictionary


################################################################################
def set_all_ini_file_settings(filename: str, dict_values: dict):
    parser = configparser.ConfigParser(delimiters='=', allow_no_value=True)
    parser.optionxform = str  # this wont change all values to lowercase
    parser._interpolation = configparser.ExtendedInterpolation()
    parser.read(filename)
    for section in dict_values.keys():
        for option, value in dict_values[section].items():
            parser.set(section, option, value)
    try:
        with open(filename, 'w') as configfile:
            parser.write(configfile, space_around_delimiters=False)
    except configparser.DuplicateOptionError:
        return


################################################################################
# def get_file_settings(section: str, config_name: str):
#     filename = constants.SETTINGS_FILENAME
#     parser = configparser.ConfigParser(delimiters='=', allow_no_value=True)
#     parser.optionxform = str  # this wont change all values to lowercase
#     parser._interpolation = configparser.ExtendedInterpolation()
#     parser.read(filename)
#     try:
#         value = parser.get(section, config_name).replace("\"", "")
#     except Exception:
#         value = None
#     if value is not None and len(value) == 0:
#         value = None
#     return value


################################################################################
def set_file_settings(section: str, config_name: str, value):
    filename = constants.SETTINGS_FILENAME
    parser = configparser.ConfigParser(delimiters='=', allow_no_value=True)
    parser.optionxform = str  # this wont change all values to lowercase
    parser._interpolation = configparser.ExtendedInterpolation()
    parser.read(filename)
    parser.set(section, config_name, value)
    try:
        with open(filename, 'w') as configfile:
            parser.write(configfile, space_around_delimiters=False)
    except configparser.DuplicateOptionError:
        return


################################################################################
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger(__name__)
    stderr_hdlr = logging.StreamHandler(stream=sys.stdout)
    stderr_hdlr.setLevel(constants.LOG_LEVEL)
    stderr_hdlr.setFormatter(constants.LOG_FORMATTER)
    logger.addHandler(stderr_hdlr)
    if issubclass(exc_type, KeyboardInterrupt) \
            or issubclass(exc_type, EOFError):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.exception("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


################################################################################
def open_get_filename():
    filename = QFileDialog.getOpenFileName(None, 'Open file')[0]
    if filename == '':
        return ''
    else:
        return str(filename)


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
    self.progressBar.setFormat(_translate("Main", message + "%p%"))
    self.progressBar.show()
    QtWidgets.QApplication.processEvents()
    self.progressBar.setValue(value)
    # sleep(3)
    if value == 100:
        self.progressBar.hide()


################################################################################
def remove_arcdps_files(self):
    gw2_dir_path = os.path.dirname(self.configs['gw2Path'])
    d3d9_path = remove_file(self, f"{gw2_dir_path}{constants.D3D9_PATH}")
    return True if d3d9_path else False


################################################################################
def remove_arcdps_backup_files(self):
    gw2_dir_path = os.path.dirname(self.configs['gw2Path'])
    d3d9_bak = remove_file(self, f"{gw2_dir_path}{constants.D3D9_BAK_PATH}")
    return True if d3d9_bak else False


################################################################################
def remove_file(self, file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        success = True
    except OSError as e:
        self.log.error(f"{e}")
        success = False
    return success


################################################################################
def backup_arcdps_files(self, type_backup: str):
    gw2_dir_path = os.path.dirname(self.configs['gw2Path'])
    d3d9_path = f"{gw2_dir_path}{constants.D3D9_PATH}"
    d3d9_bak_path = f"{gw2_dir_path}{constants.D3D9_BAK_PATH}"

    if type_backup == "backup":
        if os.path.isfile(d3d9_path):
            os.rename(d3d9_path, d3d9_bak_path)
    elif type_backup == "revert_backup":
        if os.path.isfile(d3d9_bak_path):
            os.rename(d3d9_bak_path, d3d9_path)


################################################################################
def show_message_window(windowType: str, window_title: str, msg: str):
    if windowType.lower() == "error":
        icon = QtWidgets.QMessageBox.Critical
    elif windowType.lower() == "warning":
        icon = QtWidgets.QMessageBox.Warning
    elif windowType.lower() == "question":
        icon = QtWidgets.QMessageBox.Question
    else:
        icon = QtWidgets.QMessageBox.Information

    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setWindowTitle(window_title)
    msgBox.setInformativeText(msg)

    if windowType.lower() == "question":
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Yes)
    else:
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)

    user_answer = msgBox.exec_()
    return user_answer


################################################################################
def check_new_program_version(self):
    remote_version_filename = constants.REMOTE_VERSION_FILENAME
    obj_return = Object()
    obj_return.new_version_available = False
    obj_return.new_version = None

    try:
        req = requests.get(remote_version_filename)
        if req.status_code == 200:
            remote_version = req.text

            if remote_version[-2:] == "\\n" or remote_version[-2:] == "\n":
                remote_version = remote_version[:-2]  # getting rid of \n at the end of line

            if float(remote_version) == float(self.client_version):
                obj_return.new_version_available = True
                obj_return.new_version_msg = f"Version {remote_version} available for download"
                obj_return.new_version = float(remote_version)
        else:
            self.log.error(
                f"{messages.error_check_new_version}\n{messages.remote_version_file_not_found} code:{req.status_code}")
            show_message_window("critical", "ERROR", f"{messages.error_check_new_version}")
    except requests.exceptions.ConnectionError as e:
        self.log.error(f"{messages.dl_new_version_timeout} {e}")
        show_message_window("error", "ERROR", messages.dl_new_version_timeout)
    finally:
        return obj_return


################################################################################
def download_new_program_version(self, show_dialog=True):
    if show_dialog:
        msg = f"""{messages.new_version_available}
                            \nYour version: v{self.client_version}\nNew version: v{self.new_version}
                            \n{messages.check_downloaded_dir}
                            \n{messages.confirm_download}"""
        reply = show_message_window("question", self.new_version_msg, msg)

        if reply == QtWidgets.QMessageBox.No:
            new_title = f"{constants.FULL_PROGRAM_NAME} ({self.new_version_msg})"
            _translate = QtCore.QCoreApplication.translate
            self.form.setWindowTitle(_translate("Main", new_title))
            return

    user_download_path = get_download_path()
    program_url = f"{constants.GITHUB_EXE_PROGRAM_URL}{self.new_version}/{constants.EXE_PROGRAM_NAME}"
    downloaded_program_path = f"{user_download_path}\\{constants.EXE_PROGRAM_NAME}"
    dl_new_version_msg = messages.dl_new_version

    try:
        show_progress_bar(self, dl_new_version_msg, 50)
        urllib.request.urlretrieve(program_url, downloaded_program_path)
        show_progress_bar(self, dl_new_version_msg, 100)
        show_message_window("Info", "INFO", f"{messages.info_dl_completed}\n{downloaded_program_path}")
        sys.exit()
    except Exception as e:
        show_progress_bar(self, dl_new_version_msg, 100)
        self.log.error(f"{messages.error_check_new_version} {e}")
        if e.code == 404:
            show_message_window("error", "ERROR", messages.remote_file_not_found)
        else:
            show_message_window("error", "ERROR", messages.error_check_new_version)
