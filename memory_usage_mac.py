import pandas as pd
import psutil
import gc 
print(f"Memory 1: {psutil.Process().memory_info().rss / 1024**2:.2f} MB")
df = {f'col_{i}': list(range(1000_000)) for i in range(50)}
print(f"Memory 2: {psutil.Process().memory_info().rss / 1024**2:.2f} MB")

df = None
                
print(f"Memory 3: {psutil.Process().memory_info().rss / 1024**2:.2f} MB")
gc.collect()
                
print(f"Memory 4: {psutil.Process().memory_info().rss / 1024**2:.2f} MB")
