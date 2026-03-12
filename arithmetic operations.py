#a=50
#b=30
#c=20
#d=10
#print((a+b)*c/d)
#print((a-b)*(c/d))
#print(a+(b*c)/d)

#x=['A','B','C']
#y=['A','B','C']
#z=[1,2,3,4]
#print(x==y)
#print(x==z)
#print(x!=z)

name="shrushti"
data =['a','e','i','o','u']
vowels=0
con=0
for i in name:
    if i in data:
        vowels +=1
    else:
        con +=1
    print(i)
    print("vowels", vowels)
    print("consonent",con)