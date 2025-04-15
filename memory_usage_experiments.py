import threading
import time
import pandas as pd
import psutil
import gc
import os
import tracemalloc
#tracemalloc.start()

def get_memory_usage():
    """Returns current process memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB

def buggy_dataframe_operation():
        """Creates a DataFrame then crashes"""
        print("Thread started - creating DataFrame...")
        # Create a moderate-sized DataFrame
        df = pd.DataFrame({f'col_{i}': list(range(1000_000)) for i in range(50)})
        mem = get_memory_usage()
        print(f"Peak usage: {mem:.2f} MB")   
        
        df = None
        gc.collect()
        mem = get_memory_usage()
        print(f"After clearing memory: {mem:.2f} MB")   
        
        print('Thread completed')
       
        
def main():
    print("Python Thread Crash Memory Leak Demonstration")
    print("============================================")
    
    # Initial memory usage
    start_mem = get_memory_usage()
    print(f"Initial memory usage: {start_mem:.2f} MB")
    
    # Start the thread
  #  thread = threading.Thread(target=buggy_dataframe_operation)
  #  thread.start()
  #  thread.join()
    print('received thread')

    #buggy_dataframe_operation()

    df = pd.DataFrame({f'col_{i}': list(range(1000_000)) for i in range(50)})
    df = None
    
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
