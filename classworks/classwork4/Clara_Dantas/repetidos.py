def repetido(lista):
    if len(set(lista)) == len(lista):
        return False
    
    aux= []
    for v in lista: 
        if v not in aux: 
            aux.append(v) 
        else: 
            return v
        
  
  
# segundo
# Second Version

def repetidos(lista):
    if len(set(lista)) == len(lista):
        return False
    
    hash = {}
    for v in lista:
        # if hash.get(v) is None:
        if v not in hash:
            hash[v] = v
        else:
            return v

print(repetidos([2,1,3,4,5,2,6]))