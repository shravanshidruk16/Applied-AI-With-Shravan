import logging

# Configuring settings
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="Date: %d-%m-%Y Time: %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} : {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b} : {result}")
    return result

def multiplty(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} * {b} : {result}")
    return result

def division(a,b):
    try :
        result = a/b
        logger.debug(f"Subtracting {a} - {b} : {result}")
        return result
    except ZeroDivisionError:
        logger.error("Error occured : b is zero")
        return None
    
if __name__ == "__main__":
    logger.info("Program starts from main method")
    add(10,15)
    subtract(15,10)
    multiplty(2,3)
    division(4,0)

