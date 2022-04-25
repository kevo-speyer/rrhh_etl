import logging
import datetime
import sys

def handle_unexpected_exception(exc_type, exc_value, exc_traceback):
    """Runs anytime an exception occurs."""
    if issubclass(exc_type, KeyboardInterrupt):
        #Will call default excepthook
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    #TODO send mail about error
    #Create a critical level log message with info from the except hook.
    logging.error("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))

def init_logging():
    """Configure logger and handle exceptions"""
    current_time = datetime.datetime.now()
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(f"/tmp/{current_time}_etl.log"),
            logging.StreamHandler()
        ]
    )
    #In case of exception, run the exception handler 
    sys.excepthook = handle_unexpected_exception



