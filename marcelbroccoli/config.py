#!.venv/bin/python
# Custom config module.

# system modules
import logging
import json

# pip modules
import dotenv

# current module
from . import errorcodes
from . import logger


'''
Configuration will be available through this variable
In your script, write:

import marcelbroccoli.config as config
config.data = config.load_config_file('your-config-file.json')
print(config.data['your-config-variable'])

In this way you can use the configuration in functions without passing it as argument.
'''
data = {}


# change logger name for module
logger = logging.getLogger(__name__)


'''
Load configuration file
'''
def load_config_file(cfg_file):
	cfg = None
	try:
		with open(cfg_file) as f:
			cfg = json.load(f)
	except Exception as e:
		if logger is not None:
			logger.error("Error: could not load configuration file '{}'. {}".format(cfg_file, e))
		else:
			print("Error: could not load configuration file '{}'. {}".format(cfg_file, e))

	return cfg


'''
Read the app access token from .env file
'''
def load_env():
	errorcode = errorcodes.SUCCESS
	try:
		if dotenv.load_dotenv():
			logger.debug("Successfully loaded '.env'.")
		else:
			logger.error("There was an issue loading the '.env' file.")
	except Exception as e:
		logger.error("Could not load '.env' file. {}".format(e))
		errorcode = errorcodes.ENV_LOAD_ERROR
	
	return errorcode


'''
Main attraction!
'''
if __name__ == "__main__":
	load_config_file('config.json')
