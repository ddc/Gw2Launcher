#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.5
#|*****************************************************
# # -*- coding: utf-8 -*-

import os
import sys
import platform
import logging
################################################################################
################################################################################
################################################################################
PROGRAM_NAME            = "Guild Wars 2 Utilities"
VERSION                 = 1.0
################################################################################
exit_timer              = 5
################################################################################
################################################################################
################################################################################
############### DO NOT CHANGE ANY OF THESE VARS BELLOW #########################
################################################################################
################################################################################
################################################################################
FULL_PROGRAM_NAME       = PROGRAM_NAME +" v"+str(VERSION)
exe_program_name        = "Gw2Utils.exe"
################################################################################
LOG_LEVEL               = logging.ERROR
LOG_FORMATTER           = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s',
                                            datefmt="[%d/%b/%Y %H:%M:%S]")
################################################################################
IS_WINDOWS              = os.name == "nt"
IS_MAC                  = sys.platform == "darwin"
IS_LINUX                = sys.platform == "linux"
IS_64BIT                = platform.machine().endswith("64")
PYTHON_OK               = sys.version_info >= (3,5)
################################################################################
gw2_executable_names    = ["Gw2-64.exe", "Gw2.exe"]
################################################################################
win_appdata_path        = os.getenv('APPDATA') #C:\Users\username\AppData\Roaming
program_path            = str(win_appdata_path + "/Gw2 Utils/")
data_path               = str(program_path + "data")
logs_path               = str(program_path + "logs")
################################################################################
settings_filename       = str(data_path + "/settings.ini")
style_qss_filename      = str(data_path + "/style.qss")
error_logs_filename     = str(logs_path + "/errors.log")
################################################################################
arcdps_url              = "http://www.deltaconnected.com/arcdps"
d3d9_url                = str(arcdps_url+"/x64/d3d9.dll")
md5sum_url              = str(arcdps_url+"/x64/d3d9.dll.md5sum")
buildTemplate_url       = str(arcdps_url+"/x64/buildtemplates/d3d9_arcdps_buildtemplates.dll")
github_exe_program_url  = "https://github.com/Hadesz1/Gw2Utils/raw/dev/dist/Gw2Utils.exe"
remote_version_filename = 'https://api.github.com/repos/Hadesz1/Gw2Utils/contents/VERSION'
################################################################################
