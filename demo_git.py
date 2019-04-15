# coding: utf-8
#
# Compute sum of list elements
from functions import list_sum, facto, diff_list, alphabetical_order


data = range(20, 26)
data2 = [20, 1, 29, 25, 5, 23]
spell = 'ordrealphabetique'

print ('Données : ')
print (data)
print (data2)
print ('La somme de la liste vaut :' + str(list_sum(data)))
print('Le factoriel de la longueur de la liste vaut: ' + str(facto(len(data))))
print('Différence des deux: ')
print (diff_list(data, data2))
print ('Chaine de caractere ' + spell)
print ('Ordre alphanétique ' + alphabetical_order(spell))


