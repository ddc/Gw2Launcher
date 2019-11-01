#! /usr/bin/env python3
# |*****************************************************
# * Copyright         : Copyright (C) 2019
# * Author            : ddc
# * License           : GPL v3
# * Python            : 3.6
# |*****************************************************
# # -*- coding: utf-8 -*-

import os
import sys
import platform
import logging


PROGRAM_NAME = "Guild Wars 2 Launcher"
SHORT_PROGRAM_NAME = "Gw2Launcher"
VERSION = "2.2"
################################################################################
EXIT_TIMER = 5
################################################################################
FULL_PROGRAM_NAME = f"{PROGRAM_NAME} v{VERSION}"
EXE_PROGRAM_NAME = f"{SHORT_PROGRAM_NAME}.exe"
################################################################################
DATE_FORMATTER = "%b/%d/%Y"
TIME_FORMATTER = "%H:%M:%S"
LOG_LEVEL = logging.INFO  # INFO or DEBUG
LOG_FORMATTER = logging.Formatter('%(asctime)s:[%(levelname)s]:[%(filename)s:%(funcName)s:%(lineno)d]:%(message)s',
                                  datefmt=f"[{DATE_FORMATTER} {TIME_FORMATTER}]")
################################################################################
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
IS_LINUX = sys.platform == "linux"
IS_64BIT = platform.machine().endswith("64")
PYTHON_OK = sys.version_info >= (3, 6)
################################################################################
GW2_64_BIT_EXEC_NAME = ["Gw2-64.exe"]
################################################################################
APPDATA_PATH = os.getenv('APPDATA')  # returns AppData\Roaming. 'LOCALAPPDATA' == AppData\Local.
PROGRAM_PATH = f"{APPDATA_PATH}/{SHORT_PROGRAM_NAME}"
################################################################################
SETTINGS_FILENAME = f"{PROGRAM_PATH}/settings.ini"
STYLE_QSS_FILENAME = f"{PROGRAM_PATH}/style.qss"
ERROR_LOGS_FILENAME = f"{PROGRAM_PATH}/errors.log"
################################################################################
ARCDPS_URL = "http://www.deltaconnected.com/arcdps"
D3D9_URL = f"{ARCDPS_URL}/x64/d3d9.dll"
MD5SUM_URL = f"{ARCDPS_URL}/x64/d3d9.dll.md5sum"
GITHUB_EXE_PROGRAM_URL = f"https://github.com/ddc/{SHORT_PROGRAM_NAME}/releases/download/V{VERSION}/{EXE_PROGRAM_NAME}"
REMOTE_VERSION_FILENAME = f"https://raw.github.com/ddc/{SHORT_PROGRAM_NAME}/master/VERSION"
################################################################################
D3D9_PATH = "/bin64/d3d9.dll"
D3D9_BAK_PATH = "/bin64/d3d9.dll.bak"
