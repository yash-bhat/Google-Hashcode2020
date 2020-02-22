i = {
0: {'total_books': 5, 'signup': 2, 'max_ship': 2, 'books': [0, 1, 2, 3, 4]},
1: {'total_books': 4, 'signup': 3, 'max_ship': 1, 'books': [0, 2, 3, 5, 7, 8, 10]},
2: {'total_books': 4, 'signup': 3, 'max_ship': 1, 'books': [0, 2, 3, 5, 9]},
3: {'total_books': 4, 'signup': 3, 'max_ship': 1, 'books': [0, 2, 3, 5, 1, 9]},
4: {'total_books': 4, 'signup': 3, 'max_ship': 1, 'books': [0, 2, 3, 5, 10, 8, 12]},
}
priority = [1, 3, 4, 2]

temp = dict()
#
# for ea in i.keys():
# temp.update({ea: i[ea]['books']})

total_set = set(i[priority[0]]['books'])

for ea in priority[1:]:
    temp_A = set(i[ea]['books'])
    temp_res = total_set - temp_A
    i[ea]['books'] = temp_res
    total_set.update(temp_res)


print(i)
