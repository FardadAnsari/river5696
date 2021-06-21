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



# x=input("Enter a directory name--->")
# print("\n")
# y=input("Enter domain of a simple Wee web as it is in address bar including https--->")
# print("\n")
# z=input("Sleep-time on page--->")
# print("\n")
# p=input("Enter the sending hour to database---->")
# print("\n")
# q=input("Shop id of the shop---->")
# print("\n")


certain=True


#get the time and date
now = datetime.datetime.now()
path = os.getcwd()
# current_day=now.day

# if len(sys.argv) > 5 :
#     print("You have entered too many arguments !")
#     sys.exit()
#
# if len(sys.argv)==5:


try:
    path = os.getcwd()
    os.mkdir(path + "/"+sys.argv[1])
    print(path)

except :
    os.remove(path + "/"+sys.argv[1]+"/proxy.txt")
    pass
# main function for changing the ip

def Weemarket_openbrowser(PROXY,USERAGENT):
    option = Options()
    option.add_argument('--disable-infobars')
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument('lang=en')
    option.add_argument("--proxy-server=%s" % PROXY)
    option.add_argument('--user-agent=%s' % USERAGENT)
    option.add_argument('--headless')

    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    chromedriver_path = "C:\chromedriver.exe"
    browser = Wee.Chrome(options=option, executable_path=chromedriver_path)

    return browser


count = 0
visit = 0



while True:

    # Download the proxy form github
    wget.download('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
                  path+"/"+sys.argv[1]+"/proxy.txt")
    sleep(5)
    proxy_list = []
    device_list=[]
    # adding all proxy address to a list
    for ip in open(path+"/"+sys.argv[1]+"/proxy.txt"):
        proxy_list.append(ip)

    for user_agent in open(path+"/device.txt"):
        device_list.append(user_agent)


    for ip in proxy_list:
        for device in device_list:
            now = datetime.datetime.now()

            if 14 <= now.hour and 22 >= now.hour:
                certain=True

                try:
                    s_1 = random.randint(2, 6)
                    sleep(s_1)
                    count = count + 1
                    interact = Weemarket_openbrowser(ip,device)

                    interact.get(sys.argv[2])
                    sleep(4)
                    button = interact.find_element_by_class_name('mobile')
                    button.click()
                    sleep(4)
                    print("I found the website")
                    sleep(int(sys.argv[3]))
                    visit = visit + 1
                    print("The total number of visits is  " + str(visit) + " !")
                    print(device)
                    interact.quit()
                    print(" Interaction number " + str(count) + " was successful !")

                except:
                    print(" Interaction number " + str(count) + " was Unsuccessful !")
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
                    visit=0
                    certain=False
                    break





    os.remove(path+"/"+sys.argv[1]+"/proxy.txt")



