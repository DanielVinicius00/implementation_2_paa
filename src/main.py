import time
import argparse
import csv
from gerar_lista import gerar_lista
from algoritmo.boyer_moore import boyer_moore
from algoritmo.countingsort import countingsort
from algoritmo.disCountingSort import disCountingSort
from algoritmo.HorspoolMatching import HorspoolMatching
from algoritmo.shift_table import create_shift_table

def test_sorting_algorithm(algorithm, data):
    start_time = time.time()
    sorted_arr, comparisons, swaps = algorithm(data.copy())
    end_time = time.time()

    return {
        'sorted_array': sorted_arr,
        'comparisons': comparisons,
        'swaps': swaps,
        'time': (end_time - start_time) * 1000
    }

def test_search_algorithm(algorithm, pattern, text):
    start_time = time.time()
    result = algorithm(pattern, text)
    end_time = time.time()

    return {
        'result': result,
        'time': (end_time - start_time) * 1000
    }

def append_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    parser = argparse.ArgumentParser(
        description='Execute algorithm tests.')
    parser.add_argument('num_tests', type=int, help='Number of tests to run')
    parser.add_argument('output_file', type=str, help='CSV file to append the results')
    parser.add_argument('algorithm', type=str, choices=['boyer_moore', 'countingsort', 'disCountingSort', 'HorspoolMatching'], help='Algorithm to use')

    args = parser.parse_args()
    num_tests = args.num_tests
    output_file = args.output_file
    algorithm_name = args.algorithm

    algorithms = {
        'boyer_moore': boyer_moore,
        'countingsort': countingsort,
        'disCountingSort': disCountingSort,
        'HorspoolMatching': HorspoolMatching
    }

    algorithm = algorithms[algorithm_name]

    try:
        with open(output_file, 'r') as file:
            pass
    except FileNotFoundError:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Test Type', 'Pattern', 'Text', 'Algorithm', 'Result', 'Time (ms)'])

    if algorithm_name in ['boyer_moore', 'HorspoolMatching']:
        pattern = "example"
        text = "this is an example"
        for _ in range(num_tests):
            results = test_search_algorithm(algorithm, pattern, text)
            row = [
                'search',
                pattern,
                text,
                algorithm_name,
                results['result'],
                results['time']
            ]
            append_to_csv(output_file, row)
            print(f"Test completed using {algorithm_name} with Result: {results['result']}, Time: {results['time']}ms")
    else:
        list_sizes = [1000, 10000, 50000, 100000]
        list_types = ['ordenada', 'inversa', 'aleatoria']

        for _ in range(num_tests):
            for size in list_sizes:
                for list_type in list_types:
                    lista = gerar_lista(size, list_type)
                    results = test_sorting_algorithm(algorithm, lista)

                    row = [
                        'sorting',
                        size,
                        list_type,
                        algorithm_name,
                        results['comparisons'],
                        results['swaps'],
                        results['time']
                    ]

                    append_to_csv(output_file, row)
                    print(f"Test completed for size {size} and type {list_type} using {algorithm_name} with Comparisons: {results['comparisons']}, Swaps: {results['swaps']}, Time: {results['time']}ms")

if __name__ == "__main__":
    main()
