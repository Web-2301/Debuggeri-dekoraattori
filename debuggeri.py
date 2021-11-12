# -*- coding: utf-8 -*-
# Tiedosto: debuggeri.py
import functools
from datetime import datetime
debug = True

def debuggeri(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        if debug:
            now = datetime.now()
            msg = now.strftime("%Y-%m-%d %H:%M:%S") + ' '
            msg += function.__name__ + ' '
            if (args):
                msg += ''.join(args)
            if (kwargs):
                msg += ' ' + str(kwargs)[1:-1].replace(': ', ':')
            tulos = function(*args)
            msg += ",tulos:" + tulos
            tiedosto = open("debug_log.txt", "a", encoding="utf-8") 
            tiedosto.write(msg + "\n") 
            tiedosto.close() 
            # print(msg + "\n")
        return tulos
    return wrapper
