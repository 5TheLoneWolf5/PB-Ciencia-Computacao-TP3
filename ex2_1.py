#!/bin/python3

import multiprocessing

def sum_numbers(n):
    return sum(n)

if __name__ == "__main__":
    numbers = list(range(1, 10000001))
    num_workers = multiprocessing.cpu_count()
    # print(num_workers)

    chunk_size = len(numbers) // num_workers
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(sum_numbers, chunks)

    total = 0
    for i in results:
    	print(i)
    	total += i

    print(f"Total: {total}")