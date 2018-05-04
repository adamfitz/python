#!/usr/bin/env python3


"""
Synopsis:
---------
Uses f5 sdk to take a file with a list of devices and output the device name
and software version.

Required libraries:
-------------------
requests
f5-sdk
getpass

Usage:
------
Run script and provide the filename as an argument
"""


from __future__ import print_function
import sys
import f5.bigip
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import getpass

#disable insecure connection warning (connecitng via password auth without using a certificate)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# dict to hold ouput
software_versions = {}
# ask for the list of devices
DEVICE_LIST = input("Please enter the file with names of all F5 devices: ")
try:
    with open(DEVICE_LIST, "r") as device_list:
        USER_NAME = input("Please enter F5 username: ")
        PASSWORD = getpass.getpass("Please enter password for F5 device: ")
        for line in device_list:
            try:
                DEVICE_NAME = line
                #connect to the box
                f5connection = f5.bigip.ManagementRoot(DEVICE_NAME, USER_NAME, PASSWORD)
                # add device name and tmos software version to dict
                CURRENT_SOFTWARE_VERSION = f5connection.tmos_version
                software_versions[DEVICE_NAME] = CURRENT_SOFTWARE_VERSION
                print("Device:", DEVICE_NAME, "== Software Version:", CURRENT_SOFTWARE_VERSION)
            except Exception as device_connection_error:
                #print("There is an issue connecting to",DEVICE_NAME,)
                print(device_connection_error)
except FileNotFoundError as file_not_found:
            print("\n== Device list file NOT found, please enter the correct filename. == \n")
            sys.exit(1)

    
        


