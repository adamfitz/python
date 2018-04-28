#!/usr/bin/env python3


"""
Synopsis:
---------
A basic POC F5 script using the f5-sdk to list the pool name, pool members and
their current state

Required libraries:
-------------------
requests
f5-sdk

Usage:
------
Run script and provide device name, username and password to connect to the box
"""


from __future__ import print_function
import sys
from sys import argv
import f5.bigip
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import getpass

def print_menu():
    #print a menu
    print(6 * "-" , "Please make your selection from the below 5 options" , 6 * "-")
    print("1. List all device partitions")
    print("2. List all the Virtual servers")
    print("3. List all the Pools")
    print("4. List pool member and status of specified pool member")
    print("5. Exit")
    print(67 * "-")

def main(): 
    loop = True
    # loop while true
    while loop:      
        print_menu()
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:     
            print("Attemping to get a list of partitions from ")
            try:
                get_device_partitions()
                print_device_partitions()
            except:
                pass
            print("option 1")
        elif choice == 2:
            print("Attemping to get a list of all virtual servers from ")
            try:
                get_device_partitions()
                print_device_partitions()
            except:
                pass
            print("option 2")
        elif choice == 3:
            print("Attemping to get a list of all pools configured on device ")
            try:
                get_pool_list()
                select_pool_name()
                print_pool_members()
            except:
                pass
            print("option 3")
        elif choice == 4:
            print("Listing the status of all pool members from pool: ")
            try:
                select_pool_name()
                print_pool_members()
            except:
                pass
            print("option 4")
        elif choice==5:
            print("Exiting...")
            sys.exit(1)
            loop = False # Set to false to end the loop
        else:
            # anthing other than 1-5 prompts for correct entry
            input("Please enter a selection betwen 1 and 5. Press any key to try again..")
    

def connect_to_box():
    try:
        #DEVICE_NAME = argv[1]
        #USER_NAME = argv[2]
        #PASSWORD = argv[3]
        DEVICE_NAME = input("Enter the F5 device name or IP address: ")
        USER_NAME = input("Please enter F5 username: ")
        PASSWORD = getpass.getpass("Please enter password for F5 device: ")
    except NameError as something_broke:
	    pass
    #disable insecure connection warning (connecitng via password auth without using a certificate)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    #connect to the box
    f5connection = f5.bigip.ManagementRoot(DEVICE_NAME, USER_NAME, PASSWORD)

def get_pool_list():
    #get the pool name
    pool_names = f5connection.tm.ltm.pools.get_collection()
    print("The number of configured pools on ", DEVICE_NAME, " is: ", len(pool_names))
    print("The configured pool names are: ", pool_names)

def select_pool_name():
    POOL_NAME = input("Please enter a pool from the resultant list of pools on: ", DEVICE_NAME, ": ")

def print_pool_members():
    for i in pool_names:
        current_pool_name = i.name

    #get a list of pool members from the test pool
    pool_member_list = []
    print("Getting the list of pool members from:", i.name, "and reporting their current state:\n")
    for pool in pool_names:
        for pool_member in pool.members_s.get_collection():
            print("From:", current_pool_name, "pool member: >>", pool_member.name, "<< current state is", pool_member.state )
            pool_member_list.append(pool_member.name)
        #map each member of the list to byte code strings
        pool_member_list = map(str, pool_member_list)
    #print(pool_member_list)

def get_device_partitions():
    print("placeholder! :)")

def print_device_partitions():
    print("placeholder! :)")

if __name__ == "__main__":
    main()