#!/usr/bin/env python3
##
# EPITECH PROJECT, 2023
# error handling
# File description:
# Return 84 in case of error. Else return 0.
##

import sys
from pathlib import Path


def error_output(str):
    print(str, file=sys.stderr)
    return 84


def check_arguments(argv):
    if len(argv) != 10:
        raise Exception("Invalid number of arguments (./307multigrains -h)")
    for i in range(1, len(argv)):
        if not argv[i].isnumeric():
            raise Exception("Invalid argument (not an integer number)")


def error_handling(argv):
    check_arguments(argv)
    return 0
