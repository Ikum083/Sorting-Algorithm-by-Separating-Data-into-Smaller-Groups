import random as rd
# empty lists to store data
data_set = []

# for loop to insert a random number of random data to the empty lists
for i in range(rd.randint(1, 20)):
    random_data = rd.randint(1, 20)
    data_set.insert(i, random_data)

# initial data set
print(data_set)

#function to seperate data based on chosen pivot
def grouping_data(data_set):
    pivot_data = data_set[rd.randint(1, len(data_set) - 1)]
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
            
# re adjusting data set
data_set = grouping_data(data_set)

# printing the data set after re adjustment
print(data_set)