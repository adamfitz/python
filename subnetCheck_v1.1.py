#!/usr/bin/env python
#
# Author: Adam Fitzgerald
# Purpose: Script to iterate though all IPs in an IP address block and outputs
# the PTR records if they are found
# Version: 1.1
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
import argparse

def get_dns_records(): 
	
		unicode_address_block = unicode(address_block) 								#convert the user supplied address block to unicode object
		users_ip_block = ipaddress.ip_network(unicode_address_block, strict=False) 	#create an IPv4Network class from the entered user data
		address_block_subnet_mask = str(users_ip_block.netmask) 					#get the subnet mask
		number_of_ipv4_host_addresses = users_ip_block.num_addresses 				#get the total number of IPs in the supplied address block

		#Output some basic information to the screen
		print ("")
		print ("Your have entered the network: {0}, the subnet mask is: {1}".format(address_block, address_block_subnet_mask))
		print ("The number of addresses in this address block is: {0}".format(number_of_ipv4_host_addresses))
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
		print ("\nThe number PTR records found is: %s, out of a potential %s" % (total_number_of_returned_ptr_records, number_of_ipv4_host_addresses))

def validate_user_input():
	parser = argparse.ArgumentParser(description="Validate users IPv4 address block") #create argument parser object
	parser.add_argument("CIDR address block", required=True, type=str)
	args = parser.parse_args()

def main():
	try:
		validate_user_input()
	except ValueError:
		print ("Please enter a valid IPv4 address block in CIDR notation.")
		sys.exit(1)
	else:
		get_dns_records()


if __name__ == "__main__":
	main()
 	