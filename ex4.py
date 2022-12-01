# Ecrire une fonction en Python pour convertir le nombre décimal en nombre binaire.
def fun4(x):
    r=""
    while(x!=0):
        rest= str(x%2)
        r+=rest
        x= x//2
    return r[::-1]

# example
# print(fun4(27))
# input
# 10001