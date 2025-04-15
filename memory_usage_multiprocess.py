import multiprocessing
import gc
import ctypes
import sys
import psutil
import pandas as pd
import time
import os
mem=None
def risky_operation():
    """Operation that might crash and leak memory"""
    print('starting risky operation')
    df = {f'col_{i}': list(range(1000_000)) for i in range(50)}
    time.sleep(1)
    mem=df
    # Force crash
    a = df['no_exist']

def run_in_process():
    """Isolate the risky operation in a process"""
    p = multiprocessing.Process(target=risky_operation)
    print('starting risky operation from run_in_process')
    p.start()
    print(f"Started memory: {psutil.Process().memory_info().rss/1024/1024:.2f} MB")

    p.join()
    print(f"After join memory: {psutil.Process().memory_info().rss/1024/1024:.2f} MB")


def macos_memory_cleanup():
    """macOS-specific cleanup functions"""
    if sys.platform == 'darwin':
        try:
            libc = ctypes.CDLL('libc.dylib')
            libc.malloc_zone_pressure_relief(None, 0)
            libsystem = ctypes.CDLL('/usr/lib/libSystem.dylib')
            libsystem.malloc_trim(0)
        except:
            pass

def main():
    print(f"Initial memory: {psutil.Process().memory_info().rss/1024/1024:.2f} MB")
    
    # Option 1: Run in thread (may leak)
    # Option 2: Run in process (better)
    run_in_process()
    
    # Aggressive cleanup
    for _ in range(3):
        gc.collect()
    
    # macOS specific cleanup
    macos_memory_cleanup()
    
    print(f"Final memory: {psutil.Process().memory_info().rss/1024/1024:.2f} MB")

if __name__ == '__main__':
    main()
