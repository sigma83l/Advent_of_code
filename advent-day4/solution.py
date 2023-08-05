from itertools import count
import math
import numpy as np
import os

BASE_DIR = os.getcwd()  

def Binary_ToDecimal(input) :
    dnum = 0
    i = 1
    while input!=0:
        rem = input%10
        dnum = dnum + (rem*i)
        i = i*2
        input = int(input/10)
    return dnum


def cal (input) :
 i = 0
 while i <= 12 :
    zeros = 0
    ones = 0
    output = [0,0,0,0,0,0,0,0,0,0,0,0]
    for x in input :
        if x[i] == "1" :
            ones += 1
        else :
            zeros += 1 
    if zeros < ones :
        output[i] = 1
    else:
        continue
    i += 1
 return(output)

with open(BASE_DIR+ "\\advent-day4\\input.txt") as File :
    file = File.readlines()
file = [ l.strip() for l in file ]
ones = 0
zeros = 0
for x in file :
    if x[11] == "1" :
        ones += 1
    else :
        zeros += 1
# if ones > zeros :
#         print("ones :", ones)
# elif ones < zeros :
#         print("zeros :", zeros)
# else : 
#    566     print("equal")


print(Binary_ToDecimal(110111001001))