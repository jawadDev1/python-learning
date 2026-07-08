# Python Basics 01 — Quick Reference Notes

## Files
- `01_data_types.py`
- `02_control_flow.py`
- `03_functions.py`
- `exercise_1.py`, `exercise_2.py`, `exercise_3.py`

## Concepts

### Data Types
Python's core types are `int`, `float`, and `str`, with `"""..."""` for multi-line strings. `type()` shows a value's type, `id()` shows its memory address. `//` does floor division (drops the decimal), while `/` gives a regular float result.

### Lists
A list is an ordered, mutable collection, indexed with `list[i]`. Slicing (`list[1:3]`) pulls a sub-range — start included, end excluded. Loop over items directly with `for item in list`.

### Dictionaries
A dictionary stores key-value pairs, accessed with `dict["key"]` and extended with `dict["new_key"] = value`. `.items()` loops over both key and value at once. Dictionaries can be nested (dict of dicts) or collected into a list (list of dicts) for structured records.

### Tuples
A tuple is an immutable, ordered collection — fixed once created, unlike a list. Values can be unpacked directly into variables: `r, g, b = my_tuple`.

### Sets
A set holds unique, unordered values — passing a list into `set()` strips out duplicates automatically. Iterable like any other collection with `for item in set`.

### Functions
Type hints (`def f(x: float) -> float:`) document expected input/output types without enforcing them at runtime. A function can return multiple values at once as a tuple. `*args` gathers extra positional arguments into a tuple; `**kwargs` gathers extra keyword arguments into a dict. Lambdas are single-expression anonymous functions: `square = lambda x: x**2`.

### Control Flow
`if` / `else` handles branching logic. `for` loops commonly pair with `range(len(...))` when an index is needed alongside the value. F-strings (`f"{value:.2f}"`) handle inline formatting, including decimal precision.

## Next Steps
- List/dict/set comprehensions
- Error handling (`try`/`except`)
- Classes and objects (OOP basics)
- File I/O (reading/writing files)

## Mini Exercises Practiced
1. Pass/fail checker + average calculator using a dictionary
2. Removing duplicate items using a set + a counting function
3. Hot/cold temperature classifier + Celsius-to-Fahrenheit lambda
