#with open('a_example.txt') as f:
#with open('b_read_on.txt') as f:
with open('c_incunabula.txt') as f:
    B, L, D = [int(x) for x in next(f).split()]
    scores = [int(x) for x in next(f).split()]
    collection = {}
    for i in range(L):
        a,b,c = [int(x) for x in next(f).split()]
        collection[i] = {'total_books': a, 'signup': b, 'max_ship': c, 'books': [int(x) for x in next(f).split()]}

print(B,L,D)
print(scores)
print(collection)

visited_books = []
compute_score = 0
day_weight = []
lib_priority = {}
final_L = 0


#sign-up of books
for i in range(L):
    total_books,signup,max_ship,_ = collection[i].values()

    #check if library signed up even
    if max_ship < D:
        final_L += 1

        days_books,rem = total_books//max_ship , total_books%max_ship
        if rem != 0 :
            days_books += 1
        days_books += signup

        day_weight.append(days_books)

        lib_priority[i] = days_books

        #temp = collection[i]['signup']
print(day_weight)
print (L)
print (lib_priority)

#sort based on lib priority
{k: v for k, v in sorted(lib_priority.items(), key=lambda item: item[1])}
print(lib_priority)



priority = list(lib_priority.keys())
print(priority)
# priority = [1, 3, 4, 2]

temp = dict()
#
# for ea in i.keys():
# temp.update({ea: i[ea]['books']})

total_set = set(collection[priority[0]]['books'])

for ea in priority[1:]:
    temp_A = set(collection[ea]['books'])
    temp_res = temp_A - total_set
    res = total_set.intersection(temp_A)
    collection[ea]['books'] = list(temp_res) + list(res)
    total_set.update(temp_res)


print(collection)
print(collection[1].keys())

total_books = 0
total_days = 10
res = []
which_books = {}
for j,ea in enumerate(priority):
    total_days -= collection[ea]['signup']
    # if total_days > 0:
    #     total_books += total_days*collection[ea]['max_ship'] > len(collection[ea]['books'])  and total_days*collection[ea]['max_ship'] or len(collection[ea]['books'])
    #     # print('hgjsdhjf',total_books)
    #     res.append(total_books)
    #     which_books[j] = (collection[j]['books'][:total_books])
    if total_days > 0:
        if total_days * collection[ea]['max_ship'] < len(collection[ea]['books']):
            total_books += total_days * collection[ea]['max_ship']
            which_books.update({ea: collection[ea]['books'][0:total_days * collection[ea]['max_ship']]})
            res.append(total_books)
        else:
            total_books += len(collection[ea]['books'])
            which_books.update({ea: collection[ea]['books'][0:len(collection[ea]['books'])]})
            res.append(total_books)


# print(collection[j]['books'][:total_books])
print('res:',res)
print('whcih books',which_books)


keysyash = list(lib_priority.keys())
f = open('result_c.txt',"a+")
f.write("%d\n"%(L))
for i in range(L):
    f.write("%d "%keysyash[i])
    f.write("%d\n"%len(which_books[i]))
    for val in which_books[i]:
        f.write("%d "%val)
    f.write("\n")
f.write("\n")