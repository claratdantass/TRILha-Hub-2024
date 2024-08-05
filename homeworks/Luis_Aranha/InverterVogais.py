vogais = "aeiouAEIOU"

corda = "hello"

def inverter(corda):
    left = 0
    right = len(corda) - 1
    corda = list(corda)
    while left < right:
        if corda[left] not in vogais:
            left += 1
        elif corda[right] not in vogais:
            right -= 1
        
        else:
            corda[left], corda[right] = corda[right], corda[left]
            left += 1
            right -= 1

    corda = "".join(corda)
    return corda

print(inverter(corda))