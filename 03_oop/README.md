# Python Basics 03 — Quick Reference Notes

## Files
- `decorators.py`
- `generators.py`
- `iterator.py`
- `objects_classes.py`
- `raise_exceptions.py`
- `library_project.py`

## Concepts

### Decorators
A decorator is a function that wraps another function to add extra behavior (logging, timing, access control) without changing its code. Applied with `@decorator_name` above a function definition. Common use case: measuring execution time or wrapping repeated setup/teardown logic.

### Generators
A generator is a function that uses `yield` instead of `return`, producing values one at a time and pausing state in between. Memory-efficient for large or infinite sequences since values are generated lazily instead of all at once. Iterated with `next()` or a `for` loop.

### Iterators
An iterator is any object with `__iter__()` and `__next__()` methods, allowing it to be looped over one item at a time. `iter()` gets an iterator from an iterable; `next()` pulls the next value; `StopIteration` signals the end. Custom classes can be made iterable by implementing these two dunder methods. `reversed()` gives an iterator that walks a sequence backwards.

### Classes & Objects
A class is a blueprint for creating objects with shared attributes (`__init__`) and behavior (methods). Inheritance lets a subclass reuse and extend a parent class's behavior — `issubclass()` and `isinstance()` check these relationships. Pydantic's `BaseModel` is a class type that enforces data types on attributes automatically (validation at object creation).

### Exceptions
`raise` manually triggers an exception, either a built-in one (`MemoryError`, etc.) or a custom one. Custom exceptions are made by subclassing `Exception` and can carry extra data/methods. Caught with `try` / `except SpecificError as e`, falling back to `except Exception` for anything unhandled.
