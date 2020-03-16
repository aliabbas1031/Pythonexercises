def sumofdigits(a):
    total = 0
    while a>0:
        total = total+a%10
        a=a//10
    return total

def digitsum(arr):
    data = {}
    maxvalue = -1
    for i in arr:
        eachdata = sumofdigits(i)
        if eachdata in data:
            value = data[eachdata]
            maxvalue = max(maxvalue,value + i)
            data[eachdata] = max(value,i)
        else:
            data[eachdata] = i
    return maxvalue


l = [23,54,32,46,34,14,500,500]
print(digitsum(l))


