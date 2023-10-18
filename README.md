# vPython

Run python scripts in their virtual environments.

## Install

```shell
pipx install git+https://github.com/Xdynix/vpython
```

## Usage

```shell
vpython some-script-in-venv.py arg1 arg2
```

## Example

```shell
virtualenv .venv
echo 'import sys; print(sys.executable)' > main.py

vpython main.py  # It should output tht python interpreter in virtual environment.
python main.py  # It should output system python, since virtual environment is not activated.
```
