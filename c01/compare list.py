list1 = []
list2 = []
list3 = []
n1 = int(input("Total elements in first list : "))
for i in range(n1):
    value = int(input("input no : "))
    list1.append(value)
n2 = int(input("Total elements in second list : "))
for i in range(n2):
        value = int(input("input no : "))
        list2.append(value)
if(n1 == n2):
      print("same length")
else:
       print("Not same length")
if(sum(list1) == sum(list2)):
        print("same sum")
else:
        print("sum are different")
list3 = [each for each in list1 if each in list2]
print("same members are :",list3)
