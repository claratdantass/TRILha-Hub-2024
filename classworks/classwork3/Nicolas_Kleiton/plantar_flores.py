def plantar_flores(canteiro,n):

    contador = 0

    # Verificamos cada elemento da lista.
    for i in range(len(canteiro)):
    
    #Nesse if iremos verificar o valor atual de cada elemento e caso esteja vazio (0) iremos verificar se i está no inicio ou no fim da lista, e caso não esteja, verificamos se seus ambos os lados também estão vazios para que não ocorra plantações adjacentes.

        if (canteiro [i] == 0):
            lado_esquerdo = (i == 0) or (canteiro[i - 1] == 0)
            lado_direito = (i == len(canteiro) - 1 ) or (canteiro[i + 1] == 0)


    #Caso seus ambos os lados também estejam vazios, iremos plantar.
            if (lado_esquerdo and lado_direito):
                canteiro[i] = 1
                contador+=1
                
                if (contador == n):
                     return True #Caso todas sejam plantadas com sucesso.
            
    # Caso ainda reste flores para plantar, retorna False.
    return False

print(plantar_flores([1,0,0,0,1], 2))
