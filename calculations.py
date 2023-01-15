#!/usr/bin/env python3
##
# EPITECH PROJECT, 2023
# maths
# File description:
# maths
##

import sys
from classes.Args import Args
from classes.Grains import Grains
from typing import List

F1 = 0
F2 = 1
F3 = 2
F4 = 3
P = 4
X1 = 0
X2 = 1
X3 = 2
X4 = 3
X5 = 4
X6 = 5
X7 = 6
X8 = 7
X9 = 8
B = 9

def create_tab(args: Args):
    tab = []
    l1 = [1, 0, 1, 0, 2, 1, 0, 0, 0, args.n1]
    l2 = [2, 2, 0, 1, 0, 0, 1, 0, 0, args.n2]
    l3 = [2, 1, 0, 1, 0, 0, 0, 1, 0, args.n3]
    l4 = [0, 0, 3, 1, 2, 0, 0, 0, 1, args.n4]
    l5 = [-args.po, -args.pw, -args.pc, -args.pb, -args.ps, 0, 0, 0, 0, 0]
    tab.append(l1)
    tab.append(l2)
    tab.append(l3)
    tab.append(l4)
    tab.append(l5)
    # tab.append([1, 2, 1, 0, 8])
    # tab.append([3, 2, 0, 1, 12])
    # tab.append([-2, -3, 0, 0, 0])
    return tab


def get_pivot(tab: List[List[float]], fertilizers: List[int]):
    pivot = 0
    jmin = tab[P][X1]
    jxmax = tab[F1][X1]
    for f in range(F2, P):
        if tab[f][X1] > jxmax:
            jxmax = tab[f][X1]
    i = F1
    j = X1
    for k in range(X2, B):
        if tab[P][k] < jmin:
            jmin = tab[P][k]
            j = k
        elif tab[P][k] == jmin:
            for f in range(F1, P):
                if tab[f][k] > jxmax:
                    jxmax = tab[f][k]
                    j = k
    # jxmax = tab[F1][j]
    # for f in range(F1, P):
    #     if tab[f][j] > jxmax:
    #         jxmax = tab[f][j]
    #         i = f
    imin: int = None
    for k in range(F1, P):
        if tab[k][j] != 0 and fertilizers[k] > 0 and tab[k][B] / tab[k][j] > 0:
            imin = tab[k][B] / tab[k][j]
            i = k
            break
    if imin == None:
        raise Exception("Stop: avoid division by zero")
    for k in range(F1, P):
        if tab[k][j] != 0 and tab[k][B] / tab[k][j] < imin and fertilizers[k] > 0 and tab[k][B] / tab[k][j] > 0:
            imin = tab[k][B] / tab[k][j]
            i = k
    pivot = tab[i][j]
    print(f"pivot: [F{i + 1}][x{j + 1}] = {pivot}\n", file=sys.stderr)
    return pivot, i, j


def is_one_negative_price(tab: List[List[float]]):
    for j in range (X1, B):
        if tab[P][j] < 0:
            return True
    return False


def display_tab(tab: List[List[float]]):
    y = ["F1", "F2", "F3", "F4", "P"]
    i = 0
    xs = [" ", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "b"]
    for x in xs:
        print("%10s, " % x, end="", file=sys.stderr)
    print("", file=sys.stderr)
    for l in tab:
        print("%10s, " % (y[i]), end="", file=sys.stderr)
        for n in l:
            print("%10.2f, " % (n), end="", file=sys.stderr)
        print("", file=sys.stderr)
        i += 1
    print("", file=sys.stderr)


def get_strx_from_int(i: int):
    xs = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "b"]
    return xs[i]


def get_strf_from_int(i: int):
    y = ["F1", "F2", "F3", "F4", "P"]
    return y[i]


def algo(tab: List[List[float]], fertilizers: List[int]):
    grains = Grains(0.0, 0.0, 0.0, 0.0, 0.0)

    display_tab(tab)
    z = 0

    final_values_i = [-1, -1, -1, -1, -1]

    while (is_one_negative_price(tab) and z < 10):
        # z += 1
        print("--------------------", file=sys.stderr)
        pivot, f, x = get_pivot(tab, fertilizers)
        price = tab[P][x]
        print(f"price: {tab[P][x]} (tab[P][{get_strx_from_int(x)}])\n", file=sys.stderr)
        for j in range(X1, B + 1):
            tab[f][j] = tab[f][j] / pivot
        for j in range(X1, B + 1):
            # print(f"tab[P][{get_strx_from_int(j)}] = {tab[P][j]} - {price} * {tab[f][j]}", file=sys.stderr)
            tab[P][j] = tab[P][j] - (price) * tab[f][j]
        for i in range(F1, P):
            if i != f and fertilizers[i] > 0:
                x_line = tab[i][x]
                for j in range(X1, B + 1):
                    # print(f"tab[{get_strf_from_int(i)}][{get_strx_from_int(j)}] = {tab[i][j]} - {x_line} * {tab[f][j]}", file=sys.stderr)
                    tab[i][j] = tab[i][j] - x_line * tab[f][j]
        display_tab(tab)
        final_values_i[f] = x

    for f, x in enumerate(final_values_i):
        if x == X1:
            grains.o = tab[f][B]
        elif x == X2:
            grains.w = tab[f][B]
        elif x == X3:
            grains.c = tab[f][B]
        elif x == X4:
            grains.b = tab[f][B]
        elif x == X5:
            grains.s = tab[f][B]

    return grains


def get_number_of_grains(args: Args):
    tab: List[List[float]] = create_tab(args)
    fertilizers = [args.n1, args.n2, args.n3, args.n4]
    grains: Grains = algo(tab, fertilizers)
    return grains
