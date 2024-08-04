# Can place flowers

def place_flowers(canteiro, n):
    count = 0
    length = len(canteiro)
    for i in range(length):
        if canteiro[i] == 0 and (i == 0 or canteiro[i-1] == 0) and (i == length-1 or canteiro[i+1] == 0):
            canteiro[i] = 1
            count += 1
            if count == n:
                return True
    return False

print(place_flowers([1,0,0,0,1], 1))
