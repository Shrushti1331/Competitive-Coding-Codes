#i=1
#while i<=5:
    #print(i)
    #i=i+1

#username =''
#password=''
#while username != "admin" and password != "hello":
      #username = input("Enter username:")
      #password = input("Enter password:")

#sum of first n numbers

#n=int(input("Enter number:"))
#sum=0
#i=1
#while i<=n:
    #sum=sum+i

    #i=i+1
#print("the sum of first",n,"number is:",sum)

#name ="shrushti"
#newname =" "
#for i in name:
  #  if i not in newname:
 #    newname +=i
#print(name)
#print(newname)
#print(name[::-1])

#mycart=[10,20,200,300,800,60,700]
#for i in mycart:
 #if i>400:
  #print("This is my purchased cart item")
  #continue
 #print(i) 

#name ="shrushti"
#print(name[::-1])
#if name == name[::-1]:
    #print("palindrome string")
#else:
   # print("not palindrome")


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range (1,n+1):
        print(n+1-i,end=" ")
    print()
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range (1,n+2-i):
        print("*",end=" ")
    print()