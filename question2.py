# 2). Explain the concept of list comprehension in Python with at least three examples.
# it is an easy way to read,compact and elegant way of creating a list from any existing iterable object.
# it is generally a single line of code enclosed in square brackets.you can use it to filter,format,modify and perform various tasks like existing iterables such as strings,tuples,sets,dataframes and array list

# components of list comprehension
# i) For loop.
# ii)Conditon and expression.
# iii)output.

# example 1
# lst = [1,2,3,4,5,6,7,8,9,10]
# # simple list comprehension
# a = [x for x in lst]
# print(a)
# The above code is equivalent to this:
# for x in lst:
# a.append(x)


# example 2
# lst = [1,2,3,4,5,6,7,8,9,10]
# # with if condition
# c = [x for x in lst if x > 4]
# print(c)
# The above code is equivalent to this:
# for x in lst:
#     if x > 4:
#         a.append(x)

# example 3
# with multiple if 
# d = [x for x in lst if x > 4 if x%2 == 0]

# The above code is equivalent to this
# for x in lst:
#     if x > 4:
#         if x % 2 == 0:
#             a.append(x)