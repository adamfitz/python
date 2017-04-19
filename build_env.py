#!/usr/bin/env python

"""
Script to setup a project with virtulenv

- creates project direectory
- sets up virtualenv in project directory
- activates the environments

- checks if the project directory already exists
- if directory exists the script will install libraries to that directory
- script can be run with a -il flag (install library) and will install to the
specified project dir

Constants

1 = flag for what the script should (is being told) to do
2 = the argument to pass to the script based on the first flag


"""

from __future__ import print_function
import sys
from sys import argv
import os
import pwd
import pip

# constants for user imput

CONSTANT_1 = argv[1]
CONSTANT_2 = argv[2]

def build_env_help():
	print ("")
	print (
	"""
	build_script.py script
	Usage: -h (prints this help screen)

	This script is built for linux systems and will create a new project
	directory and setup virtualenv under this directory.

	The default directory path is:
	/home/<current user>/scripts/

	So new project directories will be created in:
	"/home/<current user>/scripts/<newProjectName>"

	Use the following flags along with a project name to start the build

	Create a new virtualenv called <newProjectName>
	: build_env.py -c projectName
	"""
	)
"""
def validate_user_input():
    if not argv[0]:
		build_env_help()
	elif not argv[1]:
		build_env_help()
	elif argv[0] == "-h":
		build_env_help()
	elif argv[3] in globals():
		build_env_help()
	else:
		build_env()
"""

def check_dependencies(library):
	package_present = ""
	try:
		import virtualenv
		package_present = "y"
	except ImportError as e:
		user_choice = input("The required python library (virtualenv) is not "\
		"installed globally, do you wish to install this now?: (y|n) ")
		while not (user_choice == "y" or user_choice == "Y" or user_choice \
		=="n" or user_choice =="n"):
			user_choice = input("Please enter a valid option, install python "\
			"package (virtualenv) globally? (y|n) ")
		if user_choice == "y" or user_choice == "Y":
			pip.main(['install', library])
		else:
			print("\nThe virtualenv library is a requirement to run this "\
			"script, please install this package globally before running this "\
			"script again or choose \"y\" when prompted.")
			sys.exit(1)
	if package_present == "y":
		print("Dependencies are already met, python package (virtualenv) is "\
		"installed globally.")
	else:
		sys.exit(1)

def create_project_directory():
	default_dir = os.path.expanduser("~") +"/scripts/"
	new_directory = default_dir + CONSTANT_2
	print("")
	print("New project directory will be created in the following location: ", \
	default_dir)
	if not os.path.exists(new_directory):
		print("\nCreated project directory: ", new_directory)
		os.makedirs(new_directory)
	else:
		print("\nDirectory already exists! (", new_directory, ")")
		print("\nNo action performed...")
"""
def build_env():
	stuff
"""


def main():
	check_dependencies('virtualenv')

if __name__ == "__main__":
	main()
