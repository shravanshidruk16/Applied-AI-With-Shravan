import logging
"""
Here we need to configure our logging settings before actually using it

logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("This is a debug message")
logging.info("This is a information message - It tells everything is going as per plan")
logging.error("This is an error msg indicating some error occured")
logging.warning("This is a warning messsage")
logging.critical("This is a critical message")

"""

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="Date: %d-%m-%Y Time: %H:%M:%S"
)

logging.debug("This is a debug message")
logging.info("This is a information message - It tells everything is going as per plan")
logging.error("This is an error msg indicating some error occured")
logging.warning("This is a warning messsage")
logging.critical("This is a critical message")