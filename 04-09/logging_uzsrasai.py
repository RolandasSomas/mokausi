import logging
from time import time

data = time()
filename = f"loggers{data}_data.log"
logging.basicConfig(
    level=logging.DEBUG,
    filename=filename,
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def calculate_numbers(*args):
    result = {"Lyginiai": 0, "Nelyginis": 0}
    for n in args:
        if not isinstance(n, int):
            logging.error(f"Not correct data type{n}")
            continue
        if n % 2 == 0:
            logging.info(f"{n} pridetas prie lyginiu")
            result["Lyginiai"] += n
        else:
            logging.info(f"{n} pridetas prie nelyginiu")
            result["Nelyginis"] += n
    logging.info(f"Grazinama reiksme {result}")
    return result


numbers = [1, 2, 3, 4, 5, 6, 0]
print(calculate_numbers(*numbers))
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
