import time
import sys
import threading
import math

def is_prime(n):
    """Check if a number is prime (CPU-intensive task)"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def count_primes(start, end):
    """Count prime numbers in a range"""
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count

def run_single_threaded(start, end):
    """Run the task in a single thread"""
    start_time = time.time()
    count = count_primes(start, end)
    elapsed = time.time() - start_time
    print(f"Single-threaded: Found {count} primes in {elapsed:.2f} seconds")
    return elapsed

def run_multi_threaded(start, end, num_threads):
    """Run the task split across multiple threads"""
    chunk_size = (end - start) // num_threads
    threads = []
    results = [0] * num_threads
    
    def worker(thread_idx, start, end):
        results[thread_idx] = count_primes(start, end)
    
    start_time = time.time()
    
    for i in range(num_threads):
        thread_start = start + i * chunk_size
        thread_end = thread_start + chunk_size if i < num_threads - 1 else end
        thread = threading.Thread(target=worker, args=(i, thread_start, thread_end))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    total_primes = sum(results)
    elapsed = time.time() - start_time
    print(f"Multi-threaded ({num_threads} threads): Found {total_primes} primes in {elapsed:.2f} seconds")
    return elapsed

def main():
    print(f"Python version: {sys.version}")
    print(f"GIL enabled: {sys._is_gil_enabled()}")
    
    # Adjust these values based on your system
    start_num = 10**6
    end_num = 2 * 10**6  # Check primes between 1,000,000 and 2,000,000
    num_threads = 4
    
    print(f"\nCounting primes between {start_num} and {end_num}")
    
    # Warm-up run (ignore first run due to potential startup overhead)
    print("\nWarm-up run...")
    count_primes(10, 100)
    
    # Single-threaded run
    print("\nRunning single-threaded...")
    single_time = run_single_threaded(start_num, end_num)
    
    # Multi-threaded run
    print("\nRunning multi-threaded...")
    multi_time = run_multi_threaded(start_num, end_num, num_threads)
    
    # Calculate speedup
    if multi_time > 0:
        speedup = single_time / multi_time
        print(f"\nSpeedup: {speedup:.2f}x")
        efficiency = (single_time / (multi_time * num_threads)) * 100
        print(f"Parallel efficiency: {efficiency:.1f}%")
    else:
        print("\nCannot calculate speedup (multi-threaded time was zero)")

if __name__ == "__main__":
    main()
