#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/balldontlie/")
sys.path.insert(0,"/var/www/balldontlie/balldontlie/")

import logging
logging.basicConfig(stream=sys.stderr)

from balldontlie import app as application
