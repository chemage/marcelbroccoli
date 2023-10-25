#!.venv/bin/python
# file : errorcodes.py
# Error codes for script


'''
Error codes for script exit.
The principle is to add them together.
'''
SUCCESS         = 0
GENERIC_ERROR   = 1
ENV_LOAD_ERROR  = 2
LOG_SETUP_ERROR = 4


# start with errorcode = 0
errorcode = SUCCESS


'''
Main Attraction
'''
if __name__ == '__main__':
  print("This script is a module.")
