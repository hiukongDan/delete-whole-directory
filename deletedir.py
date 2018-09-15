#!/usr/bin/python
"""
deletedir.py: This script is used for deleting a directory 
and all the subdirectories and files contained in it.
"""

import sys as _sys
import os  as _os

def deleteAll(_directory):
    """
    deleteAll: A recursive function to delete all files contained 
    in a directory system.
    """
    _os.chdir(_directory)
    _all = _os.popen('echo * .*').read().split()
    
    for _node in _all:
        if _node == '.' or _node == '..' or _node == '*':
            pass
        elif _os.system('rm ' + _node):
            deleteAll(_node)

    _os.chdir('..')
    _os.system('rmdir ' + _directory)

if __name__ == '__main__':
    import deletedir
    _all = _sys.argv[1:]
    for _directory in _all:
        print("Removing: %s") % (_directory)
        deletedir.deleteAll(_directory)
        print("Complete\n")
