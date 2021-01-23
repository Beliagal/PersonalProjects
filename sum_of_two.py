"""Given a sorted array and a number, return boolean true if the sum of two
elements in the array is equal to the number received and false otherwise.

Test cases:

[1, 3, 4, 9] and number = 8 should return false.
[1, 2, 4, 4] and number = 8 should return true.
[1, 3, 6, 9] and number = 12 should return true.
[1, 2, 6, 8, 9, 25, 33, 56] and number = 25 should return false."""

def sum_of_two (array, result):

    simple_array = []
    for number in array:
        if number < result:
            simple_array.append(number)

    len_init = 0
    max_len = len(simple_array)

    while len_init < max_len:
    
        repeats = 0 
        finish_len = 1 
        
        while repeats < max_len and len_init != finish_len:
            
            value_sum = simple_array[len_init] + simple_array[finish_len]
            finish_len += 1

            if finish_len == max_len:
                break

            if value_sum == result:
                print ('True')
                break
                
        len_init += 1
        
        if len_init == max_len and value_sum != result:
            print ('False')

sum_of_two ([1, 3, 4, 9], 8)
sum_of_two ([1, 2, 4, 4], 8)
sum_of_two ([1, 3, 6, 9], 12)
sum_of_two ([1, 2, 6, 8, 9, 25, 33, 56], 25)    