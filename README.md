# ML Unit Testing

Small project for demonstrating unit tests around an ML pipeline using pytest.

## Summary

This repository contains a simple machine-learning pipeline (data loading, preprocessing, model training and evaluation) together with unit tests for core components.

## Project structure

- main.py - entry point for running the project
- requirements.txt - Python dependencies
- src/ - source code
  - config.py
  - dataloader.py
  - preprocessing.py
  - model.py
  - train.py
  - evaluate.py
- data/
  - Social_Network_Ads.csv
- tests/ - unit tests using `pytest`

## Setup

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running tests

Run the test suite with:

```bash
pytest -q
```

## Running the project

To run training or the main script:

```bash
python main.py
```

Or run individual modules, for example:

```bash
python src/train.py
```

## Contributing

Open an issue or submit a pull request. Keep unit tests green.

## License

MIT
