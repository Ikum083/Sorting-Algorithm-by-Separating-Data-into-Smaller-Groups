import random as rd
# empty lists to store data
data_set = []
# final lists for the arranged data
final_data_set = []

# for loop to insert a random number of random data to the empty lists
for i in range(rd.randint(1, 20)):
    random_data = rd.randint(1, 20)
    data_set.insert(i, random_data)

# initial data set
print(data_set)

# data to be used as pivot
pivot_data = data_set[rd.randint(1, len(data_set) - 1)]

#function to seperate data based on chosen pivot
def grouping_data(data_set, pivot_data):
    print(pivot_data)
    larger_group = []
    equal_group = []
    smaller_group = []
    for data in data_set:
        if data > pivot_data:
            larger_group.append(data)
        elif data == pivot_data:
            equal_group.append(data)
        else:
            smaller_group.append(data)
    data_set = [smaller_group, equal_group, larger_group]
    return data_set

def same_element_list(data_set):
    return len(set(data_set)) == 1 if data_set else True

# re adjusting data set
data_set = grouping_data(data_set, pivot_data)

# inserting lists that contains the pivot, equal groups and groups with only one element into the final lists
for j in range(len(data_set)):
    if pivot_data in data_set[j]:
        for k in range(len(data_set[j])):
            final_data_set.append(data_set[j][k])
    elif len(data_set[j]) < 1:
        for k in range(len(data_set[j])):
            final_data_set.append(data_set[j][k])
    elif same_element_list(data_set[j]):
        for k in range(len(data_set[j])):
            final_data_set.append(data_set[j][k])
    else:
        pass
# printing the data set after re adjustment
print(data_set)
print(final_data_set)