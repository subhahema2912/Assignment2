size = int(input("Enter the size of the list: "))
lst = []

for i in range(size):
    values = input("Enter the Value: ")
    tuple_values = tuple(map(int, values.split(',')))
    lst.append(tuple_values)

sorted_list = []

while lst:
    min_tuple = lst[0]
    for t in lst:
        if t[-1] < min_tuple[-1]:
            min_tuple = t
    sorted_list.append(min_tuple)
    lst.remove(min_tuple)
print("Sorted list:",sorted_list)






