import sys
import logging
from datetime import datetime
from definitions import CONSTANTS


class Logger:
    def __init__(self, levelName="INFO"):
        logFormatter = logging.Formatter(
            "%(asctime)s [%(levelname)-8.8s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )

        CONSTANTS.LOG_PATH.mkdir(parents=True, exist_ok=True)
        date_time = datetime.now().strftime("%d-%m-%Y")
        fileName = f"trace_{date_time}"
        self.rootLogger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler(
            "{0}/{1}.log".format(CONSTANTS.LOG_PATH, fileName)
            )
        fileHandler.setFormatter(logFormatter)
        fileHandler.setLevel(logging.DEBUG)
        self.rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logFormatter)
        consoleHandler.setLevel(logging._nameToLevel[levelName])
        self.rootLogger.addHandler(consoleHandler)
        # print(f"set level to {logging._nameToLevel[levelName]}")
        self.rootLogger.setLevel(logging.DEBUG)

    def info(self, message):
        self.rootLogger.info(f"{message}")

    def warning(self, message):
        self.rootLogger.warning(f"{message}")

    def critical(self, message):
        self.rootLogger.critical(f"{message}")

    def debug(self, message):
        self.rootLogger.debug(f"{message}")
