import os
import sys
import emccanon 
import interpreter


def __init__(self):
    print("__init__")
    emc_methods = [name for name, val in interpreter.__dict__.iteritems() if callable(val)]
    interp_methods = [name for name, val in interpreter.__dict__.iteritems() if callable(val)]

    print(emc_methods)
    print(interp_methods)

    print(self.params[5190])
    print(self.params[5191])
    print(self.params[5192])
    print(self.params[5193])
    print(self.params[5194])
    print(self.params[5195])

    if hasattr(interpreter, 'this'):
        if self is not interpreter.this:
            print("__init__: self not is this")
    else:
        print("__init__: no 'this' attribute")
