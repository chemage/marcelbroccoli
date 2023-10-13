#!.venv/bin/python
# Custom functions module.

# system modules
from __future__ import print_function
from datetime import datetime
import logging
import os

# pip modules

# custom modules
import marcelbroccoli.errorcodes as marcelec
import marcelbroccoli.functions as marcelfn
import marcelbroccoli.logger as marcellg


if __name__ == "__main__":

    # set working dir
    working_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(working_dir)

    s = "Bonjour, je m'appelle Marcel."
    p1 = "Bonjour"
    p2 = "bonjour"

    print(s, p1)
    print("Case sensitive: True = ", marcelfn.starts_with(s, p1, True))
    print(s, p2)
    print("Case sensitive: False = ", marcelfn.starts_with(s, p2, False))
    print(s, p2)
    print("Case sensitive: True = ", marcelfn.starts_with(s, p2, True))

    marcelfn.str2datetime("2023-10-07 23:56:34.0000")


    marcelfn.load_env()

