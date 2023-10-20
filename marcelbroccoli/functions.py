#!.venv/bin/python
# Custom functions module.

# system modules
from __future__ import print_function
from datetime import datetime
import json

# pip modules
import dotenv

# current module
from . import errorcodes
from . import logger


'''
Read the app access token from .env file
'''
def load_env(logger=logger.logger):
	try:
		if dotenv.load_dotenv():
			logger.debug("Successfully loaded '.env'.")
		else:
			logger.error("There was an issue loading the '.env' file.")
			return errorcodes.ErrorCodes.SUCCESS
	except Exception as e:
		logger.error("Could not load '.env' file. {}".format(e))
	return errorcodes.ErrorCodes.ENV_LOAD_ERROR


'''
Load configuration file
'''
def load_config_file(cfg_file, logger=logger.logger):
	cfg = None
	try:
		with open(cfg_file) as f:
			cfg = json.load(f)
	except Exception as e:
		logger.error("Error: could not load configuration file '{}'. {}".format(cfg_file, e))

	return cfg


'''
Test if a string starts with pattern
- string: string to search in
- pattern: string to search for in source start
- casesensitive: if set to false, set source and value to lower (default: True)
'''
def starts_with(string:str, pattern:str, casesensitive:bool=True):
    string = str(string)
    pattern = str(pattern)

    # check if string starts with pattern
    if len(pattern) <= len(string):
        if casesensitive:
            return string[0:len(pattern)] == pattern
        else:
            return string[0:len(pattern)].lower() == pattern.lower()
    
    # string is shorter than pattern
    else:
        return False


'''
Convert from all date and date time sources to date object.
'''
def str2datetime(str:str, format:str='%Y-%m-%d %H:%M:%s.%f') -> datetime:
    try:
        return datetime.fromisoformat(str)
    except:
        pass

    try:
        return datetime.strptime(str.replace(' ', ''), format).date()
    except:
        pass

    try:
        return datetime.strptime(str.replace(' ', ''), format).date()
    except:
        pass

'''
Convert date to string in HomeBank format.
'''
def datetime2str(dt:datetime, format:str='%d-%m-%Y %H:%M:%s.%f') -> str:
    return dt.strftime(format)


'''
Main attraction!
'''
if __name__ == "__main__":
    s = "Bonjour, je m'appelle Marcel."
    p1 = "Bonjour"
    p2 = "bonjour"

    print(s, p1)
    print("Case sensitive: True = ", starts_with(s, p1, True))
    print(s, p2)
    print("Case sensitive: False = ", starts_with(s, p2, False))
    print(s, p2)
    print("Case sensitive: True = ", starts_with(s, p2, True))
