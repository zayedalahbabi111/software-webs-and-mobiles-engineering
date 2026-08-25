# Project Status

## What it does

Project Status reads the task list in `data/tasks.csv` and prints a report showing each task's owner and status, together with the number of completed tasks.

## Set up

From the `lab01` directory, create the project environment and install the locked dependencies:

```sh
uv sync
```

## Run

Run the report from the `lab01` directory:

```sh
uv run python -m project_status
```

## Check

Check formatting and lint rules, compare the report with the expected output, and run the unit tests:

```sh
uv run ruff format --check .
uv run ruff check .
uv run python -m project_status | diff - expected_output.txt
uv run python -m unittest discover -s tests
```
