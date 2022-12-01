# Ecrire une fonction en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 +
# 4! / 4 + 5! / 5 en utilisant la fonction.
# from ex2 import facto
from ex2 import facto
def fun3(x):
    somme = 0
    while(x!=0):
        somme+= facto(x)/x
        x-=1
    return somme

# example
# print(fun3(5))
# input
# 34


    
