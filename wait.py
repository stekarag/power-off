import os
import datetime
from dateutil.relativedelta import relativedelta
import time

test = 1
while (test == 1):
	try:
		count = input("Wait for how many minutes until shutdown? ")
		sec = int(count)*60
		s_down = datetime.datetime.today() + relativedelta(seconds=+sec)
		print("System going down at %s"%s_down)
		time.sleep(sec)
		test = 0
	except ValueError as e:
		print(e)
		print("Enter a number ")
	except AttributeError as e:
		print(e)
		print("Enter a number ")

os.system("Shutdown /s /t 0")
