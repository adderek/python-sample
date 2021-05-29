#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s|%(levelname)s|%(funcName)s|%(message)s')  # add filemode='w' to overwrite instead of appending
log = logging.getLogger(__name__)

import inspect  # We will try to extract function name.... and then try a better option


def not_wrapped_main():
    log.info("starting %s", inspect.stack()[0].function)

    log.debug("Hello")

    ret_val = "ret val"
    log.info("ending %s returning '%s'", inspect.stack()[0].function, ret_val)
    return ret_val


# Let's try to create a DECORATOR (a wrapper function)
def my_wrapper(func):
    def wrap(*args, **kwargs):
        log.info("%s starting", func.__name__)  # Notice we don't need to extract function name from the stack (using inspect.stack or frame info)
        result = func(*args, **kwargs)
        log.info("%s ending (returning '%s')", func.__name__, result)
        return result
    return wrap

@my_wrapper
def wrapped_main():
    log.debug("Hello")
    return "ret val"


print(not_wrapped_main())
print(wrapped_main())

