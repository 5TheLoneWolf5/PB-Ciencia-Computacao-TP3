#!/bin/python3

import multiprocessing

def arePrime(lst, end):
    for i in range(2, int(end ** 0.5) + 1):
        if lst[i]:
            for j in range(i * i, end + 1, i):
                lst[j] = False

def prime_numbers_parallel(range_values):
    start, end = range_values
    primes = [True] * (end + 1)

    primes[0], primes[1] = False, False

    arePrime(primes, end)

    return [i for i in range(max(2, start), end + 1) if primes[i]]

if __name__ == "__main__":
    numbers = (1, 10_000_000)
    workers = 6

    chunk_size = (numbers[1] - numbers[0]) // workers
    chunks = [(i, min(i + chunk_size, numbers[1])) for i in range(numbers[0], numbers[1], chunk_size)]

    with multiprocessing.Pool(workers) as pool:
        results = pool.map(prime_numbers_parallel, chunks)

    all_primes = [num for sublist in results for num in sublist]

    print(f"Total de números primos: {len(all_primes)}")
    print(all_primes[:100])