lit=[]
n= int(input("Enter the number"))
for i in range(0,n):
    ele= int(input())
    if(ele<100):
        lit.append(ele)
    else:
        lit.append("over");
print(lit)
