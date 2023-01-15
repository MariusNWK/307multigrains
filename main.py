#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## main
## File description:
## maths
##

import sys
from usage import usage
from error_handling import error_handling
from error_handling import error_output
from project import project


def main(argv):
    if (len(argv) == 2 and argv[1] == "-h"):
        usage()
        return 0
    try:
        error_handling(argv)
        project(argv)
    except Exception as e:
        return error_output(e)
    return 0
