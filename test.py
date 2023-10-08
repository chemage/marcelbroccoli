#!.venv/bin/python
# Custom functions module.

# system modules
from __future__ import print_function
from datetime import datetime 
# from logging import getLogger, INFO, DEBUG, WARNING, ERROR, CRITICAL

# pip modules

# custom modules
import marcelbroccoli.functions
from marcelbroccoli.functions import starts_with, str2datetime
# from Marcel.marcel.functions import starts_with, str2datetime


if __name__ == "__main__":
    s = "Bonjour, je m'appelle Marcel."
    p1 = "Bonjour"
    p2 = "bonjour"

    print(s, p1)
    print("Case sensitive: True = ", marcelbroccoli.functions.starts_with(s, p1, True))
    print(s, p2)
    print("Case sensitive: False = ", starts_with(s, p2, False))
    print(s, p2)
    print("Case sensitive: True = ", starts_with(s, p2, True))

    str2datetime("2023-10-07 23:56:34.0000")
