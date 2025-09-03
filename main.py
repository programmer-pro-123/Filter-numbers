# This code tests the function filter_number
from filterNumbers import filter_numbers

example_list = [1, 10, 25, 7, 12, 5, 3, 8, 22]           # List with random numbers, the first parameter of the function
start_number = 5             # The first number of the range, the second parameter of the function
end_number = 15              # The last number of the range, the third parameter of the function
print(filter_numbers(example_list, start_number, end_number))
