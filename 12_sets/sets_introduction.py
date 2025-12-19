#      -> Sets - Sets are also built in data structure, to store 
#         multiple values using a single variable, using curly braces { }

#      -> In sets we don't have key value pairs

#         -> Lists - [10,20,30,40,50]
#         -> Tuples - (10,20,30,40,50)
#         -> Sets - {10,20,30,40,50}

#      -> Sets are UUU

#        -> Unordered
#        -> Unindexed
#        -> Unique elements

#      -> NOTE: Duplicates are automatically removed

#      -> Used especially for performing Mathematical set operations like
#         union, intersection, difference & symmetric difference

#      -> NOTE - TypeError: 'set' object is not subscriptable

#      -> not subscriptable - means you cannot use [index] and access
#         elements like in list and tuples

#      -> unhashable - means you are using list as a key in Dictionary or
#         adding a list as an element is set (immutables allowed)
# empty sets
empty_set = {} # always a dict
print(type(empty_set))

# using class
empty_set = set()
print(type(empty_set))

list_nums = [10,20,30,40,50,10,20]
tuple_nums = (10,20,30,40,50,10,20)

print(list_nums)
print(tuple_nums)

print(list_nums[0])
print(tuple_nums[0])


# numbers set
set_nums = {10,20,30,40,50,10,20}
print(set_nums) # Unordered, Unique
# print(set_nums[0]) # Unindex, TypeError: 'set' object is not subscriptable

# subscriptable or not
obj1 = [1,2,3]
print(hasattr(obj1,'__getitem__')) # True -> subscriptable
obj2 = {1,2,3}
print(hasattr(obj2,'__getitem__')) # False -> not subscriptable

# access -> loops
set_nums = {10,20,30,40,50,10,20}
print(dir(set_nums))

for i in set_nums:
    print(i)