#!.venv/bin/python
# Custom logger module for easy setup.

# system modules
# from __future__ import print_function
import sys, os
import datetime
import logging
import logging.handlers

# pip modules
import colorama

# current module
from . import errorcodes as ec
from . import functions


# logging defaults
DT_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
LOG_FORMAT = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.ERROR
LOG_MAX_BYTES = 2000000
LOG_BACKUP_COUNT = 4


'''
Custom formatter to workaround compatibility issue between Linux and Windows
with the underlying C library interpreting time formatting.
'''
class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        return datetime.datetime.now().strftime(datefmt)
        # return custom_time()



class CustomLogger(logging.Logger):
    '''
    Initialize CustomLogger
    '''
    def __init__(self, name:str, level:int=0):
        logging.Logger.__init__(self, name, level=level)


    '''
    Setup log with custom settings.
    '''
    def configure(self, logfile:str, name:str, dtformat=DT_FORMAT, level:str=LOG_LEVEL, 
              maxbytes=LOG_MAX_BYTES, backupcount=LOG_BACKUP_COUNT,
              logformat=LOG_FORMAT, errorcode=ec.errorcode):

        try:
            logging.setLoggerClass(CustomLogger)
            if name is not None: logger = logging.getLogger(name)
            handler = logging.handlers.RotatingFileHandler(logfile, mode='a', encoding='utf-8', maxBytes=maxbytes, backupCount=backupcount)
            handler.setFormatter(CustomFormatter(logformat, datefmt=dtformat))
            self.addHandler(handler)
            self.setLevel(level)
            self.info("-------------------------------------------------------------------------------")
            self.debug("Successfully completed logger setup.")

        except Exception as e:
            print("Error: could not setup logger. {}".format(e))
            errorcode =ec.LOG_SETUP_ERROR
            raise e

        return errorcode


    '''
    Write log entry if logger is set, otherwise print colored console message.
    '''
    def log(self, level:int, msg:str):
        if level == logging.CRITICAL: self.critical(msg)
        elif level == logging.ERROR: self.critical(msg)
        elif level == logging.WARNING: self.warning(msg)
        elif level == logging.WARN: self.warn(msg)
        elif level == logging.DEBUG: self.debug(msg)
        elif level == logging.INFO: self.info(msg)
        else: self.info(msg)


    def critical(self, msg:str):
        logging.Logger.critical(self, msg)
        if self.level <= logging.CRITICAL:
            print(f"{colorama.Fore.MAGENTA}{msg}{colorama.Style.RESET_ALL}")


    def error(self, msg:str):
        logging.Logger.error(self, msg)
        if self.level <= logging.ERROR:
            print(f"{colorama.Fore.RED}{msg}{colorama.Style.RESET_ALL}")


    def warning(self, msg:str):
        logging.Logger.warning(self, msg)
        if self.level <= logging.WARNING:
            print(f"{colorama.Fore.YELLOW}{msg}{colorama.Style.RESET_ALL}")


    def warn(self, msg:str):
        logging.Logger.warning(self, msg)
        if self.level <= logging.WARN:
            print(f"{colorama.Fore.YELLOW}{msg}{colorama.Style.RESET_ALL}")


    def info(self, msg:str):
        logging.Logger.info(self, msg)
        if self.level <= logging.INFO:
            if functions.starts_with(msg, "successfully", False):
                print(f"{colorama.Fore.GREEN}{msg}{colorama.Style.RESET_ALL}")
            else:
                print(msg)


    def debug(self, msg:str):
        logging.Logger.debug(self, msg)
        if self.level <= logging.DEBUG:
            print(f"{colorama.Fore.CYAN}{msg}{colorama.Style.RESET_ALL}")



'''
Object definition
'''
logging.setLoggerClass(CustomLogger)
logger = logging.getLogger(__name__)


'''
Fix Colorama for Windows
'''
if sys.platform == 'win32':
    colorama.just_fix_windows_console()

    
'''
Main attraction!
'''
if __name__ == "__main__":
    # fix colorama for windows
    if sys.platform == 'win32':
      colorama.just_fix_windows_console() # not available in python3.6.8

    # set working dir to script dir
    working_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(working_dir)

    # define log file
    log_file = os.path.abspath('test_log.log')

    # setup logger
    errorcode = logger.configure(logfile=log_file, name=__name__, level=logging.INFO, dtformat="%Y-%m-%d %H:%M:%S")

    # start log
    logger.info("Welcome to the Logger Test Script.")
    logger.info("Log file is '{}'".format(log_file))
    print("Log level: {}".format(logger.level))

    logger.info("Script execution completed with exit code {}.".format(errorcode))
    sys.exit(errorcode)

