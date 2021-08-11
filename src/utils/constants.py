# * Copyright         : Copyright (C) 2019
# * Author            : ddc
# * License           : GPL v3
# * Python            : 3.6
# # -*- coding: utf-8 -*-

import logging
import os


PROGRAM_NAME = "Guild Wars2 Launcher"
SHORT_PROGRAM_NAME = "Gw2Launcher"
VERSION = "3.1"
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
################################################################################
GW2_64_BIT_EXEC_NAME = "Gw2-64.exe"
################################################################################
APPDATA_PATH = os.getenv('APPDATA')  # returns AppData\Roaming. 'LOCALAPPDATA' == AppData\Local.
PROGRAM_PATH = os.path.join(APPDATA_PATH, SHORT_PROGRAM_NAME)
################################################################################
SETTINGS_FILENAME = os.path.join(PROGRAM_PATH, 'settings.ini')
STYLE_QSS_FILENAME = os.path.join(PROGRAM_PATH, 'style.qss')
ERROR_LOGS_FILENAME = os.path.join(PROGRAM_PATH, 'errors.log')
D3D9_PATH = os.path.join('\\bin64', 'd3d9.dll')
D3D9_BAK_PATH = os.path.join('\\bin64', 'd3d9.dll.bak')
################################################################################
ARCDPS_URL = "https://www.deltaconnected.com/arcdps"
D3D9_URL = f"{ARCDPS_URL}/x64/d3d9.dll"
MD5SUM_URL = f"{ARCDPS_URL}/x64/d3d9.dll.md5sum"
GITHUB_EXE_PROGRAM_URL = f"https://github.com/ddc/{SHORT_PROGRAM_NAME}/releases/download/v"
REMOTE_VERSION_FILENAME = f"https://raw.github.com/ddc/{SHORT_PROGRAM_NAME}/master/VERSION"
PAYPAL_REMOTE_FILENAME = f"https://raw.github.com/ddc/{SHORT_PROGRAM_NAME}/master/src/images/paypal.png"
PAYPAL_URL = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=CTYZ8TK5MJV76"
GITHUB_LATEST_VERSION_URL = f"https://github.com/ddc/{SHORT_PROGRAM_NAME}/releases/latest"
################################################################################
