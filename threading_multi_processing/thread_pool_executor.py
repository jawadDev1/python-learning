# ThreadPoolExecutor
# Auto handle multiple threads instead of manually creating and managing them.
# handle the IO bound taks asynchrosnouly

import time
from concurrent.futures import ThreadPoolExecutor


def process_file(filename):
    time.sleep(1)
    return f"Processed {filename}"


files = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt"]

with ThreadPoolExecutor(max_workers=3) as executor:
    for result in executor.map(process_file, files):
        print(result)
