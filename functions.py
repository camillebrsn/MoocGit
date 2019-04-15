def list_sum(liste):
    if isinstance(liste[0], int):
        out = 0
    elif isinstance(liste[0], str):
        out = ''
    for elem in liste:
        out += elem
    return out

def facto(n):
    out = 1
    for elem in range(2, n+1):
        out = out*elem
    return out

def diff_list(liste1, liste2):
    out = list()
    for elem in liste1:
        if elem not in liste2:
            out.append(elem)
    for elem in liste2:
        if elem not in liste1:
            out.append(elem)
    return out

def alphabetical_order(chaine):
    temp = list()
    len_str = len(chaine)
    str_list = [w for w in chaine]
    for i in range(len_str):
        temp.append(min(str_list))
        str_list.remove(min(str_list))
    return list_sum(temp)
