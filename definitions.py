from pathlib import Path
from dataclasses import dataclass


@dataclass
class Definitions:
    ROOT_DIR = Path(__file__).parent
    CONFIG_PATH = ROOT_DIR.joinpath('conf')
    LOG_PATH = ROOT_DIR.joinpath("log")


CONSTANTS = Definitions()
