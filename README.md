# Datacamp Code Along 2024
Machine Learning in Production with Python

## Banking Dataset - Marketing Targets

Banking Dataset of different customers to predict if they will convert or not.
https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets

## Project Setup

To ensure a clean and isolated development environment, use a
virtual environment created with `venv` and manage dependencies using
`pyproject.toml`.

Additionally, set up pre-commit hooks for code quality checks,
including linting with Ruff.

## Creating a Virtual Environment

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

## Installing Dependencies

Once inside the virtual environment, install project dependencies from the `pyproject.toml` file:
```bash
pip install -e .
```

Poetry and pip-tools are excellent package managers. As pip won't necessarily
handle all dependencies and constraints as effectively as package managers

## Setting up Pre-commit Hooks and Linting

Use `pre-commit` to enforce code quality standards.
Additionally, use `ruff` for linting.
Both packages are in the `pyproject.toml` file for install.

https://pre-commit.com

Navigate to your project directory and set up pre-commit hooks:
```bash
pre-commit install
```

A `.pre-commit-config.yaml` file is in project directory with config for
ruff linting. Whenever you make a commit, `pre-commit` will run linting
with Ruff and enforce code quality standards automatically.

https://github.com/astral-sh/ruff-pre-commit

