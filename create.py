#!/bin/bash

import sys
import os
import time
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from crypto import *
from selenium.webdriver.support.ui import WebDriverWait

path = "/Desktop/Testing/WebCrawlerDrivers/chromedriver"
username = str('USERNAME')

decryption()
global passw
with open('new-password.txt', 'r') as passwords:
	passw = passwords.readline()

def create():
	with Chrome() as browser:
		browser.get('http://github.com/login')
		loginArea = browser.find_element_by_xpath("//*[@id='login_field']")
		loginArea.send_keys(username + Keys.TAB)
		passwdArea = browser.find_element_by_xpath("//*[@id='password']")
		passwdArea.send_keys(passw + Keys.ENTER)
		os.remove('new-password.txt')
		browser.get('https://github.com/new')
		repoName = raw_input("Whats The Repo Name?: ")
		folderName = str(repoName)
		repoNamein = browser.find_element_by_xpath("//*[@id='repository_name']")
		repoNamein.send_keys(folderName)
		readme = browser.find_element_by_xpath("//*[@id='repository_auto_init']")
		readme.click()
		time.sleep(5)
		finalize = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button")
		finalize.click()
		time.sleep(30)
		browser.close()
		browser.quit()

if __name__ == "__main__":
	create()
