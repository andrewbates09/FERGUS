'''
Library for doing fun things with computers.
'''

__author__	= 'Andrew M Bates'
__version__	= '0.001'

import io, os, sys


# the core imports go here


# this should go in in the mods dir
try:
	'''IF RASPBERRY PI & HAS A GPIO BOARD'''
	import RPi.GPIO as RPi

except ImportError:
	pass
