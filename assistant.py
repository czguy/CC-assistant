#by code cube
from ctypes import util
from bs4 import BeautifulSoup
import requests
import os
import passmanager
import dictutil

print("loading...")
##weather - adapted for specific country and website
def func_weather():
    urlwthr = "https://amindi.ge/en/"
    page = requests.get(urlwthr).text
    soup = BeautifulSoup(page, 'lxml')
    wd = soup.find_all("div", class_="weekDay")
    wt = soup.find_all("div", class_="degrees")
    weekday = []
    weather = []
    for day in wd:
        weekday.append(day.text.replace(" ", "").replace("\n",""))
    for weath in wt:
        weather.append(weath.text.replace(" ", "").replace("\n",""))
    #currency
    curcls = soup.find("tbody")
    currency =curcls.find_all("tr") 
    cur = []
    cursub = []
    print("\n")
    for curr in currency:
        cur.append(curr)
        for i in curr:
            cursub.append(i.text.replace(" ", "").replace("\n"," "))
    for j in cursub:
        if j == " ":
            continue
        if j == "%":
            print("\n")
        else:
            print(j[:10], end=" ")
 
    print("\n")
    #printing
    #print(weekday, '\n', weather)
    print(f"Now : {weather[0]}")
    print(f"{weekday[0]} : {weather[1]}")
    print(f"{weekday[1]} : {weather[2]}")
    print(f"{weekday[2]} : {weather[3]}")
    print(f"{weekday[3]} : {weather[4]}")
    print(f"{weekday[4]} : {weather[5]}")
    print("\n")
##clear screen (works for every os)
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
print("Made by Code Cube")
print("Alpha V1.0")
func_weather()

##input
print("/h or help to display help page")
def startassistant():
    while True:
        maininp = input("command-> ")
        if maininp == "/e" or maininp == "exit":
            quit()
        elif maininp == "/cls" or maininp == "clear":
            clear()
        elif maininp == "/sw" or maininp == "weather":
            func_weather()
        elif maininp == "/pm":
            passmanager.passman()
        elif maininp == "/dict":
            dictutil.dictutil()
        elif maininp == "":
            pass
        elif maininp == "/h" or maininp == "help":
            print(
        """
        CC assistant >> help page:

        /h or help - open this page
        /cls or clear - clear the screen
        /sw or weather - show the weather
        /pm - open password manager
        /dict - open dictionary
        /e or exit - exit from program      
        """)
        else:
            print("command doesn't exist!")