#import operator
def listintolist(a):
    b = []
    b.append(a[0])
    b.append(a[-1])
    print(b)

a = [5, 10, 15, 20, 25]
listintolist(a)
