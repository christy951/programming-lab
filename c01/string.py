string = str(input("enter the string : "))
a = string[0]
modified = string[1:].replace(a,"$")
print(a+modified)