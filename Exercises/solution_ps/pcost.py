import os
import sys
import re
import csv

import decimal

# f = open("../../Data/portfolio.dat",'r')
# line = f.readline()
# f.close()
# print(line)

total_cost = 0
with open("../../Data/portfolio.dat",'r') as f:

    for i in f:

        # print(i)``
        
        breaking_characters = str(i).split(" ")
        # print(breaking_characters)
        # print(int(breaking_characters[1])*float(breaking_characters[2].partition('\n')[0]))
        total_cost = total_cost + int(breaking_characters[1])*float(breaking_characters[2].partition('\n')[0])
print(total_cost)
        # breaking_space = breaking_characters[1].split('')

        # print(str(i).split("'"))

    # line = str(f.readline())
    # print(line.split(' '))
    # print()
    # # f.close()
    # print(line)