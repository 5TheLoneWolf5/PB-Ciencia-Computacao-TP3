"""

Comparação de desempenho:

Execução Sequencial: 1.942976951599121
Execução Paralela: 1.3552920818328857

Como é possível observar, a execução paralela executou mais rapidamente este algoritmo. Contudo, os resultados podiam ser variados.

"""

#!/bin/python3

import multiprocessing
import time

def prime_numbers_seq(y):
    x = 2
    primes = [True] * (y + 1)

    primes[0], primes[1] = False, False

    for i in range(2, int(y ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, y + 1, i):
                primes[j] = False

    res = [i for i in range(x, y + 1) if primes[i]]
    print(res if res else "No")

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

    amount = 10_000_000

    start = time.time()
    prime_numbers_seq(amount)
    end = time.time()

    print(f"Execução Sequencial: {end - start}")

    numbers = (1, amount)
    workers = multiprocessing.cpu_count()

    chunk_size = (numbers[1] - numbers[0]) // workers
    chunks = [(i, min(i + chunk_size, numbers[1])) for i in range(numbers[0], numbers[1], chunk_size)]

    start = time.time()

    with multiprocessing.Pool(workers) as pool:
        results = pool.map(prime_numbers_parallel, chunks)

    end = time.time()

    print(f"Execução Paralela: {end - start}")