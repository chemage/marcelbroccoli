#!.venv/bin/python
# Custom logger module for easy setup.

# system modules
# from __future__ import print_function
import logging
import logging.handlers

# pip modules
import colorama

# custom modules

# current module
from . import errorcodes as ec
from . import functions
# from . import logger


# logging definitions
logger = logging.getLogger(__name__)
LOG_LEVEL = logging.ERROR
LOG_MAX_BYTES = 2000000
LOG_BACKUP_COUNT = 4


'''
Setup log with custom settings.
'''
def setup(logger:object, logfile:str, name:str=None, dtformat="%Y-%m-%d %H:%M:%s.%f", level:str=LOG_LEVEL, 
          maxbytes=LOG_MAX_BYTES, backupcount=LOG_BACKUP_COUNT,
          logformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s', errorcode=ec.errorcode):
  
  try:
    handler = logging.handlers.RotatingFileHandler(logfile, mode='a', encoding='utf-8', maxBytes=maxbytes, backupCount=backupcount)
    handler.setFormatter(Formatter(logformat, datefmt=dtformat))
    logger.addHandler(handler)
    logger.setLevel(level)

  except Exception as e:
    print("Error: could not setup logger. {}".format(e))
    errorcode = ErrorCodes.LOG_SETUP_ERROR

  logger.info("-------------------------------------------------------------------------------")
  return errorcode


'''
Write log entry if logger is set, otherwise print colored console message.
'''
def log(msg:str, logger=logger):
    # magenta
    if functions.starts_with(msg, 'critical', False):
        if logger is not None: logger.critical(msg)
        if logger.level > logging.CRITICAL: print(f"{colorama.Fore.MAGENTA}{msg}{colorama.Style.RESET_ALL}")

    # red
    elif functions.starts_with(msg, 'error', False):
        if logger is not None: logger.error(msg)
        if logger.level > logging.ERROR: print(f"{colorama.Fore.RED}{msg}{colorama.Style.RESET_ALL}")
    
    # yellow
    elif functions.starts_with(msg, 'warning', False):
        if logger is not None: logger.warning(msg)
        if logger.level > logging.WARNING: print(f"{colorama.Fore.YELLOW}{msg}{colorama.Style.RESET_ALL}")
    
    # green
    elif functions.starts_with(msg, 'successfully', False):
        if logger is not None: logger.info(msg)
        if logger.level > logging.INFO: print(f"{colorama.Fore.GREEN}{msg}{colorama.Style.RESET_ALL}")
    
    # green
    elif functions.starts_with(msg, 'debug', False):
        if logger is not None: logger.debug(msg)
        if logger.level > logging.DEBUG: print(f"{colorama.Fore.BLUE}{msg}{colorama.Style.RESET_ALL}")

    # no color
    else:
        if logger is not None: logger.info(msg)
        print(msg)

    
'''
Main attraction!
'''
if __name__ == "__main__":
    logger.log("Critical: HEEEEEELP !!")
