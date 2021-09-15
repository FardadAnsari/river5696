from selenium.webdriver.chrome.options import Options
from selenium import webdriver as Wee
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
import mysql.connector
import wget
import os
import sys
import zipfile
import datetime
import warnings
import urllib.request



# for turning the warning off 
warnings.simplefilter("ignore")



# defining function for cleaning cmd 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



#get the time and date
now = datetime.datetime.now()
proxy_list = []
device_list=[]
    

url = "https://raw.githubusercontent.com/FardadAnsari/User_agent/main/user_agent_total.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	device_list.append(decoded_line)







url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	proxy_list.append(decoded_line)
#print(len(proxy_list))

certain=True  


def visit_pp(PROXY,USERAGENT):
    option = Options()
    option.add_argument('--disable-infobars')
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument('lang=en')
    #option.add_argument('--log-level=OFF')
    option.add_argument("--proxy-server=%s" % PROXY)
    option.add_argument('--user-agent=%s' % USERAGENT)
    option.add_argument('--headless')

    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    chromedriver_path = "C:\chromedriver.exe"
    browser = Wee.Chrome(options=option, executable_path=chromedriver_path)

    return browser


count_s = 0
count_fail=0
visit = 0


  

while True:
    #print(sys.argv[1])
    for ip in proxy_list:
        for device in device_list:
            now = datetime.datetime.now()

            if 14 <= now.hour and 22 >= now.hour:
                certain=True

                try:
                    print(sys.argv[1])
                    s_1 = random.randint(2, 6)
                    sleep(s_1)
                    
                    interact = visit_pp(ip,device)
                    interact.get(sys.argv[2])
                    sleep(4)
                    button = interact.find_element_by_class_name('orderNows')
                    sleep(4)
                    button.click()
                    #sleep(4)
                    print("I found the website")
                    count_s = count_s + 1
                    visit = visit + 1
                    sleep(int(sys.argv[3]))
                    
                    print("The total number of visits is  " + str(visit) + " !")
                    print(device)
                    interact.quit()
                    print(" Interaction number " + str(count_s) + " was successful !")

                except:
                    
                    print(" Interaction number " + str(count_fail) + " was Unsuccessful !")
                    interact.quit()
                    count_fail=count_fail+1
                    print("Proxy has been Changed")
                    random.shuffle(proxy_list)
                    break


                # waiting for 3 hours
                sleep(20)
            else:

                while now.hour==int(sys.argv[4]) and certain:
                    mydb = mysql.connector.connect(
                        host="79.170.40.237",
                        user="cl22-data",
                        password="Wee%159125w$",
                        database="cl22-data"
                    )

                    sleep(5)

                    mycursor = mydb.cursor()
                    name=sys.argv[1]
                    domain=sys.argv[2]
                    date=str(now.date())
                    num_visit=str(visit)

                    sql = "INSERT INTO visitdatabaseFeb (shopid, name, domain, date, views) VALUES (%s, %s ,%s, %s , %s )"

                    val = (sys.argv[5], name , domain, date, num_visit)
                    mycursor.execute(sql, val)

                    mydb.commit()

                    print(mycursor.rowcount, "record inserted.")
                    print("Total Number of Successful Visits is "+ str(count_s))
                    visit=0
                    certain=False
                    break





    











