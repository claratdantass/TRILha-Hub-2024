def candy (doces, docesExtras):

    lista = []
    maior = max(doces)

    for i in range(len(doces)):
        if (doces[i] + docesExtras) >= maior:
            lista.append(True)
        else:
            lista.append(False)
    return lista

doces = [2,3,5,1,3]
docesExtras = 3

doces2 = [4,2,1,1,2]
docesExtras = 1

print(candy(doces, docesExtras))
print(candy(doces2, docesExtras))