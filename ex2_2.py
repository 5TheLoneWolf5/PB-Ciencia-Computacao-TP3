#!/bin/python3

import multiprocessing

def multiply_row(matrix1, matrix2, row):
    return [matrix1[row][col] * matrix2[row][col] for col in range(len(matrix1[0]))]

if __name__ == "__main__":
    matrix1 = [[32, 543, 14], [6, 413, 123], [354, 826, 451]]
    matrix2 = [[4, 2, 1], [5, 2, 9], [14, 3, 8]]

    num_workers = multiprocessing.cpu_count()
    
    rows = len(matrix1)
    
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.starmap(multiply_row, [(matrix1, matrix2, row) for row in range(rows)])

    for row in results:
        print(row)