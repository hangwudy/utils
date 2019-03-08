import re
 
re_digits = re.compile(r'(\d+)')
 
def embedded_numbers(s):
    pieces = re_digits.split(s)                 # 切成数字和非数字
    print(pieces)
    pieces[1::2] = map(int, pieces[1::2])       # 将数字部分转成整数
    return pieces
 
def sort_string(lst):
    return sorted(lst, key=embedded_numbers)    # 将前面的函数作为key来排序
 
# # files = "file2.txt file8.txt file11.txt file5.txt"
# files = "1_1 1_2 2_2 2_1 1_4 1_11"
# files = files.split(' ')
 
# print(' '.join(sort_string(files)))

A = [1,2,3]
B = [2,3,4]
C = [3,4,5]

for i in range(3):
    C.append(A)
print(len(C))
