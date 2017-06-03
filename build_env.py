#!/usr/bin/env python3

"""
Synopsis:
---------
A script to setup virtulenv for a new project.

- creates a new project directory
- installs a package into the a virtualenv project directory

Constants:
----------
CONSTANT_1 = flag to control what the script will do
CONSTANT_2 = the virtualenv directory or the name of the directory to create
CONSTANT_3 = the package name to install

Flags:
------
-n = create a new project directory and setup virtualenv for this project
-i = install a package into the specified virtualenv directory
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
	Name:	build_env.py script
	-----

	Usage: -h (prints this help screen)
	------
	This script will create a new project directory and setup virtualenv
	under this directory.  This script has only been tested on linux systems
	(mint 18).

	The default directory path this script uses is:
	/home/<current user>/scripts/

	New project directories will be created in the following location:
	"/home/<current user>/scripts/<newProjectName>"

	The virtualenv project directory is:
	"/home/<current user>/scripts/<newProjectName>/env"

	Examples:
	---------
	Create a new virtualenv environment in <newProjectName> directory
	$ build_env.py -n newProjectName

	Install a package into the <newProjectName> virtualenv directory
	$ build_env.py -i newProjectName packageName
	"""
	)

def check_dependencies(library):
	"""
	The virtualenv python3 library is required and the script prompts to install
	the package if it is not already installed.
	"""
	try:
		import virtualenv
		print("Dependencies are already met, python3 package (virtualenv) is "\
		"installed globally.")
	except ImportError as e:
		user_choice = input("The required python3 library (virtualenv) is not "\
		"installed globally, do you wish to install this now?: (y|n) ")
		while not (user_choice == "y" or user_choice =="n"):
			user_choice = input("Please enter a valid option, install python3 "\
			"package (virtualenv) globally? (y|n) ")
		if user_choice == "y":
			subprocess.call(['pip3', 'install', library])
		else:
			print("\nThe virtualenv library is a requirement to run this "\
			"script, please install this package globally before running this "\
			"script again or choose \"y\" when prompted.")
			sys.exit(1)

def create_project_directory():
	"""
	Check if a project directory already exists and creates it if it does not.
	"""
	default_dir = os.path.expanduser("~") +"/scripts/"
	new_directory = default_dir + CONSTANT_2
	print("")
	print("Checking if the project directory exists (",CONSTANT_2,"), if "\
	"not it will be created in the following location: ", default_dir)
	if not os.path.exists(new_directory):
		print("\nCreated project directory: {0}".format(new_directory))
		os.makedirs(new_directory)
	else:
		print("\nDirectory already exists! {0}".format(new_directory))
		print("\nNo action performed...")
	return new_directory


def install_package(project_directory, package_name):
	"""
	Install a specified python library in a specific virtualenv	directory.
	"""
	pip_binary = project_directory + "/env/bin/pip3"
	# subprocess out to get the list of installed libraries
	get_virtualenv_packages = subprocess.Popen([pip_binary, 'freeze'], \
	stdout=subprocess.PIPE)
	# read list of installed packages from stdout
	installed_packages = (get_virtualenv_packages.stdout.read()).split()
	# convert the byte string output to unicode
	installed_packages = [(i).decode() for i in installed_packages]
	# check if the requested package is already installed
	if any(package_name in packages for packages in installed_packages):
		print("The > {0} < package is already installed.".format(package_name))
	else:
		print("Installing the > {0} < package.".format(package_name))
		subprocess.call([pip_binary, 'install', package_name])

def setup_python3_binaries(project_directory):
	"""
	Check if python3 binaries are installed in the specified virtualenv
	directory.
	"""
	python3_inst = "n"
	environment_dir = project_directory + "/env"
	if not os.path.exists(project_directory + "/env/bin/python3"):
		print("Installing python3 binaries to: \n".format(environment_dir))
		subprocess.call(['virtualenv', '-p', 'python3', environment_dir])
	else:
		print("Python3 binary already exists in the project directory {0} no "\
		"action taken...".format(project_directory))

def main():
	if (len(argv) < 2 or len(argv) > 4) or CONSTANT_1 == "-h":
		build_env_help()
	# creates new project directory
	elif (CONSTANT_1 == "-n" and len(argv) == 3):
		check_dependencies('virtualenv')
		project_directory = create_project_directory()
		setup_python3_binaries(project_directory)
	# installs a package
	elif (CONSTANT_1 == "-i" and len(argv) == 4):
		package_name = CONSTANT_3
		check_dependencies('virtualenv')
		project_directory = create_project_directory()
		setup_python3_binaries(project_directory)
		install_package(project_directory, package_name)
	else:
		build_env_help()

if __name__ == "__main__":
	main()
