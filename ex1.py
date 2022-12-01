# Ecrire une fonction qui renvoie la puissance d’un nombre Xn
def fun1(x,n):
    return x**n

def fun2(x,n):
    r = 1
    for i in range(n):
        r*=x
    return r

# example
print(fun2(5,3))
# input
# 125