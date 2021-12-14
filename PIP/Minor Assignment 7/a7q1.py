def store_unique_list():
  l1=[1,2,3,4,5,6,7,8,9,10,11,12]
  l2=[]
  for item in l1:
    if item not in l2:
      l2.append(item)
  print(l1)
  print(l2)
store_unique_list()
    
