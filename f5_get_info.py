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
getpass

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
    print("\n")
    print(7 * "-" , "Please make your selection from the below 5 options" , 7 * "-")
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
            print("Attemping to get a list of partitions from a device \n")
            try:
                box_connection_list = connect_to_box()
                DEVICE_NAME = box_connection_list[0]
                f5connection = box_connection_list[1]
                list_of_partitions = get_device_partitions(f5connection)
                print("List of partitions found on: ",  DEVICE_NAME, "\n")
                for i in list_of_partitions:
                    print(i)
                sys.exit(1)
            except:
                pass
        elif choice == 2:
            print("Attemping to get a list of all virtual servers from ")
            try:
                box_connection_list = connect_to_box()
                DEVICE_NAME = box_connection_list[0]
                f5connection = box_connection_list[1]
                list_of_vs = get_vs_list(f5connection)
                print("The number of configured virtual servers on", DEVICE_NAME, "is:", len(list_of_vs))
                print("")
                print("The configured virtual server names on", DEVICE_NAME,"\n")
                for i in list_of_vs:
                    print(i)
                sys.exit(1)
            except:
                pass
        elif choice == 3:
            print("Attemping to get a list of all pools configured on device ")
            try:
                box_connection_list = connect_to_box()
                DEVICE_NAME = box_connection_list[0]
                f5connection = box_connection_list[1]
                pool_names = get_pool_list(f5connection)
                print("Total number of pools found on:", DEVICE_NAME, "is:", len(pool_names))
                print("")
                print("List of all pool names found on:", DEVICE_NAME,"\n")
                for i in pool_names:
                    print(i)
                sys.exit(1)
            except:
                pass
        elif choice == 4:
            print("Enter device info below to retreive list of configured pools")
            try:
                box_connection_list = connect_to_box()
                DEVICE_NAME = box_connection_list[0]
                f5connection = box_connection_list[1]
                pool_names = get_pool_list(f5connection)
                for i in pool_names:
                        print(i)
                selected_pool = input("Please enter pool member name from the list above: ")
                pool_members = get_pool_members(f5connection, selected_pool)
                print("Pool Member:\t State:".expandtabs(4))
                print(24 * "-")
                for key in pool_members:
                    print(key,"\t".expandtabs(4), pool_members[key])
            except:
                pass
        elif choice == 5:
            print("Exiting...")
            loop = False # Set to false to end the loop
            sys.exit(1)
        else:
            # anthing other than 1-5 prompts for correct entry
            input("Please enter a selection betwen 1 and 5. Press any key to try again..")
    

def connect_to_box():
    try:
        DEVICE_NAME = input("Enter the F5 device name or IP address: ")
        USER_NAME = input("Please enter F5 username: ")
        PASSWORD = getpass.getpass("Please enter password for F5 device: ")
    except NameError as something_broke:
        print("connect_to_box function error")
    #disable insecure connection warning (connecitng via password auth without using a certificate)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    #connect to the box
    f5connection = f5.bigip.ManagementRoot(DEVICE_NAME, USER_NAME, PASSWORD)
    return [DEVICE_NAME, f5connection]

def get_pool_list(f5connection):
    list_of_pools = []
    #get the pool name
    pool_name_object = f5connection.tm.ltm.pools.get_collection()
    for i in pool_name_object:
        list_of_pools.append(i.name)
    return list_of_pools

def select_pool_name():
    POOL_NAME = input("Please enter a pool from the resultant list of pools on: ", DEVICE_NAME, ": ")

def get_pool_members(f5connection, selected_pool):
    pool_member_dict = {}
    pool = f5connection.tm.ltm.pools.pool.load(name=selected_pool)
    #get a list of pool members from the test pool
    for pool_member in pool.members_s.get_collection():
        pool_member_dict[pool_member.name] = pool_member.state
    return pool_member_dict

def get_vs_list(f5connection):
    # function gets a list of all configured virtual servers on a device
    vs_name_object = f5connection.tm.ltm.virtuals.get_collection()
    list_of_vs = []
    for i in vs_name_object:
        list_of_vs.append(i.name)
    return list_of_vs

def get_device_partitions(f5connection):
    list_of_partitions = []
    for folder in f5connection.tm.sys.folders.get_collection():
        if not folder.name == "/" and not folder.name.endswith(".app"):
            list_of_partitions.append(folder.name)
    return list_of_partitions

if __name__ == "__main__":
    main()

# wip catch errors:
# iControlUnexpectedHTTPError
# try / except for the above error (authentication)