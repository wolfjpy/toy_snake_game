# Terminal-based Toy Snake Game

I spent a couple of off-work hours to create this toy snake game from scratch. Enjoy!

## Python Coding Skills

A list of selected coding skills demonstrated in the source code.

- data classes (new in Python 3.7)
- \_\_magic_methods\_\_
- decorator (@)
- list comprehension
- abstractmethod
- list, set, dict
- type hints
- *args (variable-length argument list)
- pytest
- pylint
- [pep8] (http://pep8.org/) (autopep8)
- virtualenv ([pipenv] (https://docs.pipenv.org/))
- [Python ASCII animations] (https://github.com/peterbrittain/asciimatics)
- [Google Style Python Docstrings] (http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Python package
- Modules
- Dynamic typing
- Mutable and immutable types
- Zen of Python
- Git

Note:

- yapf and black are good python formatters too.

## OOP Design

A list of selected OOP design demonstrated in the source code.

- Class / Object
- Abstraction
- Abstracted class / Interface
- Encapsulation
- Composition
- Inheritance
- Delegation
- Polymorphism
- UnitTest
- Test-driven Development
- MVC (Model-View-Controller)
- SOLID guidelines

Note:

- Extensibility:
	- Easy change game/render engine, e.g. implement Drawable interface. 
	- Easy add more game elements, e.g. create more snakes objects, more foods objects, and any shape of the walls in game World object.
	- Easy customized game logic, e.g. create another Logic class in logic module.

- Robustness:
	- UnitTest
	- Clearly separate Model, View, and Controller.

## Installation

Python version: **3.7**

Install pipenv (https://docs.pipenv.org/, highly recommended) first if you haven't.

Create Python 3.7 virtualenv, activiate it, install dependencies.

```bash
pipenv --python 3.7
pipenv shell
pipenv install
```

## Run Game

Make sure virtualenv is activated by `pipenv shell` from above.

Go to source code directory, run main entry point. Have fun!

```bash
cd toy_snake_game
python game.py
```
