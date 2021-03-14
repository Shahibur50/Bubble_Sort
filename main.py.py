'''
Copyright (c) 2021, Shahibur Rahaman
All rights reserved.
'''

list_of_numbers = [11, 15, 12, 1, 2, 3, 45, 4, 5, 6, 7, 8, 9, 10]


def sort(sequence, reverse=False):
    if reverse:
        for _ in range(len(sequence) - 1):
            for j in range(len(sequence) - 1):
                element = sequence[j]
                next_element = sequence[j + 1]
                
                if element < next_element:
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]  

    else:
        for _ in range(len(sequence)):
            for j in range(len(sequence) - 1):
                element = sequence[j]
                next_element = sequence[j + 1]
                
                if element > next_element:
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence


print("# BUBBLE SORT")
print()
print(f"List sorted in ascending order: {sort(list_of_numbers)}")
print(f"List sorted in ascending order: {sort(list_of_numbers, reverse=True)}")
print()
