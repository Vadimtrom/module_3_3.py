def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
# 1.2
print_params()
# 1.3
print_params(a = 2, b = 'Tree')
# 1.4
print_params(b = 25)
print_params(c = [1,2,3])
 # 2.1
values_list = ['See', 3, 'Eye']
print_params(*values_list)
 # 2.2
values_dict = {'a': None, 'b': 5, 'c':'Six'}
print_params(**values_dict)
#3.1
values_list_2 = ['Gyroscop', 100]
print_params(*values_list_2, 42)