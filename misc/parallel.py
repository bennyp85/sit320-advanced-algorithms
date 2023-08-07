import multiprocessing
import time

def compute_sum(n):
    """Compute the sum of the first n integers."""
    return sum(range(n))

def main():
    # List of large numbers to compute the sum of first n integers
    numbers = [10**7, 10**7 + 100, 10**7 + 200, 10**7 + 300, 10**7 + 400]

    # Serial computation
    start_time = time.time()
    serial_results = [compute_sum(n) for n in numbers]
    serial_duration = time.time() - start_time

    # Parallel computation using all available cores
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        parallel_results = pool.map(compute_sum, numbers)
    parallel_duration = time.time() - start_time

    # Verify results are the same (just for sanity check)
    assert serial_results == parallel_results, "Mismatch in results"

    # Print out timings
    print(f"Serial execution time: {serial_duration:.2f} seconds")
    print(f"Parallel execution time: {parallel_duration:.2f} seconds")

if __name__ == "__main__":
    main()
