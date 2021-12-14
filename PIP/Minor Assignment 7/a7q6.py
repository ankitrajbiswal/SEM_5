def funclist(n):
  lst=[]
  lst2=[0,0,0,0,0]
  for i in range(1,n+1):
    for j in range(1,6):
      lst2[j-1]=i*j
    lst.append(lst2[:])
  return lst
def main():
  n=int(input("Enter a Number : "))
  print(funclist(n))
if__name__=='__main__';
  main()
