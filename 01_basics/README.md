# Python Basics — Learning Notes

A quick summary of the core Python concepts covered in this practice folder.

## Files
- `01_data_types.py` — data types, lists, dicts, tuples
- `02_control_flow.py` — loops and conditionals
- `03_functions.py` — functions, args/kwargs, lambdas
- `exercise_1.py`, `exercise_2.py`, `exercise_3.py` — practice tasks

## Concepts Covered

### Data Types
- Basics: `int`, `float`, `str`, multi-line strings (`"""..."""`)
- `type()` and `id()` to inspect values
- Floor division `//` vs regular division `/`

### Lists
- Creating and indexing lists: `list[i]`
- Slicing: `list[1:3]` (start included, end excluded)
- Looping with `for item in list`

### Dictionaries
- Key-value pairs: `dict["key"]`
- Adding new keys: `dict["new_key"] = value`
- Looping with `.items()` to get key + value
- Nested dictionaries (dict of dicts)
- Lists of dictionaries

### Tuples
- Immutable, ordered collections: `(a, b, c)`
- Unpacking: `r, g, b = my_tuple`

### Sets
- Removing duplicates: `set(my_list)`
- Looping over unique values

### Functions
- Type hints: `def f(x: float) -> float:`
- Returning multiple values (as a tuple): `return a, b`
- `*args` — collect extra positional args into a tuple
- `**kwargs` — collect extra keyword args into a dict
- Lambda (anonymous) functions: `square = lambda x: x**2`

### Control Flow
- `if` / `else` conditionals
- `for` loops with `range(len(...))`
- String formatting with f-strings: `f"{value:.2f}"`

## Mini Exercises Practiced
1. Pass/fail checker + average calculator using a dictionary
2. Removing duplicate items using a set + a counting function
3. Hot/cold temperature classifier + Celsius-to-Fahrenheit lambda
