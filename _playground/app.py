# def reverse_args(func):
#         def wrapper(*args, **kwargs):
#             args = sorted((i for i in args), reverse=True)
#             print(args)
#             res = func(*args, **kwargs)
#             return res
#         return wrapper


# @reverse_args
# def operation(a, b):
#     return a // b

# print(operation(90, 0))
items1 = [90,0,5]
items2 = [0,90]
items1.reverse();
items2.reverse();
print(items1)
print(items2)