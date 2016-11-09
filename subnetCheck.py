#!/usr/bin/env python
#
# Author: Adam Fitzgerald
# Purpose: Script to iterate though all IPs in an IP address block and output
# any A records that are found
# Version: 1.0

from sys import argv

script, addressBlock, subnetMask = argv


