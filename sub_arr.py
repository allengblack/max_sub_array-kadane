
def max_sub_arr(arr):
    '''function to return the largest sub-array of given size with largest sum'''
    max_sum = current_sum = 0
    current_sub_arr_index = max_sub_arr_start_index = max_sub_arr_end_index = 0
    for index, item in enumerate(arr):
        if current_sum + item > 0:
            current_sum += item
        else:
            current_sum = 0
            current_sub_arr_index = index + 1

        if current_sum > max_sum:
            max_sub_arr_start_index = current_sub_arr_index
            max_sub_arr_end_index = index + 1
            max_sum = current_sum
    return "The largest sub-array is {} and its sum is {}".format(
        arr[max_sub_arr_start_index:max_sub_arr_end_index], max_sum)

print(max_sub_arr([-2, 3, 2, -1]))
print(max_sub_arr([-1, 2, -3, 4, -5]))
print(max_sub_arr([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]))
