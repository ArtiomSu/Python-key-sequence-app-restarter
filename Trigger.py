import subprocess
import os
import sys
import time

class Trigger:
	def __init__(self, sequence, use_ctrl, process_location, process_name):
		self.sequence = sequence
		self.sequence_counter = 0
		self.use_ctrl = use_ctrl
		self.ctrl_pressed = False
		self.process_name = process_name
		self.process_location = process_location
		self.start_the_process()

	def check_sequence(self, key):
		key_string = ""
		try:
			key_string = str(key.char)
		except AttributeError:
			key_string = str(key)

		if self.use_ctrl and self.sequence_counter == 0:
			# check first if ctrl is pressed
			if key_string == "Key.ctrl_l":
				self.ctrl_pressed = True
				return 0

		if self.use_ctrl and self.ctrl_pressed:
			# continue with the others
			if self.sequence[self.sequence_counter] == key_string:
				self.sequence_counter = self.sequence_counter + 1
			else:
				self.sequence_counter = 0
				self.ctrl_pressed = False

			if self.sequence_counter == len(self.sequence):
				self.sequence_counter = 0
				self.ctrl_pressed = False
				self.restart_the_process()

		#print(str(self.sequence_counter)+" "+str(key)+" "+self.sequence[self.sequence_counter]+" "+str(self.use_ctrl)+" "+str(self.ctrl_pressed))
	
	def kill_the_process(self):
		print("Killing "+self.process_name)
		os.system("taskkill /im "+self.process_name)

	def start_the_process(self):
		print("Starting "+self.process_name)
		self.process = subprocess.Popen(self.process_location,shell=False)

	def restart_the_process(self):
		print("Restarting "+self.process_name)
		self.kill_the_process()
		time.sleep(2)
		self.start_the_process()		