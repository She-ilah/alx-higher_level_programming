#!/usr/bin/python3
"""Function defines the Pascals triangle"""


def pascal_triangle(n):
    """"Returns list of integers representing the Pascal’s triangle"""
    if n <= 0:
        return []
    temp = []
    hold = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(hold[j] + hold[j - 1])
        hold = row
        temp.append(row)
    return temp
