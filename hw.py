"""
Exercise-1: Count unique elements
Write a function "count_unique_elements(my_list: list) -> int" that takes a 
list of integers and returns the number of unique elements in the list.

Example:
count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]) -> 5
"""
from operator import index


def count_unique_elements(my_list: list) -> int:
    s = set(my_list)
    return len(s)
    pass

"""
Exercise-2: Remove duplicates
Write a function "remove_duplicates(my_list: list) -> list" that takes a list of integers and 
removes all duplicates, returning the new list with unique elements in their original order.

Example:
remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]) -> [1, 2, 3, 4, 5]
"""

def remove_duplicates(my_list: list) -> list:
    s = set(my_list)
    l = list(s)
    return l
    pass

"""
Exercise-3: Reverse a list
Write a function "reverse_list(my_list: list) -> list" that takes a list of integers and 
returns a new list with the elements in reverse order.

Example:
reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def reverse_list(my_list: list) -> list:
    return my_list[::-1]
    pass

"""
Exercise-4: Find the maximum value in a list
Write a function "max_value(my_list: list) -> int" that takes a 
list of integers and returns the maximum value in the list.

Example:
max_value([1, 2, 3, 4, 5]) -> 5
"""

def max_value(my_list: list) -> int:
    max_val = my_list[0]
    for i in my_list:
        if i > max_val: max_val = i

    return max_val
    pass

"""
Exercise-5: Find the minimum value in a list
Write a function "min_value(my_list: list) -> int" that takes a 
list of integers and returns the minimum value in the list.

Example:
min_value([1, 2, 3, 4, 5]) -> 1
"""

def min_value(my_list: list) -> int:
    min_val = my_list[0]
    for i in my_list:
        if i < min_val: min_val = i

    return min_val
    pass

"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a 
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    sum_of_val = 0
    for i in my_list:
        sum_of_val += i

    return sum_of_val
    pass

"""
Exercise-7: Find the average of a list
Write a function "average(my_list: list) -> float" that takes a 
list of integers and returns the average value of the list.

Example:
average([1, 2, 3, 4, 5]) -> 3.0
"""

def average(my_list: list) -> float:
    sum_val = 0
    for i in my_list:
        sum_val += i

    return sum_val / len(my_list)
    pass

"""
Exercise-8: Find the index of an element in a list
Write a function "find_index(my_list: list, element: int) -> int" that takes a 
list of integers and an element, and returns the index of the first occurrence of 
the element in the list. If the element is not in the list, return -1.

Example:
find_index([1, 2, 3, 4, 5], 3) -> 2
find_index([1, 2, 3, 4, 5], 6) -> -1
"""

def find_index(my_list: list, element: int) -> int:
    for i in range(len(my_list)):
        if my_list[i] == element: return i

    return -1
    pass

"""
Exercise-9: Check if a list is sorted
Write a function "is_sorted(my_list: list) -> bool" that takes a list
of integers and returns True if the list is sorted in non-descending 
order (i.e., each element is greater than or equal to the previous element), 
False otherwise.

Example:
is_sorted([1, 2, 3, 4, 5]) -> True
is_sorted([1, 3, 2, 4, 5]) -> False
"""

def is_sorted(my_list: list) -> bool:
    temp = my_list[:]
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] >= my_list[j]: my_list[j] = my_list[i]

    return temp == my_list
    pass

"""
Exercise-10: Count the frequency of an element in a list
Write a function "count_frequency(my_list: list, element: int) -> int" that 
takes a list of integers and an element, and returns the number of 
times the element appears in the list.

Example:
count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3) -> 2
"""

def count_frequency(my_list: list, element: int) -> int:
    count = 0
    for i in my_list:
        if i == element: count+=1

    return count
    pass

"""
Exercise-11: Find the mode of a list
Write a function "find_mode(my_list: list) -> int" that takes a list of 
integers and returns the mode (i.e., the value that appears most frequently) 
of the list. If there are multiple modes, return any of them.

Example:
find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]) -> 2
"""

def find_mode(my_list: list) -> int:
    if len(my_list) == 0: return None
    l = []
    for i in range(len(my_list)):
        l.append(my_list.count(my_list[i]))

    max_val = max(l)
    max_val_index = l.index(max_val)
    return my_list[max_val_index]
    pass

"""
Exercise-12: Remove all occurrences of an element in a list
Write a function "remove_all(my_list: list, element: int) -> list" 
that takes a list of integers and an element, and returns a new list 
with all occurrences of the element removed.

Example:
remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3) -> [1, 2, 4, 5, 1, 2]
"""

def remove_all(my_list: list, element: int) -> list:
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] != element:
            new_list.append(my_list[i])

    return new_list
    pass

"""
Exercise-13: Rotate a list to the left by k positions
Write a function "rotate_left(my_list: list, k: int) -> list" that takes a 
list of integers and an integer k, and returns a new list with the elements rotated k positions to the left.

Example:
rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
"""

def rotate_left(my_list: list, k: int) -> list:
    new_list = []
    for i in range(len(my_list)):
        if i + k >= len(my_list):
            new_list.append(my_list[i + k - len(my_list)])
        else:
            new_list.append(my_list[i + k])

    return new_list
    pass

"""
Exercise-14: Rotate a list to the right by k positions
Write a function "rotate_right(my_list: list, k: int) -> list" that 
takes a list of integers and an integer k, and returns a new list 
with the elements rotated k positions to the right.

Example:
rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
"""

def rotate_right(my_list: list, k: int) -> list:
    new_list = []
    for i in range(len(my_list)):
        if i - k < 0:
            new_list.append(my_list[len(my_list) + i - k])
        else:
            new_list.append(my_list[i - k])

    return new_list
    pass

"""
Exercise-15: Find the intersection of two lists
Write a function "find_intersection(list1: list, list2: list) -> list" that 
takes two lists of integers and returns a new list with the elements that are present in both lists.

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
"""

def find_intersection(list1: list, list2: list) -> list:
    l = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]: l.append(list1[i])

    s = set(l)
    new_list = list(s)
    return new_list
    pass

"""
Exercise-16: Find the union of two lists
Write a function "find_union(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in either list (i.e., the union of the lists).

Example:
find_union([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
"""

def find_union(list1: list, list2: list) -> list:
    l = []
    for i in range(len(list1) + len(list2)):
        if i >= len(list1):
            l.append(list2[i - len(list2)])
        else:
            l.append(list1[i])

    s = set(l)
    new_list = list(s)

    return new_list
    pass

"""
Exercise-17: Find the difference of two lists
Write a function "find_difference(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in the first list but not the second list.
Assume that list does not contain duplicates.

Example:
find_difference([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2]
"""

def find_difference(list1: list, list2: list) -> list:
    l = list1[:]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]: l.remove(list1[i])

    return l
    pass
