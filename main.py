from pynput.keyboard import Key, Listener
import atexit
import signal
import sys
import Trigger

configs = []
################## Config ##########################
useEscapeToExit = False
showKeysLogs = True
#### Your Apps ####
discord = Trigger.Trigger("disc",True,'\"C:\\Users\\Fuking useless shit\\AppData\\Local\\Discord\\Update.exe\" --processStart Discord.exe',"Discord.exe")
configs.append(discord)
firefox = Trigger.Trigger("fire",True,'\"C:\\Program Files\\Mozilla Firefox\\firefox.exe',"firefox.exe")
configs.append(firefox)
####################################################

def on_press(key):
	global configs
	for trigger in configs:
  		trigger.check_sequence(key)
	if key == Key.esc and useEscapeToExit:
		return False
	if showKeysLogs:
		print(str(key))	

def main():
	with Listener(on_press=on_press) as listener:
		listener.join()			

@atexit.register  
def goodbye():  
	for trigger in configs:
		trigger.kill_the_process()
	sys.exit()

signal.signal(signal.SIGABRT, goodbye)    

if __name__ == '__main__':
	main()

