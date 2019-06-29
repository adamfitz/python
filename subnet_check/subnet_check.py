#!/usr/bin/env python3.6
"""
Author: Adam Fitzgerald
Purpose: Take an IPv4 or IPv6 address block in CIDR notation and return all DNS 
records found in the given address block.

Version: 1.4

Usage:
subnet_check.py -h (prints the help screen)
subnet_check.py 192.0.2.0/24
subnet_check.py 203.0.113.0/29

subnet_check.py 2001:db8::/32
subnet_check.py 2001:db8::1/128

All correct CIDR notation is accepted however be aware the script may appear
to hang or pause for an excessive period of time when iterating through
large address blocks or if there are not many DNS records are present/found.

Python version: 3.6 or above

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
			get_dns_records(user_cidr_block)

	except IndexError as not_enough_args:
		print(f"\r\n:: Error :: Not enough Arguments.\r\n\r\nHelp Command:\r\nsubnet_check.py -h\r\n")
	except ValueError as not_valid_network:
		print(f"\r\n:: Error :: Invalid IPv4 or IPv6 address.\r\n\r\nHelp Command:\r\nsubnet_check.py -h\r\n")

def get_dns_records(user_cidr_block):
	"""
	This function attempts to create an ip_address object and retrieve the
	associated PTR records for the given address block.
	"""
	# make sure the user input is a string:
	user_cidr_block = str(user_cidr_block)

	# create network class
	address_block = ipaddress.ip_network(user_cidr_block, strict=False)
	# subnet mask as string
	subnet_mask = str(address_block.netmask)
	# total addresses
	total_host_addresses = address_block.num_addresses

	# determine address family accordingly
	address_family = address_block.version
	if address_family == 6:
			address_family = "IPv6"
	else:
		address_family = "IPv4"

	# Output summary info
	print ("")
	print(f"Addressess family:\t{address_family}")
	print (f"Address block:\t\t{user_cidr_block}\r\nSubnet mask:\t\t{subnet_mask}")
	print (f"Total addresses:\t{total_host_addresses}")
	print ("")

	# assign all host addresses to a list
	all_host_ips = list(address_block.hosts())

	# convert the list of ipaddress module classes back to strings
	ips_to_iterate_through = map(str, all_host_ips)

	# counter for returned PTRs
	ptr_counter = 0

	# need to write if statement for a single IP and throw it out of the loop
	# if only 1 address is given

	# show me the sata type for a sinle address (list or string?)
	#print(f"What is the data type of a single Ip address?? {all_host_ips}")  # <- nothing it is an empty list
	#print(f"What functions do I have?? ?? {dir(address_block)}")  
	#print(f"Testing... {address_block.network_address}")


	if (subnet_mask == "255.255.255.255") or (subnet_mask == "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"):
		try:
			lookup_address = str(address_block.network_address)
			ptr_record = socket.gethostbyaddr(lookup_address)
			print(f"{lookup_address} \t {ptr_record[0]}")
			ptr_counter =+ 1
		except socket.herror as unknownHostError:
			pass
		print (f"\r\nReturned PTR records: {ptr_counter}, out of the total: {total_host_addresses}")
	else:
		for i in ips_to_iterate_through:
			try:
				ptr_record = list(socket.gethostbyaddr(i))
				print(f"{i} \t {ptr_record[0]}")
				ptr_counter =+ 1
			except socket.herror as unknownHostError:
				continue
			print (f"\r\nReturned PTR records: {ptr_counter}, out of the total: {total_host_addresses}")



	

def subnet_check_usage():
	# the below string is purposely not indented to work around the issue with 
	# triple quoted strings and the default indent.
	print(
	f"""
subnet_check script
Usage: -h (prints this help screen)

Take an IPv4 or IPv6 address block in CIDR notation and return all DNS 
records found in the given address block.

Example: 
subnet_check.py 172.16.0.1/24
subnet_check.py 2001:db8::1/128

Warning: When large address blocks are specified the script will take some 
time to run, likewise if there are not many PTR records present/found.

NOTE: It is NOT recommended to run this against a large IPv6 address block as
there is progress indicator implemented and it will be difficult to determine 
if the script is still running or not.
"""
	) # the string is "de intented" on purpose to remove the default triple quote intent
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
