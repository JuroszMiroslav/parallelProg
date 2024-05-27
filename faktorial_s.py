import math
import time
import sys

# Zvýšení limitu pro převod velkých čísel na řetězce
sys.set_int_max_str_digits(10000000)
def calculate_factorials(num):
    results = []
    for num in numbers:
        results.append(math.factorial(num))
    return results

if __name__ == '__main__':
    numbers = [50000, 50001, 50002, 50003,50000, 50001, 50002, 50003]
    start_time = time.time()
    results = calculate_factorials(numbers)
    end_time = time.time()
    print(results)
    print(f'Sequential execution took {end_time - start_time} seconds')
