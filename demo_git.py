# coding: utf-8
# Compute sum of list elements
def list_sum(liste):
    out = 0
    for elem in liste:
        out += elem
    return out

def facto(n):
    out = 1
    for elem in range(2, n+1):
        out = out*elem
    return out

data = range(20)

print ('Données : ')
print (data)
print ('La somme de la liste vaut :' + str(list_sum(data)))
print('Le factoriel de la longueur de la liste vaut:' + str(facto(len(data))))
