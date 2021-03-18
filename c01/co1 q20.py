a=[1,2,3,4,7,6,5,8]
ls=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ls.append(a[i])
print(ls)
