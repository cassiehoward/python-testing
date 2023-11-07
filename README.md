# CICD
## Step 1: Create a .github/workflows directory

1. In your git repository, create a directory named `.github/workflows`. This is where you will define your workflow files.

## Step 2: Create a Workflow File

2. Inside the `.github/workflows` directory, create a new YAML file that defines your workflow. You can name this file whatever you like, but it should have the `.yml` file extension.

Here's a simple example of a GitHub Actions workflow file for a Python project that runs tests on each push to the main branch:

```yaml
name: Python CI

on:
  push:
    branches:
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
      working-directory: .

    - name: Run tests
      run: |
        pytest
      working-directory: .
```

## Step 3: Create a requirements.txt file

3In your git repository, create a file named `requirements.txt`. 
Here's a simple example of a requirements.txt:
```commandline
pytest
```
