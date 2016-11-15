#!/usr/bin/env python
#
# Author: Adam Fitzgerald
# Purpose: Script to iterate though all IPs in an IP address block and output
# any A records that are found
# Version: 1.0
#
# ipaddress module docs can be found here:
# https://docs.python.org/dev/howto/ipaddress.html#ipaddress-howto
#
# socket module docs found here:
# https://docs.python.org/2/library/socket.html#module-socket
#
from sys import argv
import ipaddress
import socket

script, addressBlock = argv

#convert the user supplied address block to unicode object
unicodeAddressBlock = unicode(addressBlock)

#create an IPv4Network class from the entered user data
usersIpBlock = ipaddress.ip_network(unicodeAddressBlock, strict=False)

#get the total number of IPs in the supplied address block
numberOfIpv4HostAddresses = usersIpBlock.num_addresses

#Output some basic information to the screen
print ""
print "Your have entered the network: %s" % (addressBlock)
print "The number of addresses in this subnet is: %d" % (numberOfIpv4HostAddresses)
print ""

#retrieve all the host ips from the IPv4Network class
allHostIps = list(usersIpBlock.hosts())

#convert the unicode list back to a byte string list 
ipsToIterateThrough = map(str, allHostIps)

#function to do the DNS lookup and print the results to the screen
def getDnsRecords():
	for i in ipsToIterateThrough:
		try:
			ptr_record = list(socket.gethostbyaddr(i))
			print "%-20s %-20s" % (i, ptr_record[0])
		except socket.herror as unknownHostError:
			continue

# call the function
getDnsRecords()

	
	
