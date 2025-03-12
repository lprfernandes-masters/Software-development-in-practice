"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

from time import process_time
from iterative.iterative_floyd import iterative_floyd
from recursion.recursive_floyd import recursive_floyd_warshall
import sys
sys.path.append('../')


def performance_test(function_handle):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters
    """
    start = process_time()
    function_handle()
    end = process_time()
    print(f"Execution Time: {end - start} seconds")


print("Recursion Test Time")
performance_test(recursive_floyd_warshall)

print("Iterative Test Time")
performance_test(iterative_floyd)
