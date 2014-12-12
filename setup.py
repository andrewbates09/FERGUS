import os
import sys

# I plan on looking to switching to setuptools in the future
# from setuptools import setup, find_packages
from distutils.core import setup, Extension

if sys.version_info < (3, 4):
	print('FERGUS requires python 3.4 or later. You are currently using python ' + sys.version)
	sys.exit(1)

import fergus

setup(
	name			= 'FERGUS',
	author			= 'Andrew M Bates',
	author.email	= 'andrewbates09@gmail.com',
	version			= '0.001',
	description		= 'Finally an Extendable Responsive Generally Useful System',
	keywords		= 'fergus',
	url				= 'https://github.com/andrewbates09/FERGUS/',
	packages		= ['fergus'],
	classifiers		= [	'Natural Language :: English',
						'Operating System :: POSIX :: Linux',
						'Programming Language :: Python'
						'Programming Language :: Python :: 3.4'],
)
