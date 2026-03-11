# Membership operator : 1) in  2) not in
# name="Shrushti"
# print("Z" in name)
# print("Z" not in name)

#for loop
# for i in range(1,10): # no need to give increment it by default increments sequentially (i++)
#     print(i)

# for i in range(1,10,2): # 2 in the increment (i+2)
#     print(i)

# for i in range(5,0,-1): # Decrement (i--)
#     print(i)


#2-10 table
# for i in range(1,10):
#     for j in range(2,11):
#         print(i*j,end="\t")
#         print()
#         print("----------------------------------")


# if condition
# no=int(input("Enter any digit:"))
# if no>0:
#     print("Positive")
# if no<0:
#     print("negative")
# if no==0:
#     print("zero")

# Day of the week
# day=(str(input("Enter day:")))
# if day=='saturday' or 'sunday' or 'SATURDAY' or 'SUNDAY':
#     print("weekend")
# else:
#     print("week day")

# m=int(input("Enter marks for maths:"))
# p=int(input("Enter marks for physics:"))
# e=int(input("Enter marks for english:"))
# total=m+p+e
# print("Total:",total)
# percent=(total/300)*100
# print("percentage:",percent)
# if percent>=60:
#     print("eligible for placement")
# else:
#     print("Not eligible")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
e=int(input("Enter fiveth number:"))
if a>b and a>c and a>d and a>e:
    print(a," is max value")
if b>c and b>a and b>d and b>e:
    print(b," is max value")
if c>b and c>a and c>d and e:
    print(c," is max value")
if d>b and d>c and d>a and d>e:
    print(d," is max value")
else:
    print(e," is max value")