from log import *


def check_interger(num):
    # True if variable is interger
    result = False
    if isinstance(num, int) and not(isinstance(num, bool)):
        result = True
    return result


def classname(klass):
    return f'class {klass.__class__.__name__}: '
