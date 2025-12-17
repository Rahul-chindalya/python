# -> List Methods 

#     1 -> append : adds an element to the end of the list
#          element can be a number, string or list also

#     2 -> extend : takes an iterable (list, tuples, strings), and add
#     each element to the list Individually

#     NOTE: Both append & extend will take only single argument

#     3 -> insert : insert allows you to insert an element at
#         a specific position(index)

#             -> if you give index out of range, element is added
#             at the end of the list

#             -> insert will move the positions, but not replace

#     4 -> pop - will remove and returns an element from the list
#         removes last element

#     5 -> remove - will remove based on pattern, not by index
#         By default first occurrence is removed, 
#         If pattern is not found, we get error  

#     6 -> clear - clears all the elements in list  

#     7 -> index - returns index position
#         -> element is must
#         -> start is optional, default start is 0
#         -> end is optional, default end is end of list
    
#     8 -> count - returns number of times an element is appeared

#     9 -> copy - creates a shallow copy, duplicating without 
#     affecting the original

#         -> if you want soft copy use Assignment
    
#     10 -> reverse - reverses the elements in the list, 
#         updates the original list

#         -> Reverse but don't update original list (Slicing)

#     11 -> sort - sorts the list either in ascending or descending
#         -> Default is ascending
#         -> If you need descending, update reverse as True
#         -> Sort can be possible only with same type of data, 
#             mix data we cannot sort


#     -> Lists Characteristics

#         -> Ordered - Items stored and order is preserved

#         -> Mutable - You can change the data (append, remove etc)

#         -> Allows Duplicates - Same element can be stored multiple times

#         -> Can Hold Any Type Of Data 

# List Methods 
list_nums = [10,20,30,40,50]
print(list_nums) # Before append
list_nums.append(60) # one element
print(list_nums) # After append

# list_nums.append(70,80) # multiple element
# TypeError: list.append() takes exactly one argument (2 given)
list_nums.append([70,80])
print(list_nums) # After append --> added as nested list

list_nums.append("Hello")
print(list_nums)

# In Lists we can have duplicates
list_nums.append(60)
list_nums.append("Hello")
print(list_nums)

list_nums = [10,20,30,40,50]
# list_nums.extend(60) --> TypeError: 'int' object is not iterable
list_nums.extend([60]) 
print(list_nums)

list_nums.extend([70,80])
print(list_nums) # After extend --> added as Individually
list_nums.extend("Hello")
print(list_nums)

# list_nums.extend([70,80],[90,100]) --> TypeError: list.extend() takes exactly one argument (2 given)
print(list_nums)

list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(10,20)
print(list_nums)

list_nums.insert(0,5)
print(list_nums)

list_nums[0] = 15
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop()
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop(2)
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# list_nums.pop(10) --> IndexError: pop index out of range
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.remove(20)
print(list_nums)
# list_nums.remove(60) --> ValueError: list.remove(x): x not in list
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums)
print(list_nums.index(40))

print(list_nums.index(20,4,8))

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums.count(50))

list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums = list_nums.copy() # shallow copy
print(backup_list_nums)

backup_list_nums.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums)

# Soft copy 
list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums_soft = list_nums # Soft copy
backup_list_nums_soft.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums_soft)

list_nums = [10,20, 30,40,50]
print(list_nums)

print(list_nums.reverse())
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# print(text[::-1])
print(list_nums[::-1])
print(list_nums)

list_nums = [10,30,20,50,40]
print(list_nums)
print(list_nums.sort(reverse=False)) # ascending
print(list_nums)

print(list_nums.sort(reverse=True)) # descending
print(list_nums)

list_text = ["hi","abc","zoro"]
print(list_text)
print(list_text.sort())
print(list_text)

mixed_list = ["hi",2,3.5,"abc","zoro"]
print(mixed_list)
print(mixed_list.sort())
print(mixed_list)