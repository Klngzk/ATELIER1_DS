# Ecrire une fonction Python pour trouver la fréquence d’un caractère dans une chaîne.
def fun7(char,string):
    f=0
    for i in string:
        if(i == char): f+=1
    return f


# example
# print(fun7("a","banana"))
# input
# 3