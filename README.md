# Basic Python Tools

## How to use project

### Developed with
```bash
python3.10 --version
# ❯ Python 3.10.11
```

### Environment set up
```bash
python3.10 -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
export PYTHONPATH="."
```

### Run linter
```bash
python -m pylint ./*
# ❯ --------------------------------------------------------------------
# ❯ Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Run tests
```bash
python -m coverage run -m unittest discover
# ❯ ..................
# ❯ ----------------------------------------------------------------------
# ❯ Ran 18 tests in 0.002s
# ❯
# ❯ OK
```

### Display coverage report
```bash
python -m coverage report -m
# ❯ Name                       Stmts   Miss  Cover   Missing
# ❯ --------------------------------------------------------
# ❯ dictionary.py                 30      0   100%
# ❯ tests/__init__.py              0      0   100%
# ❯ tests/test_dictionary.py      51      1    98%   143
# ❯ --------------------------------------------------------
# ❯ TOTAL                         81      1    99%
```


## Package docs
- [coverage](https://coverage.readthedocs.io)
- [pylint](https://pylint.readthedocs.io)
