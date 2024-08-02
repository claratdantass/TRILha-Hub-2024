def count_candies(doces, docesExtras):
    array = []
    maior = max(doces)
    for i in range(len(doces)):
        array.append(doces[i] + docesExtras >= maior)

    return array

print(count_candies([2,3,5,1,3], 3))
