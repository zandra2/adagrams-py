# Details About How to Run Tests

Run all tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

If you want to run all tests that exist in one file, use:

```bash
# Must be in activated virtual environment
$ pytest tests/test_file_name.py
```

... where `test_file_name.py` is replaced with the correct test file name.

If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest -s
```
