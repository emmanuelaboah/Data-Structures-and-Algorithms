'''
Problem Statement
Define a procedure, `deep_reverse`, that takes as input a list, and returns a new list that is the deep reverse of the input list.  
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down. 
Note: The procedure must not change the input list itself.

Example
 Input: [1, 2, [3, 4, 5], 4, 5]
 Output: [5, 4, [5, 4, 3], 2, 1]
'''

def deep_reverse(arr):
    
    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = [] 
    
        if type(item) is list:
            item = deep_reverse(item)
        
        # append the item to the final list
        reversed_items.append(item)

    return reversed_items

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)