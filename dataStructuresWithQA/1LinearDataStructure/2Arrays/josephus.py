"""
Author: https://www.linkedin.com/in/mukesh-manral/
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after 
the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def josephus(int_list, skip):
    #list starts with 0 index
    skip = skip - 1                     
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        #hash index to every 3rd
        idx = (skip + idx) % len_list   
        yield int_list.pop(idx)
        len_list -= 1
