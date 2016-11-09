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


from sys import argv
import ipaddress
import socket

script, addressBlock = argv

#convert the user supplied address block to unicode object
unicodeAddressBlock = unicode(addressBlock)
usersIpBlock = ipaddress.ip_network(unicodeAddressBlock, strict=False)
numberOfIpv4HostAddresses = usersIpBlock.num_addresses

print "Your have entered the network: %s" % (addressBlock)
print "The number of host addresses in this network is: %d" % (numberOfIpv4HostAddresses)


#Function to do the DNS lookup for he supplied subnet
#def getDnsRecords(self):
recordsToReturn = str(usersIpBlock.hosts())
print type(recordsToReturn)
for x in recordsToReturn:
	print socket.gethostbyaddr(x)
	print x
	
	
