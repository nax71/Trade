import argparse
import logging
from log_conf import Logger


class VerboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
        logger.info(f'values = {values} : option_string = {option_string}')

        # call the function
        func_ext = option_string.replace("--", "")
        return globals()['subcommand_' + func_ext](values)


def subcommand_input(value: int):
    logger.info(f"call input function with parameter: values={value}")
    logger.debug(f"call input function with parameter: values={value}")


def main():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument(
        '--input',
        action=VerboseStore,
        type=int,
        required=True,
        help="Input value for input option")
    my_parser.add_argument(
        '--debug',
        action="store_true",
        help="Add debug traces")
    args = my_parser.parse_args()

    # set the debug level
    if args.debug:
        for handler in logger.rootLogger.handlers:
            if isinstance(handler, type(logging.StreamHandler())):
                handler.setLevel("DEBUG")
                logger.debug('Debug logging enabled')


if __name__ == "__main__":
    logger = Logger()
    main()
