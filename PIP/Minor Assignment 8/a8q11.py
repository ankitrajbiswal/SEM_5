def gen(n,str=''):
    if n>0:
        gen(n-1,str+'0')
        gen(n-1,str+'1')
    else:
        print(str)
gen(3)

#Owned By
Ankit Raj Biswal
1941012238
ankitrudra2001@gmail.com
