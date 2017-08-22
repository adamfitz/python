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
The script requires 3 arguments to run:
- device name or IP
- GUI username
- GUI password
"""


from __future__ import print_function
import sys
from sys import argv
import f5.bigip
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


try:
    DEVICE_NAME = argv[1]
    USER_NAME = argv[2]
    PASSWORD = argv[3]
except IndexError as not_enough_arguments:
	pass

#disable insecure connection warning (connecitng via password auth without using a certificate)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#connect to the box
f5connection = f5.bigip.ManagementRoot(DEVICE_NAME, USER_NAME, PASSWORD)
#get the pool name
pool_names = f5connection.tm.ltm.pools.get_collection()
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
