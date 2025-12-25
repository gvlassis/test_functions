# test_functions

## Description
Simple Python methods for testing via functions. The terminal output is unbuffered, colorful and with appropriate unicode symbols.

## Getting Started
1) Install/update(-U) test_functions from GitHub

```bash
pip install -U git+https://github.com/gvlassis/test_functions
```

2) Write your own testing methods, that compare a tuple (`test()`), or/and a list of tuples (`test_tuples()`)

```python
import test_functions

def test1():
    test_functions.test(2, 1+1)

def test2():
    test_functions.test_tuples([(3, 1+2), (3, 2+1)]
```

3) Call your testing methods via `test_functions()`

```python
test_functions.test_functions([test1, test2])
```
