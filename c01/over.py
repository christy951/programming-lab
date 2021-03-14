list = []
n=int(input("enter the number"))
for i in range (0,n):
  
 if(i<100):
    list.append(i)
else:
  list.append("over")
  print(list)
