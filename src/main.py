from gpiozero import Button
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from supabase_API import record_DT

Filler_Running_PIN: int = os.getenv("GPIO_Filler_Running_PIN")
timer_running = False
start_time = None
Filler_running = Button(Filler_Running_PIN,pull_down = True)

print("Running... Waiting for DT")


while True:
	#Timer Start Condition
	if not Filler_running.is_pressed and not timer_running:
		start_time = datetime.now().replace(microsecond=0)
		timer_running = True
		print("Downtime Started")
		time.sleep(0.5)
		
	#Timer Stop Condition
	if Filler_running.is_pressed and timer_running:
		end_time = datetime.now().replace(microsecond=0)
		duration = int(((end_time - start_time).total_seconds())/60)
		print("Downtime recorded")
		print(f"Start time: {start_time} endtime: {end_time}")
		print(f"Duration: {duration}")
		if duration >= 0:
			record_DT(start_time, end_time, duration)
		timer_running = False
		start_time = None
		
		time.sleep(0.5)
