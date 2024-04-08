import re, datetime, math

name = input('Enter file:')
if len(name) < 1:
    name = 'regex_sum_1966297.txt'
handle = open(name)
ln = handle.readlines()
lst = []

for line in ln:
    numb = re.findall('[0-9]+', line)
    for i in numb:
        i = int(i)
        lst.append(i)

print(sum(lst))

def doc_file(name):
    if len(name) < 1:
        name = 'regex_sum_1966297.txt'
    handle = open(name)
    ln = handle.readlines()
    return ln

# def doc_du_lieu_trong_file(ln):
#     result = []
#     for line in ln:
#         numb = re.findall('[0-9]+', line)
#         for i in numb:
#             i = int(i)
#             result.append(i)
#     return result

# def tinh_tong_phan_tu_trong_mang(array_input):
#     result = 0
#     for i in array_input:
#         result = result + i
    return result

data = doc_file("test.txt")
list_so = doc_du_lieu_trong_file(data)
tong = tinh_tong_phan_tu_trong_mang(list_so)
