#!/usr/bin/env python3

"""
Script to setup a project with virtulenv

- creates project direectory
- sets up virtualenv in project directory
- activates the environments

- checks if the project directory already exists
- if directory exists the script will install libraries to that directory
- script can be run with a -i flag (install library) and will install to the
specified project dir

Constants

1 = flag for what the script should (is being told) to do
2 = the virtualenv directory to create or where a new package will be installed
3 = the package name to install


Flags:

-n = create a new project directory and setup virtualenv for this project
-i = install a package into the specified virtualenv directory
-c = check if project directory exists and python3 binaries are installed in it


"""

from __future__ import print_function
import sys
from sys import argv
import subprocess
import os
import pwd

try:
	CONSTANT_1 = argv[1]
	CONSTANT_2 = argv[2]
	CONSTANT_3 = argv[3]
except IndexError as not_enough_arguments:
	pass

def build_env_help():
	print ("")
	print (
	"""
	build_script.py script
	Usage: -h (prints this help screen)
	===================================

	This script will create a new project directory and setup virtualenv
	under this directory.  It has been tested only on linux systems (mint 18).

	The default directory path this script uses is:
	/home/<current user>/scripts/

	New project directories will be created in the folowing location:
	"/home/<current user>/scripts/<newProjectName>"

	Examples:
	=========

	Create a new virtualenv environment in <newProjectName> directory
	: build_env.py -n newProjectName

	Install a package into the newProjectName virtualenv directory
	: build_env.py -i newProjectName packageName

	Check that python3 binaries are installed in the virtaulenv <newProjectName>
	directory
	: build_env.py -c newProjectName
	"""
	)

def check_dependencies(library):
	"""
	The build environment script requires the virtualenv python library and
	prompts to install the package if it is not already installed.
	"""
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
	"""
	Function checks if a project directory already exists and creates it if
	it does not.
	"""
	default_dir = os.path.expanduser("~") +"/scripts/"
	new_directory = default_dir + CONSTANT_2
	print("")
	print("Checking if the project directory exists (",CONSTANT_2,"), if "\
	"not it will be created in the following location: ", default_dir)
	if not os.path.exists(new_directory):
		print("\nCreated project directory: ", new_directory)
		os.makedirs(new_directory)
	else:
		print("\nDirectory already exists! (", new_directory, ")")
		print("\nNo action performed...")
	return new_directory

"""
def build_env():
	stuff
"""

def install_package(project_directory, package_name):
	"""
	Function installs a specified python library in a specific virtualenv
	directory.
	"""
	package_present = ""
	pip_binary = project_directory + "/env/bin/pip"
	test = project_directory + "/env/bin/"
	try:
		import package_name
		package_present = "y"
	except ImportError as e:
		user_choice = input("The requested package is not installed, do you "\
		"wish to install this package now?: (y|n) ")
		while not (user_choice == "y" or user_choice == "n"):
			user_choice = input("Please enter a valid option, do you want to "\
			"install the ",package_name, " package (y|n) ")
		if user_choice == "y":
			#call pip from the virtualenv dir
			print("Installing",package_name,"package for the project in the "\
			"following directory: ", project_directory)
			subprocess.call([pip_binary, 'install', package_name])
		else:
			print("\nYou have chosen NOT to install the following python "\
			"package: ", package_name, " . The ", project_directory, " project"\
			" directory has NOT been modified.")
			sys.exit(1)
	if package_present == "y":
		print("Package ",package_name, "is already installed in: "\
		"",project_directory, " project directory")
	else:
		sys.exit(1)

"""
def check_running_in_virtualenv():
"""
#Funciton that checks if a virtualenv is activated
"""
	import sys
	if hasattr(sys, 'real_prefix'):
		#activate the specified virtualenv
	else:
		continue
"""

def setup_python3_binaries(project_directory):
	environment_dir = project_directory + "/env"
	if not os.path.exists(project_directory + "/env/bin/python3"):
		print("Installing python3 binaries to: \n", environment_dir)
		subprocess.call(['virtualenv', '-p', 'python3', environment_dir])
	else:
		print("Python3 binary already exists in the project directory ",\
		environment_dir," no action taken...")
		sys.exit(1)

def main():
	#try:
	if not argv[1]:
		build_env_help()
	if argv[1] == "-h":
		build_env_help()
	elif argv[1] == "-c":
		check_dependencies('virtualenv')
		create_project_directory()
		setup_python3_binaries(create_project_directory())
	elif argv[1] == "-n":
		check_dependencies('virtualenv')
		create_project_directory()
		setup_python3_binaries(create_project_directory())
	elif argv[1] == "-i":
		check_dependencies('virtualenv')
		project_directory = create_project_directory()
		setup_python3_binaries(create_project_directory())
		install_package(project_directory, package_name)
	else:
		build_env_help()
	#except IndexError as not_enough_arguments:
		#build_env_help()





if __name__ == "__main__":
	main()
