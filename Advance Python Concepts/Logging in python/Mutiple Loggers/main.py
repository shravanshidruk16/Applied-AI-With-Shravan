import logging

# Creating a logger for module 1

logger1 = logging.getLogger("Module 1")
logger1.setLevel(logging.DEBUG)


# Creating a logger for module 2

logger2 = logging.getLogger("Module 2")
logger2.setLevel(logging.WARNING)

# Configuring the basic setting of the logger

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="Date: %d-%m-%Y Time: %H:%M:%S"
)


# Log messages with different loggers
logger1.debug("This is debug message for module 1")
logger2.warning("This is a warning message for module 2")
logger2.error("This is a error message")

print("""
    Here the key takeaways are :
    Firstly root used to come but now module 1 or the module name will come   
    So that you can use multiple types of logs and debug later on the activity
"""
)