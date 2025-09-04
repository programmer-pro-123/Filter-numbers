# MIT License
#
# Copyright (c) 2025 programmer-pro-123
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""
This file contains the function filter_numbers. This function filtrates integer
numbers into a list, returning a new list with the numbers in
the initial one which belongs to the range established by the user.

The list must contain only integer numbers, in other case the function
will raise an exception.
"""

def filter_numbers(numbers, start, end):
    """
    The parameter numbers is a list with integer numbers; the parameter
    start is the first number of the range; and the parameter end is the
    last number of the range
    """

    list_range = list()       # The new list that the function returns

    for number in numbers:    # We loop through the list to filter the numbers
        if type(numbers) is not int:
            # For each element in the list, we check if it is an integer number.
            raise TypeError(Not valid element/s in the list)
            # If there are elements in the list which are not integer numbers, the function
            # raises an exception

        if start <= number <= end:
            # For each list's number, we check if it is into the range
            list_range.append(number) # If the number belongs to the range, we add it to the list that 
                                      # the function returns (called list_range)

    return list_range        # Finally the function returns the list with the filtrated numbers
