# Basic Python Tools

## How to use project

### Developed with
```bash
python3.9 --version
# ❯ Python 3.9.16
```

### Environment set up
```bash
python3.9 -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
export PYTHONPATH="./src"
```

### Format Imports
```bash
isort src
# ❯ Fixing PATH_TO_PROJECT/src/tests/test_dictionary.py
```

### Format Code
```bash
black src
# ❯ All done! ✨ 🍰 ✨
# ❯ 4 files left unchanged.
```

### Run linter
```bash
python -m pylint src
# ❯ --------------------------------------------------------------------
# ❯ Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

# OR
python -m flake8 src
```

### Run tests
```bash
python -m coverage run -m unittest discover src
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
# ❯ src/dictionary.py                 30      0   100%
# ❯ src/tests/__init__.py              0      0   100%
# ❯ src/tests/test_dictionary.py      51      1    98%   135
# ❯ --------------------------------------------------------
# ❯ TOTAL                         81      1    99%
```


## Package docs
- [coverage](https://coverage.readthedocs.io)
- [pylint](https://pylint.readthedocs.io)
- [isort](https://pycqa.github.io/isort)
- [flake8](https://flake8.pycqa.org)
- [black](https://black.readthedocs.io)
