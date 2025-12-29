
import csv
from itertools import islice
from collections import Counter, defaultdict

with open('test_sales.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)  # Skip header
    
    while True:
        chunk = list(islice(reader, 3))  # Small chunks for testing
        if not chunk: break
        
        print("Chunk:", chunk)
        # Process: user -> actions set (deduping)
