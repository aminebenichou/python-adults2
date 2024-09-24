def sum(a=[]):
    i = 0
    b = 0
    while i< len(a):
        b += a[i]
        i += 1
    return b


result = sum([10,10])
print(result)
