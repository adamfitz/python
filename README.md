Collection of python scripts

- subnetCheck.py -

Description:
A script written to take an IP address block and return all the PTR records that exist for IPs in that address block.  This script uses the ipaddress module to validate the CIDR notation of the address block provided by the user and return the number of valid address in the provided address block.  Then iterates through all the valid host IPs int he provided address block and print the IP address and the hostname, no value is returned for IPs that do not have a corresponding PTR.

WIP:
- Function to sanitise user input
- Function to support IP address and subnet mask notation
- Error handling function
- Script usage/help function
- Cleaner code

Script Current version: 1.3

Vesioning:

subnetCheck.py = original hack

subnetCheck_v1.1.py = trying to get fancy, script kind of works

subnetCheck_v1.2.py = hacking around to add input validation

subnetCheck_v1.3.py = closer to finishing up input validation
