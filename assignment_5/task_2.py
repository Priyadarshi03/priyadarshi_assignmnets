'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = number_list[:5]

reverse_first_five = first_five[::-1]

print(f"first_five Elements {first_five}")

print(f"first_five Elements {reverse_first_five}")