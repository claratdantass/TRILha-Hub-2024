def romanos(s):
    hash = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    sum = 0
    for i in range(len(s)-1, -1, -1):
        print(hash[s[i]])
        curr = hash[s[i]]
        prox = hash[s[i-1]]
        if curr < prev:
            sum -= curr
        else:
            sum += curr
        prev = curr
        print(curr)
    
    return sum

print(romans("IV"))