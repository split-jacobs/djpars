import json
import schedule
import time
from models.py import Table

def open():
	with open ('data_base.json', 'r') as file:
		data =json.load(file)
		
		
schedule.every().day.at('16:11').do(open)
	
while True:
	schedule.run_pending()
	time.sleep(1)