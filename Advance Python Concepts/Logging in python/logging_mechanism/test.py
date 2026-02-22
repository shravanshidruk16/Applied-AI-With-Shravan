from logger import logging

def addition(a,b):
    logging.debug("Addition operation is taking place")
    return a+b

if __name__ == "__main__":
    logging.info("Main section execution starts!")
    addition(10,15)


