# Ecrire une fonction qui cherche un élément dans une matrice puis renvoi sa position «
# i,j».

def fun8(value,m):
    r =[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if value == m[i][j]:
                temp = []
                # we add one to i and j because normal matrix index starts with 1
                temp.extend([i+1,j+1])
                r.append(temp)
    # we used a list inside a list to show the index of the number if it has duplicates
    return r


# without duplicate
matrix = [[1,23,3],[5,6,8],[9,44,56]]
print(fun8(3,matrix))
# input
# [[1, 3]]

# with duplicate
matrix = [[1,23,3],[5,6,8],[9,3,56]]
print(fun8(3,matrix))
# input
# [[[1, 3], [3, 2]]