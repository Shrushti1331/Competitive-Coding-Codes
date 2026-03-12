m=int(input("Enter marks for maths:"))
p=int(input("Enter marks for physics:"))
e=int(input("Enter marks for english:"))
if m>p:
    if m>e:
        print("Marks of maths is maximum")
    else:
        print("Marks of english is maximum")
else:
    if p>e:
       print("Marks of physics is maximum")
    else:
        print("Marks of english is maximum")