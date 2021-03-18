N=int(input("Enter Total number of elements in list:"))
list=[]
for i in range(N):
            value=int(input("enter a number : "))
            list.append(value)
            for i in list:
                print("square of",i,"is :",pow(i,2))
