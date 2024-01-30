# DS Python HW

HW source code for course MIPT/Data Science

## Prerequisites

- [python 3.11](https://www.python.org/downloads)
- [poetry](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)

Install dependencies with poetry:

```sh
poetry install
```

Running notebooks with jupyter lab:

```sh
poetry run jupyter lab
```

## HWs:

### Guessing number based on random input from interval [1, 100].

[solution](./src/game_core.py) uses double pointer technique and minimises interval on
each iteration.

Test parametrised with 1000 random values based on numpy `np.random.randint` method.
Test asserts number of attempts to be less than 20 for each iteration.
To run tests use:

```sh
poetry run pytest tests/test_game_core.py
```

Solution is duplicated in [guess_number notebook](./notebooks/guess_number.ipynb)

### HeadHunter CV analysis.

#### Prerequisites

Data dump with CVs from hh.ru is available via [link](https://drive.google.com/file/d/1EzqRRuSg1sGORzAssQ8J1VZsAydAVfqu/view?usp=drive_link)
