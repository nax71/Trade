import signal
import time
from lib import logger
from exceptions import TimeOutException


def alarm_handler(signum, frame):
    logger.info(f"ALARM signal recevived {signum}")
    raise TimeOutException()


def my_function_to_timeout():
    for sec in range(20):
        logger.info(f"{sec}")
        time.sleep(1)


def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(8)
    logger.info("Start Program")
    try:
        my_function_to_timeout()
    except TimeOutException as ex:
        logger.critical(ex.__doc__)
    signal.alarm(0)
    logger.info("End Program")


if __name__ == "__main__":
    main()
