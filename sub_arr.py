
def max_sub_array(arr, length):
    '''function to return the largest sub-array of given size with largest sum'''
    if length < 1:
        return "Sub-array length must be at least 1"
    if length == 1:
        return [max(arr)]
    if len(arr) == 0 or len(arr) == 1:
        return "Array is empty or has only one item"
    if len(arr) < length:
        return "Required sub-array length greater than array {}".format(arr)

    max_sub_arr = []
    max_sum = 0

    for i in range(len(arr) - length+1):
        sub_arr = arr[i:i+length]
        my_sum = sum(sub_arr)

        if my_sum > max_sum:
            max_sum = my_sum
            max_sub_arr = sub_arr
    return 'The max sum is {} from sub-array {}'.format(max_sum, max_sub_arr)
