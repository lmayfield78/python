import schedule
import time
from tools import status_code


# http://web.ics.purdue.edu/~jinsuh/analyticspractice-webscrape-schedule.php
# https://pypi.python.org/pypi/schedule

def hourly():
    '''
    This function will run continuously every hour.
    It will run the status code function verifying
    all urls for specific status codes. 

    '''
    print("checking @ " + time.strftime("%H:%M:%S \n"))
    status_code.status_200_check()



schedule.every(1).hour.do(hourly)

while True:
    schedule.run_pending()
    time.sleep(1)



