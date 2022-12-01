# Ecrire un programme python composé de plusieurs fonctions :
# • fonction qui envoi la valeur moyenne d’une liste


def fun9_1(l):
    s = 0
    for i in l:
        s+=i
    return s / len(l)
 
# print(fun9_1([1,23,2]))
# input
# 8.6666666


# • fonction qui renvoi le min ou max selon le choix de l ‘utilisateur

def fun9_2(list):
    i = input("Type 1 for min or 2 for max: ")
    if i == "1":
        min = list[0]
        for x in list:
            if(x<min): min = x
        return min
    elif i == "2":
        max = list[0]
        for x in list:
            if(x>max): max = x
        return max
    else:
        return "Wrong input"

# print(fun9_2([123,5,6,15,5]))
# input
# Type 1 for min or 2 for max: 1
# 5

# • fonction qui renvoie le médian d ‘une liste

def fun9_3(list):
    # impair
    if(len(list) %2 != 0):
        list.sort()
        return list[len(list)//2]
    # pair
    elif(len(list) %2 == 0):
        list.sort()
        index_before = len(list)//2 - 1
        index_after = len(list)//2
        return (list[index_after]+list[index_before]) /2

# print(fun9_3([7,5,2,9,1,6]))
# input
# 5.5


# • fonction qui renvoi le mode d’une liste
def fun9_4(list):
    res = dict()
    # we store the answer in a list because we can have 2 or more modes
    modes = []
    for x in list:
        if(res.get(x) == None): res[x]=1
        else: res[x]+=1
    max = 1
    for value in res.values():
        if value > max: max = value
    
    for key,value in res.items():
        if(value == max): modes.append(key)
    
    if max == 1: return "No Mode"
    return modes
        

# print(fun9_4([1,3,5,4,5,4]))
# input
# [5, 4]


# • fonction qui calcul la variance

def fun9_5(list):
    moyen = fun9_1(list)
    s = 0
    for x in list:
        s+= (x-moyen) ** 2
    return s/(len(list))

# print(fun9_5([2,4,6,8,10]))
# input
# 8