"""

PYTHONPATH is copied into sys.path at startup

# learn-python
export PYTHONPATH="/home/runner/workspace/learn-python:$PYTHONPATH"

# mvf
export PYTHONPATH="/home/runner/workspace:$PYTHONPATH"

# install requirements using
pip install -r requirements.txt

# list all packages with
pip list

# lint
ruff check --ignore E402

# astral tools
  ruff( linter and code formatter )
  uv( package manager )
  ty( real time type checking )


"""