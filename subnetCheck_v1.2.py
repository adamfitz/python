#!/usr/bin/env python
#
# Author: Adam Fitzgerald
# Purpose: Script to iterate though all IPs in an IP address block and outputs
# the PTR records if they are found
# Version: 1.2
#
# ipaddress module docs can be found here:
# https://docs.python.org/dev/howto/ipaddress.html#ipaddress-howto
#
# socket module docs found here:
# https://docs.python.org/2/library/socket.html#module-socket
#
from __future__ import print_function
from sys import argv
import sys
import ipaddress
import socket

# global variables for user input
user_cidr_block = argv[1]														#assign proviedd CIDR block to a list
subnetmask_bits = user_cidr_block.split("/")

def get_dns_records():
	unicode_address_block = unicode(user_cidr_block)							#convert the user supplied address block to unicode object
	users_ip_block = ipaddress.ip_network(unicode_address_block, strict=False) 	#create an IPv4Network class from the entered user data
	address_block_subnet_mask = str(users_ip_block.netmask) 					#get the subnet mask as string
	number_of_ipv4_host_addresses = users_ip_block.num_addresses 				#get the total number of IPs in the supplied address block

	#Output some basic information to the screen
	print ("")
	print ("Your have entered the network: {0}, the subnet mask is: {1}".format(user_cidr_block, address_block_subnet_mask))
	print ("The number of IP addresses in this address block is: {0}".format(number_of_ipv4_host_addresses))
	print ("")

	all_host_ips = list(users_ip_block.hosts()) 								#retrieve all the host ips from the IPv4Network class
	ips_to_iterate_through = map(str, all_host_ips)								#convert the unicode list back to a byte string list
	total_number_of_returned_ptr_records = 0 									#var to count the number of returned PTRs

	for i in ips_to_iterate_through: #need to write if statement for a single IP and throw it out of the loop if only 1 address is given
		try:
			ptr_record = list(socket.gethostbyaddr(i))
			print ("%-20s %-20s" % (i, ptr_record[0]))
			total_number_of_returned_ptr_records = total_number_of_returned_ptr_records + 1
		except socket.herror as unknownHostError:
			continue
	print ("\nThe number of PTR records found is: %s, out of a potential %s" % (total_number_of_returned_ptr_records, number_of_ipv4_host_addresses))

def subnet_check_usage():
	print ("")
	print (
	"""
	subnetCheck script version 1.2
	Usage: -h (prints this help screen)

	Takes an IP address block in CIDR notation and returns all DNS records
	for that IP address range.

	Example: subnetCheck_v1.2.py 172.16.0.1/16

	Warning: The script may take some time to run when address blocks larger
	than /24 are requested.  Also the script may appear to be hung or pause
	for an excessive period of time for large address ranges or if there are
	not many DNS records present.
	"""
	)

def validate_user_input():
	subnetmask_bits_string = subnetmask_bits[1]
	subnetmask_bits_integer = int(subnetmask_bits_string)

	if len(subnetmask_bits) != 2:
		subnet_check_usage()
	elif user_cidr_block == "-h":
		subnet_check_usage()
	elif (subnetmask_bits_integer < 1):
		print ("The prefix bits should not be less than 1")
		print ("You entered:",subnetmask_bits_integer)
		subnet_check_usage()
	elif (subnetmask_bits_integer > 32):
		print ("The prefix bits should not be greater than 32")
		print ("You entered:",subnetmask_bits_integer)
		subnet_check_usage()
	else:
		get_dns_records()

def main():
	if len(argv) != 2:
		subnet_check_usage()
	elif argv[1] == "-h":
		subnet_check_usage()
	elif len(argv) == 2:
		validate_user_input()
	else:
		get_dns_records()

if __name__ == "__main__":
	main()
