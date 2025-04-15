import threading
import time
import pandas as pd
import psutil
import gc
import os
import ctypes

def get_memory_usage():
    """Returns current process memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

def buggy_dataframe_operation():
        """Creates a DataFrame then crashes"""
        print("Thread started - creating DataFrame...")
        # Create a moderate-sized DataFrame (~50MB)
        data = {f'col_{i}': list(range(1000_000)) for i in range(50)}
        df = pd.DataFrame(data)
        print("DataFrame created, now doing buggy operation...")
        
        # Deliberate bug - access invalid memory after a delay
        time.sleep(2)  # Give time for main thread to measure memory
        print("About to crash...")
       # a = df['bad_key']

        
        # This will cause a segmentation fault
       # ctypes.string_at(0)  # Access null pointer
        

def main():
    print("Python Thread Crash Memory Leak Demonstration")
    print("============================================")
    
    # Initial memory usage
    start_mem = get_memory_usage()
    print(f"Initial memory usage: {start_mem:.2f} MB")
    
    # Start the thread
    thread = threading.Thread(target=buggy_dataframe_operation)
    thread.start()
    
    # Let it run for a moment
    time.sleep(1)
    
    # Memory usage after DataFrame creation
    mid_mem = get_memory_usage()
    print(f"\nMemory usage after DataFrame creation: {mid_mem:.2f} MB")
    print(f"Memory allocated by thread: {mid_mem - start_mem:.2f} MB")
    
    # Wait for crash (should happen after 2 seconds in thread)
    time.sleep(10)
    
    # Check thread status
    if thread.is_alive():
        print("\nThread is still alive (waiting for crash)...")
        time.sleep(1)
    
    # Memory usage after crash
    post_crash_mem = get_memory_usage()
    print(f"\nMemory usage after thread crash: {post_crash_mem:.2f} MB")
    print(f"Memory still held: {post_crash_mem - start_mem:.2f} MB")
    
    # Run garbage collector
    print("\nRunning garbage collector...")
    gc.collect()
    
    # Final memory usage
    end_mem = get_memory_usage()
    print(f"\nMemory usage after GC: {end_mem:.2f} MB")
    print(f"Memory still held: {end_mem - start_mem:.2f} MB")

if __name__ == "__main__":
    main()
