#!/usr/bin/env python
"""
Author: Adam Fitzgerald

Purpose: Login to TG-1 router and get the IPv4 IP.

Usage: This script is used to login to the TG-1 router and extract the WAN,
Gateway and DNS server IPs via the TG-1 web interface.

It uses the chrome browser and requires the chromedriver program
to be put into the same directory as the script, the chrome driver can be
downloaded here: https://sites.google.com/a/chromium.org/chromedriver/downloads

Version: 0.1

Required Modules:
- selenium
- time
- beautiful soup 4
- re

Device Details:  The TG-1 router is a Technicolour gateway device rebranded
by the Australian ISP Internode and used for connecting premesises to NBN
fibre to the node.

Testing was done on the below verion of TG-1 hwardware and software.

Product Vendor: Technicolor
Product Name: MediaAccess TGiiNet-1
Software Version: 15.4
Firmware Version: 15.53.7004-V1-7-1-CRF557
Hardware Version: VANT-5

"""
from selenium import webdriver
from time import sleep
from bs4 import *
import re

browser = webdriver.Chrome('./chromedriver') # setup chrome driver
router_url = "http://10.23.0.254/login.lp" # router IP addres//web portal login
browser.get(router_url) # open the login page for my TG-1 router

# find the IDs below with the developer tools in chrome (elements TAB)
username = browser.find_element_by_id("srp_username") # setup the username form field
password = browser.find_element_by_id("srp_password") # setup the password form field

username.send_keys("")
password.send_keys("admin")

# find the submit button and press it
login_button = browser.find_element_by_id("sign-me-in")
login_button.click()

# sleep for 3 seconds to allow the initial settings page to load
sleep(3)

# load up and grab the settings page and assign html output to string variable
what_is_my_ip__url = "http://10.23.0.254/modals/internet-modal.lp"
browser.get(what_is_my_ip__url) # go to page behind the login page?
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

# search html and convert to text
html_to_text = BeautifulSoup(innerHTML, 'html.parser')
raw_page_text = html_to_text.get_text()

# use a regex to parse the page and find the IP addresses then print them
ip_address = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', raw_page_text)

print("WAN IP  ", ":", ip_address[0], sep="\t")
print("WAN Gateway", ":", ip_address[1], sep="\t")
print("Nameserver 1", ":", ip_address[2], sep="\t")
print("Nameserver 2", ":", ip_address[3], sep="\t")
