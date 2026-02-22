import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="addition_function.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="Date: %d-%m-%Y Time: %H:%M:%S"
)
