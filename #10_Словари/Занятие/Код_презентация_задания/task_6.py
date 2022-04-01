# # 1 Вариант
#
# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)
# ##############################################################


# # 2 Вариант
#
# a = 'pythonist'
# b = {}
# for i in a:
#     b[i] = a.count(i)
# print(b)
# ##############################################################



# # 3 Вариант
#
# a = 'pythonist'
# b = {}
# for i in a:
#     if i not in b:
#         b[i] = a.count(i)
# print(b)
# ##############################################################