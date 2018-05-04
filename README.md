A collection of useful (hopefully) python scripts

## subnet_check.py

#### Description:
Take an IPv4 address block in CIDR notation and return all DNS records
found in that IPv4 address block.

**Current version:**
1.3

**WIP:**
- Function to support IP address and subnet mask notation
- Check for /32 host IP and do single look up

## build_env.py


#### Description:
A script to create a new project directory and setup virtualenv under this
directory

**Current version:**
0.2

**WIP:**
- Environment check to return the current status

## f5_get_info.py


#### Description:
Connect to F5 device, get virtual servers, pools, pool members, partitions

**Current version:**
0.1

**WIP:**
- Everything

## f5_get_version.py


#### Description:
Connect to F5 device, get current software version

**Current version:**
1.0

## router_ip.py


#### Description:
Connect to TG1 router, login and grab the current WAN IP, WAN gateway IP and DNS name server IPs

**Current version:**
0.2

**WIP:**
- Doing something useful with it (sending an email with the extracted info perhaps)
