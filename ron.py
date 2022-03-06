# ======================== #
def Logo_Awal():
    print("""
# ======================== #
# ======================== #
# = Created By Anonymous = #
# = Welcome Salam Santuy = #
# ======================== #
# ======================== #
    """, flush=True)
# ======================== #
Logo_Awal() # Logo Awal
# ======================== #

# ======================== #
from stem import Signal
from datetime import datetime
from pydub import AudioSegment
from selenium import webdriver
from stem.control import Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
# ======================== #
# pip3 install stem pydub SpeechRecognition selenium requests undetected-chromedriver==1.5.2
# ======================== #
import speech_recognition as sr
import undetected_chromedriver as uc
import random, urllib, os, sys, time, requests, urllib, pydub, re, json, stem.process
# ======================== #

# ======================== #
options = uc.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--headless') # Linux/Windows
options.add_argument('--no-sandbox') # Linux/Windows
options.add_argument('--headless=chrome') # Linux/Windows
#options.add_argument(f'--proxy-server=socks5://127.0.0.1:9050') # Linux/Windows
options.add_argument('--window-size=1366,768')
#options.add_extension('./ublock.crx')
driver = uc.Chrome(options=options)
# ======================== #

# ======================== #
driver.get('https://webmining.anlinotes.my.id')
wallet = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wallet"]')))
wallet.send_keys('86QH75AKHx8JALxRj7TkqvfNTvGZmLkUS1V7EosrG3CGPqA4vv7B229KC95aCGTFS4Up3e8maah8Y79t2gqP3NaBL8U32XD')
time.sleep(2)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start"]'))))
Loop = False
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hashes-per-second"]')))
    cek_hash = driver.find_element(By.XPATH, '//*[@id="hashes-per-second"]').text
    Loop = True
except Exception as e:
    print("GAGAL!")
if Loop:
  while True:
    time.sleep(10)
    print(f'Hash Kamu : {cek_hash} Hash')
# ======================== #
