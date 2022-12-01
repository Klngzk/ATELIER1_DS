# Ecrire une fonction python qui calcul la factorielle d’un nombre donné
def facto(x):
    n = x
    if x == 0 or x ==1:
        return 1
    while(x!=1):
        n*= x-1
        x-=1
    return n

# example
# print(facto(5))
# input
# 120
        