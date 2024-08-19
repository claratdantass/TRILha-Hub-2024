# mover todos os numeros 0 de um array para a ultima posiçao, sem criar um novo array;
# manter a posiçao relativa dos numeros diferentes de 0;

lista = [1,7,9,3,0,0,6,8]

def mover(lista):

    contador = 0
    
    for posicao in range(len(lista)):

        if lista[posicao] != 0:
            lista[contador] = lista[posicao]
            contador += 1
    
    for indice in range(contador, len(lista)):
        lista[indice] = 0

    print(lista)

mover(lista)