import timeit

code_to_test = """
a = 1
b = 0
a,b = b,a
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)