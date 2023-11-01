#!.venv/bin/python
# Custom functions module.

# system modules
from datetime import datetime
import json
import os

# current module
from . import errorcodes
from . import logger


'''
Set working dir to folder and return working_dir
'''
def set_working_dir(folder:str) -> str:
	# get folder name if folder is a file
	if os.path.isfile(folder):
		folder = os.path.dirname(folder)

	# set working dir
	working_dir = os.path.abspath(folder)
	os.chdir(working_dir)
	
	# return working dir
	return working_dir


'''
Write JSON to file
'''
def write_json_file(data, fname:str):
	try:
		with open(fname, 'w', encoding='utf-8') as json_file:
			json.dump(data, json_file, ensure_ascii=False, indent=4)
		errorcode = 0
	except Exception as e:
		logger.error("Error: could not dump JSON to file '{}'. {}".format(fname, e))
		errorcode = -1
	return errorcode


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
