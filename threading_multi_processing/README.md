# Threading & Multiprocessing — Quick Reference Notes

## Files
- `multi_threading.py`
- `thread_pool_executor.py`
- `fetch_parallel_urls.py`
- `multi_processing.py`
- `multi_processing_pool.py`
- `multiprocessing_queue.py`
- `share_value_between_process.py`

## The GIL (Global Interpreter Lock)
CPython only lets one thread execute Python bytecode at a time, even on a multi-core machine. This means threads don't give a real speedup for CPU-bound work (pure computation), but they still help for I/O-bound work (network calls, file/disk waits) since the GIL is released while waiting on I/O. Multiprocessing sidesteps the GIL entirely by running separate Python processes, each with its own interpreter and memory — real parallelism, but heavier.

## Multi-Threading
A thread runs inside the same process and shares memory with other threads in it. Created with `threading.Thread(target=fn, args=(...))`, started with `.start()`, and `.join()` blocks until it finishes (like `await` in JS). Best suited for I/O-bound tasks — network requests, file reads, waiting on external systems — where threads spend most of their time waiting rather than computing.

## ThreadPoolExecutor
A managed pool of worker threads from `concurrent.futures`, so threads don't need to be created/joined manually. `executor.map(fn, iterable)` runs `fn` across the pool and yields results in order. `max_workers` caps how many threads run concurrently. Ideal for batches of I/O-bound work (e.g. fetching many URLs, processing many files) — used with `requests` to parallelize HTTP calls in `fetch_parallel_urls.py`.

## Multi-Processing
A process has its own separate memory space, so variables/state in one process aren't visible in another (unlike threads). Created with `multiprocessing.Process(target=fn, args=(...))`, same `.start()` / `.join()` pattern as threads. Since each process runs on its own core with its own GIL, this is the right tool for CPU-bound work — heavy computation, number crunching, image/data processing.

## Multiprocessing Pool
`Pool(processes=n)` manages a fixed set of worker processes for you — analogous to ThreadPoolExecutor but for processes. `.map(fn, iterable)` splits the work across processes (map) and collects results back into one list (reduce). Always call `.close()` then `.join()` to clean up the pool after use.

## Sharing Data Between Processes
Because processes don't share memory by default, results computed inside a process aren't visible outside it unless explicitly shared:
- **Queue** (`multiprocessing.Queue`) — a thread/process-safe FIFO for passing data back to the parent; producer calls `.put()`, consumer calls `.get()`.
- **Shared memory** (`multiprocessing.Value`, `multiprocessing.Array`) — pre-typed shared variables (`"i"` = int, `"d"` = double) that multiple processes can read/write directly, avoiding the need to pass messages.

## asyncio vs Threading vs Multiprocessing
- **asyncio** — single thread, cooperative multitasking via `async`/`await`. Best for large numbers of I/O-bound tasks (thousands of concurrent network calls) with minimal overhead, since there's no thread/process creation cost.
- **Threading** — best for a moderate number of I/O-bound tasks, especially when working with libraries that aren't async-aware (e.g. blocking calls like `requests`). Limited by the GIL for CPU work.
- **Multiprocessing** — best for CPU-bound work that needs true parallelism across cores. Higher overhead (separate memory, slower startup) but bypasses the GIL entirely.
