
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 16:56:55 2016

@author: Justin Stuart
"""

from random import random
import matplotlib.pyplot as plt

EMPTY=0
TREE=1
BURNING=2
n=20

def main():
    i=0;
    t=30
    result = initForest(n)
    plt.imshow(result, cmap=plt.cm.Oranges)
    plt.colorbar()
    plt.show()

    while i < t:
           # print(result)
            result = fire(result);
            i=i+1
            image = result
            plt.imshow(image, cmap=plt.cm.Oranges)
            plt.colorbar()
            plt.show()


def initForest(n):
    probTree =  0.8    # probability of grid forest occupied by tree
                       # (value 1); i.e., tree density
    probBurning = 0.1  # probability that a tree is burning (value 2);
                       # i.e., fraction of burning trees
    forest = [[] for i in range(n)]
    i=0
    j=0
    for i in range(n):
        for j in range(n):
            if random() <= probTree:
                if random() <= probBurning:
                    forest[i].append(BURNING)
                else:
                    forest[i].append(TREE)
            else:
                forest[i].append(EMPTY)
    return forest

def fire(forest):
    probImmune = 0.5
    probLightning = 0.0

    forest2 = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if forest[i][j] == EMPTY:
                forest2[i].append(EMPTY)
            elif forest[i][j] == BURNING:
                forest2[i].append(BURNING)
            else: forest2[i].append(TREE)

    i=0
    j=0
    for i in range(n):
        for j in range(n):
            if (forest[i][j] == EMPTY):
                forest2[i][j] = EMPTY

            elif (forest[i][j] == BURNING):

                if (i>0 and forest[i-1][j]==TREE):
                    if random() >= probImmune:
                        forest2[i-1][j] = BURNING

                if (i<(n-1) and forest[i+1][j]==TREE):
                    if random() >= probImmune:
                        forest2[i+1][j] = BURNING

                if (j>0 and forest[i][j-1]==TREE):
                    if random() >= probImmune:
                        forest2[i][j-1] = BURNING

                if (j<(n-1) and forest[i][j+1]==TREE):
                    if random() >= probImmune:
                        forest2[i][j+1] = BURNING

                forest2[i][j]=EMPTY

            elif(forest[i][j] == TREE):
                if(random() <= (probLightning*(1-probImmune))):
                    forest2[i][j] = BURNING

    return forest2

main()
