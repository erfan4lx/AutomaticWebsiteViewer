import sys
import os
import random
from selenium import webdriver
import requests
import time

banner = """                                                
  [[ye]]*   )                              (        
[[re]]` )  /(    )        (      )         )\    )  
 [[ye]]( )(_))( /(   (    )\    (      (  ((_)( /(  
[[re]](_(_()) )(_))  )\ )((_)   )\  '  )\  _  )(_)) 
[[gr]]|_   _|((_)_  _(_/( (_) _((_))  ((_)| |((_)_  
  [[gr]]| |  / _` || ' \))| || '  \()/ _ \| |/ _` | 
  |_|  \__,_||_||_| |_||_|_|_| \___/|_|\__,_|

  M4nifest0 Cyber Security Team [erfan4lx] 
  Unidentified Cyber Security Team [erfan4lx]
  Vortex Cyber Security Team [erfan4lx]
  
  github.com/erfan4lx  
  youtube.com/channel/UCHL7e6sD1eXIBIvjBYnXYEQ\n\n
"""
print(banner)
time.sleep(5)

def req(target_url,timeo,stay_time):
	try:
		driver=webdriver.Firefox()
		driver.set_page_load_timeout(timeo)
		driver.get(target_url)
		time.sleep(stay_time)
		driver.close()
	except:
		driver.close()

target=str(input("\033[1;33;40mEnter The Target URL(Ex: https://www.google.com) :"))
timeout=int(input("\033[1;33;40mEnter The Time Out(In Seconds) :"))
stay=int(input("\033[1;33;40mEnter The Stay Time(In Seconds) :"))

while True:
	req(target,timeout,stay)
	print("\033[1;32;40mSleeping For 5 Seconds")
	time.sleep(5)
