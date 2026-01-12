n1 = int(input("Enter the number1"))
n2 = int(input("Enter the number2"))
a = n1+n2
print(a,"is the result")
def char_freq(s):
    dict1={}
    for i in s:
        if i not in dict1:
            dict[i]=1
        else:
            dict[i]+=1
    return(dict.items())
str1=input("enter the string")
dict1=char_freq(str1)
print(dict1)