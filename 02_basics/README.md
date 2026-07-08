# Python Basics 02 — Quick Reference Notes

## Files
- `modules.py`
- `files.py`
- `error_handling.py`
- `calc.py`
- `exercise_script.py`

## Concepts

### pip
pip is Python's package manager, used to install third-party libraries from [PyPI](https://pypi.org/). Install with `pip install <package-name>`, remove with `pip uninstall <package-name>`.

### Modules
A module is just a `.py` file (built-in or your own) whose code can be reused via `import`. `dir(module)` lists everything available on it — useful for quick exploration. Common built-ins: `math` (`pow`, `pi`, `log10`, `floor`, `ceil`) and `calendar` (`month`, `isleap`).

### File Handling
Files are opened in a mode — `"r"` (read), `"w"` (write, overwrites), `"a"` (append). `with open(...) as f:` is the preferred pattern since it auto-closes the file. `f.read()` grabs the whole file at once; looping with `for line in f:` reads it line by line.

### Error Handling
`try` / `except` catches runtime errors so the program doesn't crash. Catch specific exceptions first (e.g. `ZeroDivisionError`), with a general `except Exception as e` as a fallback. `type(e).__name__` reveals the exception's class name for debugging. `input()` always returns a string, so cast it (`int(x)`) before using it as a number.
