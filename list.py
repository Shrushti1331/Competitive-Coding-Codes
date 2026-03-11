# myList=["Shrushti","Ashish","Komal","Sandip",43,50.3,"sanchita","","janhvi"]
# print(myList)
# print(type(myList))
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[-1])
# print(myList[2:5])
# print(myList[:5])
# print(myList[1:])
# print(myList[1:8:2])
# print(myList[:])
# print(myList[::-1])
# myList.append("Harsh")
# myList.append("Laxman")
# print(myList)
# myList.insert(1,"sanket")
# print(myList)
# myList.remove("Sandip")
# print(myList)
# newList=myList.copy()
# print(myList)
# print(newList)

# 2D list
# myList=[
#     ["Shrushti","Swamy"],
#     ["85.46"],
#     [440013,"yyy"]
# ]
# print(myList)
# # print(myList[row][col])
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][0])
# print(myList[2][0])
# print(myList[2][1])

# Operations on List
# list1=["Shrushti","Swamy"]
# # print(list1*2)
# list2=[31,21,"Rbu"]
# # print(list1+list2)
# # del list2[2]
# # del list2
# list2.clear() #shows empty list (used to check is stack is empty or not)
# print(list2)

# Aliasing (Assigning one variable reference to another variable)
myList=[44,22,77,0,9,88]
newList=myList
print(id(myList))
print(id(newList))
