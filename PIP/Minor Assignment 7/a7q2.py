def cumulative(lst):
        c_lst=[ ]
        length=len(lst)
        c_lst=[ sum(lst[0:x:1]) for x in range(0, length +1)]
        return c_lst[1:]
lst=[1,2,3,4,5]
print(cumulative(lst))
