# ayods

[![Version](https://img.shields.io/pypi/v/ayods.svg)](https://pypi.org/project/ayods/)
[![License](https://img.shields.io/pypi/l/ayods.svg)](#)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/ayods.svg)](https://pypi.python.org/pypi/ayods)

`ayods` is a Python CLI tool for initializing data science project structures with ease. Choose from minimal, standard, or professional templates to quickly set up your project.

## Features

- **Interactive CLI**: Guides you through setting up your project.
- **Predefined Templates**: Select from Minimal, Standard, or Professional project structures.
- **Notebook and Data Handling**: Automatically organizes directories for notebooks and datasets.
- **Customizable**: Extend templates to suit your workflow.

## Installation

First, ensure you have Python 3.8+ installed. Then, install `ayods` using pip:

```bash
pip install ayods
```

Alternatively, you can install the latest version from GitHub:

```bash
git clone https://github.com/SandWithCheese/ayods.git
cd ayods
pip install .
```

## Usage

Run the following command to initialize a new project:

```bash
usage: ayods [-h] [-v] [dirname]

Python CLI tool for initializing data science projects

positional arguments:
  dirname        Directory name to initialize the data science project

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

## Requirements

- Python 3.8+
- questionary 2.1.0 (not yet tested with other versions)

## TODO

- [ ] Add full documentation support
- [ ] Add tests for all modules
- [ ] Add support for custom templates

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
