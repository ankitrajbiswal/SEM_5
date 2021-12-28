def StringToInt(s):
    if s:
        return ord(s[-1])-ord('0')+10*StringToInt(s[:-1])
    else:
        return 0
str1='124'
print(StringToInt(str1))

#Output
124

#Owned By
Ankit Raj Biswal
1941012238
ankitrudra2001@gmail.com
