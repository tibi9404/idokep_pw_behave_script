# Playwright with Behave Project

## Overview

This project uses Playwright with Behave to perform automated end-to-end testing. The output files, including result files, are generated in the `output_files` folder in the root directory. The `output_files` folder is emptied before every run to ensure clean results.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Playwright
- Behave

## Project Structure

repository/
├── features/ │
│├── environment.py │
│├── steps/ │
││ └── steps.py │
│└── example.feature
├── output_files/
└── README.md

## How to run the tests

```sh
behave
```
