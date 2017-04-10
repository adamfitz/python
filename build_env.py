#!/usr/bin/env python

"""
Script to setup a project with virtulenv

- creates project direectory
- sets up virtualenv in project directory
- activates the environments

- checks if the project directory already exists
- if directory exists the script will install libraries to that directory
- script can be run with a -il flag (install library) and will install to the specified project dir

Constants

1 = flag for what the script should (is being told) to do
2 = the argument to pass to the script based on the first flag


"""

from __future__ import print_function
from sys import argv
import os

# constants for user imput

CONSTANT_1 = argv[0]
CONSTANT_2 = argv[1]


def build_env_help():
    print ("")
	print (
	"""
	build_script.py script
	Usage: -h (prints this help screen)

	Creates a virtualenv based on user input
	"""
	)
