def add_odd_numbers_of_array(array):
    return_value = 0
    for num in array:
        if num % 2 == 1: # if the num is odd
            return_value += num
    return return_value

if __name__ == '__main__':
    array1 = [2, 4, 6, 8]
    array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    array3 = [1, 2, 3]
    
    # print the sums of array1, array2, array3
    print(add_odd_numbers_of_array(array1)) # answer = 0
    print(add_odd_numbers_of_array(array2)) # answer = 25
    print(add_odd_numbers_of_array(array3)) # answer = 4