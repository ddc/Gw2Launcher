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
################################################################################
################################################################################
################################################################################
class CreateFiles():
    def __init__(self, log):
        self.log = log
################################################################################
################################################################################
################################################################################
    def create_settings_file(self):
        file = open(constants.settings_filename, encoding="utf-8", mode="w")
        file.write("""; DO NOT OPEN THIS FILE WITH NOTEPAD.
; Use Notepad++ or any other modern text editor.
; Use True or False.

[GW2]
gw2Path = ""
port = 6112
arcdps = False 

[Parameters1]
autologin = False
32bits = False
bmp = False
mapLoadinfo = False
mce = False
dx9single = False
forwardrenderer = False
log = False
nodelta = False
nomusic = False
noui = False
nosound = False
prefreset = False
shareArchive = False
uispanallmonitors = False
useOldFov = False
windowed = False
umbra = False

[Parameters2]
assetsrv = ""  
authsrv = ""  
portal = ""  
datFile = ""  
useDatFile = False  
verify = False  
copydat = False  
repair = False  
diag = False
uninstall = False  
""")
        file.close()        
################################################################################
################################################################################
################################################################################
    def create_style_file(self):
        file = open(constants.style_qss_filename, encoding="utf-8", mode="w")
        file.write("""
QWidget {
   background-color: #222222;
}

QWidget:disabled {
    color: #f5f5f5;
    background-color: #222222;
}

QLabel:disabled,
QCheckBox:disabled,
QRadioButton:disabled,
QGroupBox:disabled,
QTabBar:disabled
{
    color: #828282;
    padding: 3px;
    outline: none;
    background-color: transparent;
}

QLineEdit,
QLabel,
QCheckBox,
QRadioButton,
QGroupBox,
QtWidgets  {
    color: #FFFFFF;
}

QDialogButtonBox {
    button-layout: 0;
}

QTextEdit {
    color: #FFFFFF;
    background-color: #222222;
    border: 1px transparent #FFFFFF;
    padding: 0px;
    margin: 0px;
}

QPlainTextEdit {
    color: #FFFFFF;
    background-color: #222222;
    border-radius: 2px;
    border: 1px solid #b6b6b6;
    padding: 0px;
    margin: 0px;
}

/* QPushButton */

QPushButton {
   background-color: #8b0000;
   color: #000000;
   border-radius: 5px;
   border-style: none;
   height: 25px;
   font-weight: bold;
}

QPushButton:hover {
   background-color: #8b0000;
   color: #ffffff;
}

QPushButton:pressed {
   background-color: #000000;
   color: #8b0000;
   border-radius: 5px;
   border-style: none;
   height: 25px;
   font-weight: bold;
}

/* QTabWidget */

QTabWidget{
    border: 1px transparent #FFFFFF;
}

QTabWidget:focus {
    border: 1px transparent #FFFFFF;
}

QTabWidget::tab-bar {
    alignment: center;
    border: 1px transparent #FFFFFF;
}

/* QTabBar */

QTabBar::tab {
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #cccccc, stop: 1.0 #ffffff);;
    border:1px solid grey;
    border-top-left-radius:12px;
    border-top-right-radius:12px;
    padding:4px;
}

QTabBar::tab:selected {
    border-bottom: 1px transparent #FFFFFF;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #8b0000, stop: 1.0 #ffffff);
}

/* QProgressBar */

QProgressBar,
QProgressBar:horizontal {
    background: #bdc1c9;
    border: 1px solid #b6b6b6;
    text-align: center;
    padding: 1px;
    border-radius: 4px;
}
QProgressBar::chunk,
QProgressBar::chunk:horizontal {
    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #3874f2, stop:1 #5e90fa);
    border-radius: 3px;
}

/* QRadioButton */

QRadioButton::indicator:checked {
    background-color:#8b0000;
    border:1px solid black;
    border-radius: 8px;
}

QRadioButton::indicator:unchecked {
    background-color:#ffffff;
    border:1px solid black;
    border-radius: 8px;
}

/* QCheckBox */

QCheckBox::indicator:checked {
    background-color:#8b0000;
    border:1px solid black;
}

QCheckBox::indicator:unchecked {
    background-color:#ffffff;
    border:1px solid black;
}

/* QScrollBar */

QScrollBar::down-arrow:horizontal{background: none;display:none;}
QScrollBar::up-arrow:horizontal{background: none;display:none;}
QScrollBar::add-page:horizontal{background: none;display:none;}
QScrollBar::sub-page:horizontal{background: none;display:none;}

QScrollBar::up-arrow:vertical{background: none;display:none;} 
QScrollBar::down-arrow:vertical{background: none;display:none;}
QScrollBar::add-page:vertical{background: none;display:none;}
QScrollBar::sub-page:vertical{background: none;display:none;}

QScrollBar:horizontal {
    height: 15px;
    margin: 3px 15px 3px 15px;
    border: 1px transparent #3A3939;
    border-radius: 4px;
    background-color: #3A3939;
}

QScrollBar::handle:horizontal {
    background-color: #b6b6b6;
    min-width: 5px;
    border-radius: 4px;
}

QScrollBar::add-line:horizontal {
    margin: 1px 3px 0px 3px;
    width: 6px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    margin: 1px 3px 0px 3px;
    height: 10px;
    width: 6px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,
QScrollBar::sub-line:horizontal:hover,
QScrollBar::up-arrow:horizontal,
QScrollBar::down-arrow:horizontal {
    background: none;
}

QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:vertical {
    background-color: #3A3939;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #3A3939;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background-color: #b6b6b6;
    min-height: 5px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical {
    margin: 3px 0px 3px 1px;
    height: 6px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    margin: 3px 0px 3px 1px;
    height: 6px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,
QScrollBar::add-line:vertical:hover,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    background: none;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}
""")
        file.close()  
################################################################################
################################################################################
################################################################################        
        