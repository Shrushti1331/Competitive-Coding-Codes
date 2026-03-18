# a = input("Enter string: ")
# count = 0
# special_chars = " !@#$%^&*"

# for char in a:
#     if char in special_chars:
#         count += 1

# print(count)


# import re
# var='gasgg54@#vscsd!s*'
# count=0
# for i in var:
#  z=ord(i)
#  if z>=97 and z<=122:
#     continue
#  elif z>=48 and z<=57:
#     continue
#  else:
#       count+=1
# print(count)


# # Sample arrays
# a = [1, 2, 3]
# b = [2, 3, 4]
# c = [3, 4, 5]

# # Convert lists to sets
# set_a = set(a)
# set_b = set(b)
# set_c = set(c)
# common = set_a.intersection(set_b, set_c)

# print("Common elements:", common)


# a=[0,1,0,3,12]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)
# print(a)

a = [10, 11, 7, 12, 14]
total_distance = 0

# We loop from 0 to the second-to-last index (len(a) - 1)
# so that a[i+1] doesn't look for a number that isn't there.
for i in range(len(a) - 1):
    # abs() ensures the distance is positive, even if the number drops
    distance = abs(a[i+1] - a[i])
    total_distance += distance

print("Total distance:", total_distance)