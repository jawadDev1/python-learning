# Python Basics 02 — Learning Notes

A quick summary of the concepts covered in this practice folder.

## Files
- `modules.py` — importing and using built-in modules
- `files.py` — reading/writing files
- `error_handling.py` — try/except basics
- `calc.py` — custom module example (imported into other scripts)
- `exercise_script.py` — practice task
- `funny.txt`, `funny_wc.txt`, `test2.txt` — sample/output files used in exercises

## Concepts Covered

### pip
- Package manager for installing third-party libraries from [PyPI](https://pypi.org/)
- Install: `pip install <package-name>`
- Uninstall: `pip uninstall <package-name>`

### Modules
- `import <module>` to reuse code (built-in or your own `.py` files)
- `dir(module)` — lists all available methods/attributes on a module
- Built-in modules practiced: `math`, `calendar`
  - `math.pow(x, y)`, `math.pi`, `math.log10(x)`, `math.floor(x)`, `math.ceil(x)`
  - `calendar.month(year, month)`, `calendar.isleap(year)`
- Importing your own custom module (e.g. `calc.py`) and calling its functions

### File Handling
- Opening files with modes: `"w"` (write), `"a"` (append), `"r"` (read)
- Manual open/close: `f = open(...)`, `f.write(...)`, `f.close()`
- **Preferred pattern:** `with open("file.txt", "r") as f:` — auto-closes the file
- Reading a whole file: `f.read()`
- Reading line by line: `for line in f:`
- Writing processed output to a new file (e.g. word-count per line)

### Error Handling
- `try` / `except` blocks to catch runtime errors
- Catching specific exceptions first (e.g. `ZeroDivisionError`)
- Catching general exceptions with `except Exception as e`
- `type(e).__name__` — get the exception's type/name for debugging
- `input()` for reading user input (always comes in as a string — needs casting, e.g. `int(x)`)

## Mini Exercise Practiced
- A  script that reads content from one file and writes it to another file.
