import time
from datetime import datetime as dt #have a short name so easier to ref

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list =["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

#want these four websites at 8am to be added to hosts
#remove it when its passes a certain time 
#so use a while loop

#to compare dates use dt.now() and create a new dt object
# dt.now() < dt(2016,5,5,8)  => False

#use variables in dt.now so its always true

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours.. ")
    else:
        print("Fun Hours")
    time.sleep(5)
