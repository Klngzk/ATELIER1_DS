# Ecrire une fonction en Python pour compter les chiffres d'un nombre donné.
def fun6(x):
    if(x<0): x*=-1
    r = str(x)
    return len(r)

def fun6plus(x):
    if(x<0): x*=-1
    c = 1
    while(x>9):
        c+=1
        x = x/10
    return c
        
# example
# print(fun6(123456789))
# input
# 9