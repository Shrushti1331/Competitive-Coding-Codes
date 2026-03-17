
# def add():
#     n1 = int(input("Enter the value of n1:"))
#     n2 = int(input("Enter the value of n2:"))
#     sum =n1+n2
#     mul=n1*n2
#     sub=n1-n2
#     div=n1/n2
#     return sum, sub, mul, div 

# result= add()
# print(result)
#total four types of argument we can pass
#position argument
#keyword argument
#default argument
#variable length argument/variable number argument

# def personalInfo(fname, lname):
#     print("First Name=", fname)
#     print("Last Name=", lname)
# personalInfo("Shrushti", "Swamy")

# def personalInfo(fname,lname):
#     print("First Name="< fname)
#     print()


# def personalInfo(fname,lname):
#     print("First Name:",fname)
#     print("Last Name:",lname)
# fname="shrushti" 
# lname="swamy"
# personalInfo(fname,lname)



# def cityName(city="Nagpur"):
#      print(city)
# cityName("Mumbai")
# cityName("Delhi")
# cityName()

# def studentName(*name):
#     print(name)
   

# studentName("Shrushti", "Mariyam", "janhavi", "rugvedi")

mylist =[5,2,9,7,5,6]
def searchElement(target):
   for i in range(len(mylist)):
       if target == mylist[i]:
           return i 
result =searchElement(7)
print("Element found at index number=", result) 

