#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2018
# * Author            : Hadesz#1223 (discord)
# * E-Mail            : hadesz456@gmail.com
# * License           : GPL v3
# * Python            : 3.6
#|*****************************************************
# # -*- coding: utf-8 -*-

import os
import sys
import platform
import logging
from src.utils import utils
################################################################################
################################################################################
################################################################################
PROGRAM_NAME            = "Guild Wars 2 Utilities"
VERSION                 = 1.9
################################################################################
exit_timer              = 5
################################################################################
################################################################################
################################################################################
############### DO NOT CHANGE ANY OF THESE VARS BELLOW #########################
################################################################################
################################################################################
################################################################################
FULL_PROGRAM_NAME       = f"{PROGRAM_NAME} v{VERSION}"
exe_program_name        = "Gw2Utils.exe"
################################################################################
date_formatter          = "%b/%d/%Y"
time_formatter          = "%H:%M:%S"
LOG_LEVEL               = logging.INFO
LOG_FORMATTER           = logging.Formatter('%(asctime)s:[%(levelname)s]:[%(filename)s:%(funcName)s:%(lineno)d]:%(message)s',
                                datefmt=f"[{date_formatter} {time_formatter}]")
################################################################################
IS_WINDOWS              = os.name == "nt"
IS_MAC                  = sys.platform == "darwin"
IS_LINUX                = sys.platform == "linux"
IS_64BIT                = platform.machine().endswith("64")
PYTHON_OK               = sys.version_info >= (3,6)
################################################################################
gw2_64_bit_exec_name    = ["Gw2-64.exe"]
################################################################################
my_docs_path            = str(utils.get_my_documents_path())
program_path            = f"{my_docs_path}/Gw2Utils"
#data_path               = f"{program_path}/data"
#logs_path               = f"{program_path}/logs"
################################################################################
settings_filename       = f"{program_path}/settings.ini"
style_qss_filename      = f"{program_path}/style.qss"
error_logs_filename     = f"{program_path}/errors.log"
################################################################################
arcdps_url              = "http://www.deltaconnected.com/arcdps"
d3d9_url                = f"{arcdps_url}/x64/d3d9.dll"
md5sum_url              = f"{arcdps_url}/x64/d3d9.dll.md5sum"
buildTemplate_url       = f"{arcdps_url}/x64/buildtemplates/d3d9_arcdps_buildtemplates.dll"
extras_url              = f"{arcdps_url}/x64/extras/d3d9_arcdps_extras.dll"
github_exe_program_url  = f"https://github.com/Hadesz1/Gw2Utils/releases/download/{VERSION}/Gw2Utils.exe"
remote_version_filename = "https://api.github.com/repos/Hadesz1/Gw2Utils/contents/VERSION"
################################################################################
d3d9_path               = "/bin64/d3d9.dll"
d3d9_bak_path           = "/bin64/d3d9.dll.bak"
template_path           = "/bin64/d3d9_arcdps_buildtemplates.dll"
template_bak_path       = "/bin64/d3d9_arcdps_buildtemplates.dll.bak"
extras_path             = "/bin64/d3d9_arcdps_extras.dll"
extras_bak_path         = "/bin64/d3d9_arcdps_extras.dll.bak"     
################################################################################
