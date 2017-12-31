def getBin(n):
    arr = "{0:b}".format(n)
    print (arr)
    return arr

arr = list(getBin(27))

ones = arr.count("1")

#list comprehension to get positions of all 1s
lst = [i for i,j in enumerate(arr) if j == '1'] 

lst = [i + 1 for i in lst]

result = [ones] + lst
print (result)
