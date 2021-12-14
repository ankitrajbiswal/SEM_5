freq={}
sentence=input('Enter a sentence: ')
for i in sentence:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
