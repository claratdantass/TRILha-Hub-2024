#Lista de doces
#Cada elemento representa o numero de doces da crianca i
#Ou seja, cada crianca é um indice

def maior_n_doces(doces, docesExtras):
    maior = max(doces)
    lista = []
    for i in doces:
        if (i + docesExtras) >= maior:
            lista.append(True)
        else:
            lista.append(False)
    
    return lista


