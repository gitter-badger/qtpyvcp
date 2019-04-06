import os
import sys
import emccanon 
import interpreter


def __init__(self):
    print("__init__")

    methods = [name for name, val in interpreter.__dict__.iteritems() if callable(val)]

    print(methods)

    if hasattr(interpreter, 'this'):
        if self is not interpreter.this:
            print("__init__: self not is this")
    else:
        print("__init__: no 'this' attribute")
