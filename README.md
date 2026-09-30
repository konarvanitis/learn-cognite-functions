# Learning how to use Cognite Functions

A step by step guide with practical examples and code for using Cognite Python SDK.
https://cognite-docs.readthedocs-hosted.com/projects/cognite-sdk-python/en/latest/

## Getting Started

### Prerequisites

- Python 3.10 or 3.11
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### 1. Clone the repository

```bash
git clone https://github.com/cognitedata/learn-cognite-functions.git
```

### 2. Install dependencies

We recommend using uv to manage your Python virtual environment:

```bash
uv sync
```

This installs the dependencies defined in `pyproject.toml` and creates a virtual environment (`.venv`) in the project folder.

### 3. Run the notebooks

Open the repo in your IDE (e.g., VS Code) and start exploring the Jupyter notebooks.

> **Note:** You may need to select the uv virtual environment (`.venv`) as your kernel.

## Alternative: pip installation

If you prefer not to use uv, you can install the packages directly with pip:

```bash
pip install cognite-sdk msal pandas
```

## Additional notes for developers

### Add new libraries as needed

```bash
uv add pandas numpy
```

or if only required for development

```bash
uv add --dev pandas
```

### Set up clean notebook diffs (one-time, per clone)

Jupyter stamps your local kernel name and Python version into each notebook's metadata every time you run it, which shows up as noisy, unrelated diffs in `git status`/`git diff`. Run this once after cloning to strip that noise before it ever reaches git:

```bash
uv run nbstripout --install --attributes .gitattributes
git config filter.nbstripout.extrakeys "metadata.kernelspec metadata.language_info.version"
```

This registers a git filter that strips outputs, execution counts, and the kernel/version metadata from notebooks whenever git reads or diffs them — your local `.ipynb` files on disk are untouched, so notebooks still run and show outputs normally in your editor.
