#!.venv/bin/python
# Custom functions module.

# system modules
from __future__ import print_function
from datetime import datetime 
# from logging import getLogger, INFO, DEBUG, WARNING, ERROR, CRITICAL

# pip modules
# import colorama

# custom modules
# from marcel.functions import startswith

# custom modules

# current module
# from errorcodes import ErrorCodes, errorcode
from .logger import *
# from . import *

# meta data
__author__ = "Marcel Gerber"
__date__ = "2023-10-08"
__version__ = "0.1.0"


'''
Read the app access token from .env file
'''
def load_env(logger=logger):
  try:
    dotenv.load_dotenv()
    return ErrorCodes.SUCCESS
  except Exception as e:
    log("Error: could not load '.env' file. {}".format(e), logger=logger)
    return ErrorCodes.ENV_LOAD_ERROR


'''
Test if a string starts with pattern
- string: string to search in
- pattern: string to search for in source start
- casesensitive: if set to false, set source and value to lower (default: True)
'''
def starts_with(str:str, pattern:str, casesensitive:bool=True):
    # check if string starts with pattern
    if len(pattern) <= len(str):
        if casesensitive:
            return str[0:len(pattern)] == pattern
        else:
            return str[0:len(pattern)].lower() == pattern.lower()
    
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
