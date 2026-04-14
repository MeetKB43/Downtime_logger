from gpiozero import Button
from datetime import datetime
import time
import os
#from Python_Excel_API import save_to_excel
from supabase_API import record_DT

timer_running = False
start_time = None

print("Running... Waiting for DT")


while True:
	s = input("Enter input")
	
	#Timer Start Condition
	if s=="s" and not timer_running:
		start_time = datetime.now().replace(microsecond=0)
		timer_running = True
		print("Downtime Started")
		time.sleep(0.5)
		
	#Timer Stop Condition
	if s=="e" and timer_running:
		end_time = datetime.now().replace(microsecond=0)
		duration = int(((end_time - start_time).total_seconds())/60)
		print("Downtime recorded")
		print(f"Start time: {start_time} endtime: {end_time}")
		print(f"Duration: {duration}")
		if duration >= 5:
			record_DT(start_time, end_time, duration)
		timer_running = False
		start_time = None
		
		time.sleep(0.5)
	
	#Close loop
	if s=="t":
		break
	time.sleep(0.1)
