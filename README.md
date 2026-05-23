# quote‑spark

`quote‑spark` is a **single‑file** Python command‑line tool that prints a random inspirational quote.

## Features
- No external runtime dependencies – just the Python standard library.
- Instantly runnable: `python -m quote_spark` or `./quote_spark.py` (make it executable).
- Tiny test suite (pytest) and linting (flake8) executed automatically on every push via GitHub Actions.

## Installation & Usage
```bash
# Clone the repo
git clone https://github.com/your‑username/quote‑spark.git
cd quote‑spark

# Run directly (requires Python ≥3.9)
python -m quote_spark
# or make it executable
chmod +x quote_spark.py
./quote_spark.py
```

## Contributing
Feel free to open issues or PRs – just keep the project tiny! If you add new functionality, update the test suite and ensure the CI passes.

## License
MIT – see [LICENSE](LICENSE) for details.
