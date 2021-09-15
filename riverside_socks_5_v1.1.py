from selenium.webdriver.chrome.options import Options
from selenium import webdriver as Wee
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
import mysql.connector
#import wget
import os
import sys
import zipfile
import datetime
import warnings
import urllib.request


proxy_list = []
device_list=[]

#turning of the warnings 
warnings.simplefilter("ignore")



#cleaning screan function 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



url = "https://raw.githubusercontent.com/FardadAnsari/User_agent/main/user_agent_total.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	device_list.append(decoded_line)




url = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	proxy_list.append(decoded_line)
#print(len(proxy_list))



url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	proxy_list.append(decoded_line)


url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
file = urllib.request.urlopen(url)
for line in file:

	decoded_line = line.decode("utf-8")
	decoded_line=decoded_line.strip() 
	proxy_list.append(decoded_line)






certain=True


#get the time and date
now = datetime.datetime.now()

    
# main function for changing the ip

def Weemarket_openbrowser(PROXY,USERAGENT):
    option = Options()
    option.add_argument('--disable-infobars')
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument('--disable-web-security')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--allow-running-insecure-content')
    option.add_argument('lang=en')
    # Based of the type of porxy this argument will be change *** 
    option.add_argument("--proxy-server=socks5://%s" % PROXY)
    option.add_argument('--user-agent=%s' % USERAGENT)
    #option.add_argument('--headless')

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
  
    sleep(5)
    

    for ip in proxy_list:
        for device in device_list:
            now = datetime.datetime.now()

            if 14 <= now.hour and 22 >= now.hour:
                certain=True

                try:
        
                    s_1 = random.randint(2, 6)
                    sleep(s_1)
                    interact = Weemarket_openbrowser(ip,device)
                    interact.get(sys.argv[2])
                    sleep(15)
                    button = interact.find_element_by_class_name('orderNows')
                    button.click()
                    sleep(40)
                    print("I found the website")
                    sleep(int(sys.argv[3]))
                    count_s=count_s+1
                    visit = visit + 1
                    print("The total number of visits is  " + str(visit) + " !")
                    print(device)
                    interact.quit()
                    print(" Total number of successful interactions is "+str(count_s))

                except:
                    count_fail = count_fail + 1
                    print(" Total number of unsuccessful interactions is "+str(count_fail))
                    interact.quit()
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







