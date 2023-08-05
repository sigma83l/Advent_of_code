from itertools import count
import math
import numpy as np
import os

from sympy import SeqMul

BASE_DIR = os.getcwd()  

class Board :
    def __init__(self, *nummatrix):
        self.nummatrix = nummatrix
        self.zerosmatrix = np.zeros(shape=(5,5), dtype="i")
        self.wins = False

    def new(self, num):
        for arr, Index in enumerate(self.nummatrix): 
            for mem, index in enumerate(arr):
                if mem == num :
                    self.zerosmatrix[Index, index] = 1
                else :
                    continue

    def wins(self, List):
            List = [j.index() for i in self.zerosmatrix for j in i if j==1]
            for i in List:
                return i

    def cal_score():
        pass

    def __str__(self):
        for i in self.nummatrix:
            for j in i :
                print(j)



with open(BASE_DIR+ "\\advent-day5\\input.txt") as file:
    # inputs = file.readlines()[0].split(",")
    # inputs[len(inputs)-1] = inputs[len(inputs)-1].replace("\n", "")
    # inputs = [int(i) for i in inputs]
    # print(inputs)
    BoardList = []
    templates = [ l.strip() for l in file.readlines()[1:] ]
    Indexlist = [i for i in range(0, len(templates), 6)]
    for i in range(len(Indexlist)):
        for j in range(Indexlist[i-1], Indexlist[i]):
            BoardList.append(Board(templates[j]))

    # for i in range(1,2):
    #     BoardList[i].__str__() 
    print(templates)
