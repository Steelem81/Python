def zeroing_out(array):
    #given an array
    #replace all negative values with zero
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0
    return array

test_array = [10, 5, -7, -9, 2, 22, 10]
t_array_out = zeroing_out(test_array)
print(t_array_out)

#list comprehension
print([0 if x < 0 else x for x in test_array])

