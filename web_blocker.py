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
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working Hours.. ")
        with open(hosts_path, 'r+' ) as file: #r+ can read/write
            content = file.read()
            for website in website_list:
                if website in content:
                    pass #dont want to do anything, so just pass
                else:
                    file.write("\t"+ redirect+" "+website+"\n")
    else: #now we need to delete those lines
        with open(hosts_path, 'r+' ) as file:
            content = file.readlines() #make it a list to check it against the list
            #When you are appending the pointer right in the beginning and replace from the beg
            file.seek(0)
            #no way to actually delete, just append them
            for line in content:
                #if any item in each line of the file is not in the website list
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #removes everything after the seek method
        print("Fun Hours...")
    time.sleep(5)
