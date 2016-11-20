#!/usr/bin/env python
#
# Author: Adam Fitzgerald
# Purpose: Script to iterate though all IPs in an IP address block and outputs
# the PTR records if they are found
# Version: 1.0
#
# ipaddress module docs can be found here:
# https://docs.python.org/dev/howto/ipaddress.html#ipaddress-howto
#
# socket module docs found here:
# https://docs.python.org/2/library/socket.html#module-socket
#
from __future__ import print_function
from sys import argv
import ipaddress
import socket

script, address_block = argv

#convert the user supplied address block to unicode object
unicode_address_block = unicode(address_block)

#create an IPv4Network class from the entered user data
users_ip_block = ipaddress.ip_network(unicode_address_block, strict=False)

#get the subnet mask
address_block_subnet_mask = str(users_ip_block.netmask)

#get the total number of IPs in the supplied address block
number_of_ipv4_host_addresses = users_ip_block.num_addresses

#Output some basic information to the screen
print ("")
print ("Your have entered the network: %s, the subnet mask is: %s" % (address_block, address_block_subnet_mask))
print ("The number of addresses in this address block is: %d" % (number_of_ipv4_host_addresses))
print ("")

#retrieve all the host ips from the IPv4Network class
all_host_ips = list(users_ip_block.hosts())

#convert the unicode list back to a byte string list 
ips_to_iterate_through = map(str, all_host_ips)

#function to do the DNS lookup and print the results to the screen
def get_dns_records():
	#var to count the number of returned PTRs
	total_number_of_returned_ptr_records = 0

	for i in ips_to_iterate_through:
		try:
			ptr_record = list(socket.gethostbyaddr(i))
			print ("%-20s %-20s" % (i, ptr_record[0]))
			total_number_of_returned_ptr_records = total_number_of_returned_ptr_records + 1
		except socket.herror as unknownHostError:
			continue
	print ("\nThe number PTR records found is: %s, out of a potential %s" % (total_number_of_returned_ptr_records, number_of_ipv4_host_addresses))

# call the function
get_dns_records()
