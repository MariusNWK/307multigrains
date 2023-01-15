#!/usr/bin/env python3
##
# EPITECH PROJECT, 2023
# maths
# File description:
# maths
##

from classes.Grains import Grains
from classes.Args import Args
from calculations import get_number_of_grains


def print_ressources(args: Args):
    print(f"Resources: {args.n1} F1, {args.n2} F2, {args.n3} F3, {args.n4} F4")


def print_grains(args: Args, grains: Grains):
    print("Oat: {} units at ${}/unit".format("{:.2f}".format(grains.o) if grains.o > 0 else "{:.0f}".format(grains.o), args.po))
    print("Wheat: {} units at ${}/unit".format("{:.2f}".format(grains.w) if grains.w > 0 else "{:.0f}".format(grains.w), args.pw))
    print("Corn: {} units at ${}/unit".format("{:.2f}".format(grains.c) if grains.c > 0 else "{:.0f}".format(grains.c), args.pc))
    print("Barley: {} units at ${}/unit".format("{:.2f}".format(grains.b) if grains.b > 0 else "{:.0f}".format(grains.b), args.pb))
    print("Soy: {} units at ${}/unit".format("{:.2f}".format(grains.s) if grains.s > 0 else "{:.0f}".format(grains.s), args.ps))


def print_total(args: Args, grains: Grains):
    total = grains.o * args.po + grains.w * args.pw + grains.c * args.pc + grains.b * args.pb + grains.s * args.ps
    print("Total production value: ${}".format("{:.2f}".format(total) if total > 0 else "{:.0f}".format(total)))


def project(argv):
    args = Args(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]), int(argv[7]), int(argv[8]), int(argv[9]))
    print_ressources(args)
    print("")
    grains: Grains = get_number_of_grains(args)
    print_grains(args, grains)
    print("")
    print_total(args, grains)
    return 0
