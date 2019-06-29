import os
import pytest

from pathlib import Path


@pytest.fixture
def requirements_files():
    """
    Load all of our requirements files as strings in a dict for use in tests
    """
    # Return data
    requirements_strings = {}

    # Path to our files
    req_dir = Path(__file__).parent / "requirements_files"

    for file_path in os.listdir(str(req_dir)):
        with open(req_dir / file_path) as f:
            requirements_strings[str(file_path)] = f.read()

    return requirements_strings
