#!/usr/bin/env python3.6
"""
Author: Adam Fitzgerald
Purpose: Take an IPv4 address block in CIDR notation and return all DNS records
found in that IPv4 address block.

Version: 1.3

Usage:
subnet_check.py -h (prints the help screen)
subnet_check.py 192.0.2.0/24
subnet_check.py 198.51.100.0/25
subnet_check.py 203.0.113.0/29

All correct CIDR notation is accepted however be aware the script may appear
to hang or pause for an excessive period of time when iterating through
large address blocks or if there are not many DNS records are present/found.

Modules:
The ipaddress and socket modules are used.

ipaddress module docs found here:
https://docs.python.org/dev/howto/ipaddress.html#ipaddress-howto

socket module docs found here:
https://docs.python.org/2/library/socket.html#module-socket
"""

from __future__ import print_function
from sys import argv
import ipaddress
import socket

def main():
	try:
		# global variable to grab the CIDR block
		user_cidr_block = argv[1]

		if len(argv) != 2:
			subnet_check_usage()
		elif argv[1] == "-h":
			subnet_check_usage()
		#elif len(argv) == 2:
		#	validate_user_input()
		else:
			get_dns_records()

	except IndexError as not_enough_args:
		print(f"\r\nError: Not enough Arguments.")
		subnet_check_usage()



def get_dns_records():
	#convert to unicode object
	unicode_address_block = unicode(user_cidr_block)
	#create an IPv4Network class
	users_ip_block = ipaddress.ip_network(unicode_address_block, strict=False)
	#get the subnet mask as string
	address_block_subnet_mask = str(users_ip_block.netmask)
	#get the total number of IPs in the block
	number_of_ipv4_host_addresses = users_ip_block.num_addresses

	#Output some basic information
	print ("")
	print ("You have entered the network: {0}, the subnet mask is: {1}".format
		(user_cidr_block, address_block_subnet_mask))
	print ("The number of IPv4 addresses in this address block is: {0}".format
		(number_of_ipv4_host_addresses))
	print ("")
	#get all the host IPs
	all_host_ips = list(users_ip_block.hosts())
	#convert the unicode list back to a byte string list
	ips_to_iterate_through = map(str, all_host_ips)
	#var to count the number of returned PTRs
	total_number_of_returned_ptr_records = 0

	# need to write if statement for a single IP and throw it out of the loop
	# if only 1 address is given
	for i in ips_to_iterate_through:
		try:
			ptr_record = list(socket.gethostbyaddr(i))
			print ("%-20s %-20s" % (i, ptr_record[0]))
			total_number_of_returned_ptr_records = total_number_of_returned_ptr_records + 1
		except socket.herror as unknownHostError:
			continue
	print ("\nThe number of returned PTR records is: %s, out of a potential %s"
		% (total_number_of_returned_ptr_records, number_of_ipv4_host_addresses))

def subnet_check_usage():
	print(
	f"""
subnet_check script
Usage: -h (prints this help screen)

Take an IPv4 address block in CIDR notation and return all DNS records found
in that IPv4 address block.

Example: subnet_check.py 172.16.0.1/16

Warning: When large address blocks are specified the script will take some 
time to run, likewise if there are not many PTR records present/found.
"""
	) #the string is "de intented" on purpose to remove the default triple quote intent
"""
def validate_user_input():
	try:
		#split the input into subnet bits for validation
		subnetmask_bits = user_cidr_block.split("/")
		subnetmask_bits_string = subnetmask_bits[1]
		subnetmask_bits_integer = int(subnetmask_bits_string)
		#split network bits into 4 octets for validation
		network_address = subnetmask_bits[0]
		network_address_octects = network_address.split(".")

		if len(subnetmask_bits) != 2:
			subnet_check_usage()
		elif len(network_address_octects) < 3:
			subnet_check_usage()
		elif user_cidr_block == "-h":
			subnet_check_usage()
		elif (subnetmask_bits_integer < 1):
			print ("\nThe prefix bits should not be less than 1")
			print ("You entered:",subnetmask_bits_integer)
			subnet_check_usage()
		elif (subnetmask_bits_integer > 32):
			print ("\nThe prefix bits should not be greater than 32")
			print ("You entered:",subnetmask_bits_integer)
			subnet_check_usage()
		else:
			get_dns_records()
	except (IndexError, ValueError) as validationErrors:
		subnet_check_usage()
"""

if __name__ == "__main__":
	main()
