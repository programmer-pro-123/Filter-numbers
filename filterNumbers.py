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
This file contains the function filter_number. This function filtrates integer
numbers in a list, returning a new one with the numbers in
the initial one which are into the range established by the user.
"""

def filter_numbers(numbers, start, end):
    """
    The parameter numbers is a list with integer numbers; the parameter
    start is the first number of the range; and the parameter end is the
    last number of the range
    """
    
    list_range = list()       # The new list that the function returns
    for number in numbers:    # We loop through the list to filter the numbers
        if start <= number <= end:
            # For each list's number, we check if it is into the range
            list_range.append(number) # if belongs, we add it to the list
                                      # that the function returns
    return list_range          # Finally the function return the list
                               # with the numbers in the range
