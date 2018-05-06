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

# for testing purposes define the filename
# DEVICE_LIST = "f5_test_list.txt"

def main():
    DEVICE_LIST = input("Please enter the file with names of all F5 devices: ")
    names = read_and_sanitise_file(DEVICE_LIST)
    get_device_info(names)


def read_and_sanitise_file(DEVICE_LIST):
    box_names = []
    box_names_checked = []
    box_names_incorrect = []

    try:
        with open(DEVICE_LIST, "r") as device_list:
            # read each line into the list
            box_names = device_list.readlines()
            # strip off the newline char from each element in the list
            box_names = [x.strip("\n") for x in box_names]
    except FileNotFoundError as file_not_found:
            print("\n== Device list file NOT found, Please check the file exists and try again. == \n")
            sys.exit(1)
    
    # sort list and check if any elements have a space or are empty
    for i in box_names:
        if (' ' in i) or (i == ''):
            box_names_incorrect.append(i)
        else:
            box_names_checked.append(i)
    return box_names_checked

def get_device_info(f5_device_list):
    user_name = input("Please enter F5 username: ")
    user_password = getpass.getpass("Please enter password for F5 device: ")
    # dict to hold ouput
    software_versions = {}
    #disable insecure connection warning (connecitng via password auth without using a certificate)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    for f5_name in f5_device_list:  
        try:
            # setup connect to the box
            f5connection = f5.bigip.ManagementRoot(f5_name, user_name, user_password)
            f5_software_version = f5connection.tmos_version
            # add device name and tmos software version to dict
            software_versions[f5_name] = f5_software_version
        except Exception as device_connection_error:
            print("There is a problem connecting to", f5_name, "please check connectivity / username / password.")
        #print(device_connection_error, "\n") # uncomment this line to enable printing of the exception to stdout
    for i in software_versions:
        print(i , "== Software Version:", software_versions[i])

if __name__ == "__main__":
    main()

    
        


