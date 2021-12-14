#1
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    print(l1)
    print(l2)
print(func())

#Output 1
[0, 1, 2, 3, 4]
[3, 4, 5, 6, 7]
None


#2
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
        l1, l2 = l2, l1
    print(l1)
    print(l2)
print(func())

#Output 2
[3, 1, 5, 3, 7]
[0, 4, 2, 6, 4]
None
