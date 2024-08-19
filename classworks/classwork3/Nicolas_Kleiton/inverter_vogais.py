def inverter_vogais(s: str) -> str:

    vogais = 'aeiouAEIOU'

    lista_vogais = []

    for letter in s:
        if letter in vogais:
            lista_vogais.append(letter)
    
    nova_string = []

    for letter in s:
        if letter in vogais:
            nova_string.append(lista_vogais.pop())
        else:
            nova_string.append(letter)
    
    return ''.join(nova_string)
