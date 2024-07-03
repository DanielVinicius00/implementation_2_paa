# Authors:
# # Benedito Jaime (GitHub: beneX90)
# # Daniel Vinicius (GitHub: DanielVinicius00)
# # Érick Santos Marçal (GitHub: erarich)

import time
import argparse
import csv
from gerar_lista import gerar_lista
from algoritmo.Boyer_Moore import Boyer_Moore
from algoritmo.countingsort import countingsort
from algoritmo.disCountingSort import disCountingSort
from algoritmo.HorspoolMatching import HorspoolMatching
from algoritmo.shift_table import shift_table


def test_sorting_algoritmo(algoritmo, data):
    start_time = time.time()
    sorted_arr, comparisons, swaps = algoritmo(data.copy())
    end_time = time.time()

    return {
        'sorted_array': sorted_arr,
        'comparisons': comparisons,
        'swaps': swaps,
        'time': (end_time - start_time) * 1000
    }


def append_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    parser = argparse.ArgumentParser(
        description='Execute sorting algorithm tests.')
    parser.add_argument('num_tests', type=int, help='Number of tests to run')
    parser.add_argument('output_file', type=str,
                        help='CSV file to append the results')
    parser.add_argument('algorithm', type=str, choices=['quick_sort', 'bubble_sort', 'selection_sort', 'insertion_sort', 'merge_sort', 'heap_sort'],
                        help='Sorting algorithm to use')

    args = parser.parse_args()
    num_tests = args.num_tests
    output_file = args.output_file
    algoritmo_name = args.algorithm

    algorithms = {
        'Boyer_Moore': Boyer_Moore,
        'countingsort': countingsort,
        'disCountingSort': disCountingSort,
        'HorspoolMatching': HorspoolMatching,
        'shift_table': shift_table
    }

    algorithm = algorithms[algoritmo_name]

    try:
        with open(output_file, 'r') as file:
            pass
    except FileNotFoundError:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['List Size', 'List Type', 'Algorithm',
                            'Comparisons', 'Swaps', 'Time (ms)'])

    list_sizes = [1000, 10000, 50000, 100000]
    list_types = ['ordenada', 'inversa', 'aleatoria']

    for _ in range(num_tests):
        for size in list_sizes:
            for list_type in list_types:
                lista = gerar_lista(size, list_type)
                results = test_sorting_algoritmo(algorithm, lista)

                row = [
                    size,
                    list_type,
                    algoritmo_name,
                    results['comparisons'],
                    results['swaps'],
                    results['time']
                ]

                append_to_csv(output_file, row)
                print(
                    f"Test completed for size {size} and type {list_type} using {algoritmo_name} with Comparisons: {results['comparisons']}, Swaps: {results['swaps']}, Time: {results['time']}ms")


if __name__ == "__main__":
    main()