#!/usr/bin/env python
"""
Author: Adam Fitzgerald
Purpose: Login to TG-1 router and get the IPv4 IP.  This script uses the
chrome browser and requires teh chromedriver program in the same directory as the
script, it can be found here:

https://sites.google.com/a/chromium.org/chromedriver/downloads


Version: 0.1

Modules:
- selenium

"""
from selenium import webdriver
from time import sleep
from lxml import *
from lxml import html

browser = webdriver.Chrome('./chromedriver')
router_url = "http://10.23.0.254/login.lp" # router IP addres//web portal login
browser.get(router_url) # open the login page for my TG1 router

# find the IDs below with the developer tools in cheom (elements TAB)
username = browser.find_element_by_id("srp_username") #username form field
password = browser.find_element_by_id("srp_password") #password form field

username.send_keys("")
password.send_keys("admin")

# find the submit button and press it
login_button = browser.find_element_by_id("sign-me-in")
login_button.click()

# sleep for 5 seconds to allow the initial settings page to load
sleep(3)

# load up and grab the settings page and assign html output to string variable
what_is_my_ip__url = "http://10.23.0.254/modals/internet-modal.lp"
browser.get(what_is_my_ip__url) # go to page behind the login page?
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

# search html and convert to text
html_element = html.document_fromstring(innerHTML)
#print(dir(html_element.cssselect))
div_class_element = html_element.cssselect("\"class=control-group\"")
#element_text = []
#for instance in div_class_element:
    #text = instance.text_content()
    #element_text.append(text)
#print(type(element_text))
