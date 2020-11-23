# Python-key-sequence-app-restarter
This script was designed originally to auto restart discord by typing out a key sequence like control key followed by d i s c. However the script is modular and you can auto restart any app.

# setup
1. git clone this repo
2. create a shortcut to main.py so that you can pin it to the start menu
3. Install python 3
4. install pynput module by opening cmd and type `pip install pynput`
3. in main.py edit the config

# config
Open main.py and config start at `################## Config ##########################`

useEscapeToExit allows you to press escape key to close the script

showKeysLogs shows info in the cmd window. Set this to False if not debugging.

### Add Your apps
adding apps current follows this template
```
yourApp = Trigger.Trigger("sequence"(letter you cant to press),True(start with left control?),'\"exe location',"exe name")
configs.append(yourApp)
```
Here is a firefox example
```
firefox = Trigger.Trigger("fire",True,'\"C:\\Program Files\\Mozilla Firefox\\firefox.exe',"firefox.exe")
configs.append(firefox)
```

# demonstation on youtube
coming soon
