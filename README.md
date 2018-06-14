# Guild Wars 2 Utilities by [Hadesz#1223](mailto:hadesz456@gmail.com)

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?style=plastic)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=CTYZ8TK5MJV76)
[<img src="https://img.shields.io/github/license/Hadesz1/Gw2Utils.svg?style=plastic">](https://github.com/Hadesz1/Gw2Utils/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.5-blue.svg?style=plastic)](https://www.python.org/downloads/)
[![GitHub release](https://img.shields.io/github/release/Hadesz1/Gw2Utils.svg?style=plastic)](https://github.com/Hadesz1/Gw2Utils/releases/latest)

## Download
+ [Latest Release](https://github.com/Hadesz1/Gw2Utils/releases/latest)

## Program Notes
+ Configuration, logs and database files will be saved inside "Documents/Gw2Utils"
    + "Documents/Gw2Utils/config/"
    + "Documents/Gw2Utils/data/"
    + "Documents/Gw2Utils/logs/"

## Requirements
+ [Python 3.5](https://www.python.org/downloads/)
+ [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
    
## Requirements to Compile
+ [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html)

## Steps to Compile
+ Make sure python3 is your default (linux)
    + python --version (to check the python version)
+ Install PyInstaller through pip as admin/root:
    + pip install --upgrade pyinstaller requests urllib3
+ Execute the program at least once with python3:
    + python main.py
+ Execute python3 and call PyInstaller as a module to compile with python optmizations:
    + python -O -m PyInstaller -y -F Gw2Utils.spec
    
+ Executable file will be inside the "dist" directory as "Gw2Utils.exe"

## Notes
+ PyInstaller is only needed to create the executable file. Python scripts don't need to be compiled to be usable, just run the main.py to launch the program itself.
+ The format/extension of the executable will depend on which operating system you used for compilation. For example, if you run the PyInstaller command on windows the executable file will be .exe. If you run it on Linux the extension will depend on the distribution you are using.
+ For example, it is not possible to create a Windows executable (.exe) by directly running a Pyinstaller command on a Linux Distribution and vice versa.

## Acknowledgements
+ [QT5](https://www.qt.io)
+ [Python](https://www.python.org/downloads/)
+ [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
+ [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html)
+ [Guild Wars 2](https://www.guildwars2.com/en/)

## License
Released under the [GNU GPL v3](LICENSE).

## Buy me a cup of coffee
This program is open source and always will be, even if I don't get donations. That said, I know there are people out there that may still want to donate just to show their appreciation so this is for you guys. Thanks in advance!

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=CTYZ8TK5MJV76)
