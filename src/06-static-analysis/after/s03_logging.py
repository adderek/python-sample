#!/usr/bin/python3
'''Example showing how you could use logging in your apps'''

import logging
# This library is rather poorly implemented :(

import sys  # we will use it for loguru (or custom keyword in 'logging')

from loguru import logger
# Don't reinvent the wheel...
# or do it as a separate project and share over the internet
# `sudo apt install pip` (or pip3) and `pip install loguru`


def main_using_python_logger():
    '''Main block using python logger'''
    logging.basicConfig(
            filename="logging.log",
            # filemode='w'  # to overwrite file instead of appending
            # stream=sys.stderr  # we used stream in previous script
            level=logging.DEBUG,
            format='%(asctime)s|%(levelname)s|%(message)s',
            # Rule of a thumb: always use international standard formats.
            #   ISO-8601 is a document worth reading.
            #   asctime is not following that rule
            datefmt='%Y-%m-%dT%H:%M:%S'
            # Custom format... does not support fractional part
            )
    # But we can create our own "keywords" like %(isotime)s
    #   but this shows that logging is a poor implmementation :(

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.debug("Hello builtin")


def main_using_loguru():
    '''Main block using loguru logger'''
    logger.debug("Hello")

    # This adds an extra "sink" printing to sys.stderr
    logger.add(
            sys.stderr,
            format="{time}|{level}|{message}",
            filter="__main__", level="DEBUG")

    # We could add more sinks if needed
    # There are many options to use in rotation value - see doc
    # logger.add("filename", rotation="10 MB", compression="zip")

    logger.debug("World")
    # This message will be printed to stderr using
    # default sink and again using second sink


if __name__ == '__main__':
    main_using_python_logger()
    main_using_loguru()
