#Website blocker python file to use when running in background

import time
from datetime import datetime as dt

host_temp = r"C:\Users\Ban\Desktop\Udemy Python\003app\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts" #r at beginning instead of double \
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.animenewsnetwork.co.uk", "animenewsnetwork.co.uk", \
"www.amazon.co.uk", "amazon.co.uk"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
        print("Get back to coding!")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path,'r+') as file:
            content = file.readlines() #reads lines seperately
            file.seek(0) #goes back to the beginning
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #any lines after "original" file is deleted
        print("Party hard!")
    time.sleep(5) #sleep time in seconds
