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
#create an IPv4 object from the entered user data
usersIpBlock = ipaddress.ip_network(unicodeAddressBlock, strict=False)
#get a list of all the Ips in the address block and assign to a list
numberOfIpv4HostAddresses = usersIpBlock.num_addresses
print ""
print "Your have entered the network: %s" % (addressBlock)
print "The number of host addresses in this network is: %d" % (numberOfIpv4HostAddresses)

#convert the type of the elements in the list to a string as this is required
#for the socket.gethostbyaddr() function
recordsToReturn = usersIpBlock.hosts()
changeToList = list(recordsToReturn)
print type(changeToList)

listAsString = str(changeToList)
print listAsString
#define a function to iterate through the list
def getDnsRecords():
	for i in listAsString:
		#str(changeToList[i]
		#returnedDnsRecord = socket.gethostbyaddr(i)
		print i[2]
#call the function to iterate through the list
#getDnsRecords()

#Function to do the DNS lookup for he supplied subnet

#recordsToReturn = usersIpBlock.hosts()

#print type(recordsToReturn)
#for x in recordsToReturn:
#	print socket.gethostbyaddr('')
#	print x
	
	
