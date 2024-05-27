import math
import time
import multiprocessing
import sys

# Zvýšení limitu pro převod velkých čísel na řetězce
sys.set_int_max_str_digits(10000000)

def calculate_factorial(num):
    return math.factorial(num)

if __name__ == '__main__':
    numbers = [50000, 50001, 50002, 50003,50000, 50001, 50002, 50003]
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(calculate_factorial, numbers)
    end_time = time.time()
    print(results)
    print(f'Parallel execution took {end_time - start_time} seconds')
