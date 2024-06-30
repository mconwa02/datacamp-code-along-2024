# Datacamp Code Along 2024
Machine Learning in Production with Python

## Summary for Code-Along Session

**Background Context:**

In this code-along session, we will work with a dataset from a Portuguese banking institution's direct marketing campaigns, sourced from Kaggle. The dataset contains information about various marketing efforts, including telephonic outreach, aimed at promoting term deposits. Term deposits are significant for banks as they provide a stable income stream. Identifying and targeting potential customers effectively can enhance marketing efficiency and reduce costs.

https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets/data

**Tasks Covered:**

1. **Feature Engineering**:
   - We will develope functions to enhance the DataFrame with new features.
   - These functions were combined into a streamlined data transformation process using the Pandas `pipe` method.

2. **Unit Testing**:
   - We implemented unit tests using the `pytest` framework to ensure the new features were correctly added to the DataFrame.
   - The tests verified that the new columns were accurately calculated and correctly incorporated into the DataFrame.

Overall, this session provided practical experience in enhancing a dataset with valuable features and ensuring the robustness of these enhancements through thorough testing.

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

