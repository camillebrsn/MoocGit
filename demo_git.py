# coding: utf-8
#
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

data = range(20, 26)
data2 = [20, 1, 29, 25, 5, 23]

def diff_list(liste1, liste2):
    out = list()
    for elem in liste1:
        if elem not in liste2:
            out.append(elem)
    for elem in liste2:
        if elem not in liste1:
            out.append(elem)
    return out

print ('Données : ')
print (data)
print (data2)
print ('La somme de la liste vaut :' + str(list_sum(data)))
print('Le factoriel de la longueur de la liste vaut: ' + str(facto(len(data))))
print('Différence des deux: ')
print (diff_list(data, data2))
