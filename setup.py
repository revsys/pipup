from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Grab the version from bumpversion
with open(path.join(here, ".version"), encoding="utf-8") as f:
    version = f.read()
    version = version.strip()

setup(
    name="pipup",
    version=version,
    description="Install or update pip dependency and save it to requirements.txt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Frank Wiles",
    author_email="frank@revsys.com",
    url="https://github.com/revsys/pipup",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click==7.0"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points="""
        [console_scripts]
        pipup=pipup.main:cli
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
