# pipup - Better requirements.txt management

## Installation

pipup is installed via pip:

    pip install pipup

## Usage

Using pipup is easy:

    $ pipup Django

If Django is already installed, pipup will display the current version for you
like this:

    $ pipup Django
    Looking for 'Django'
    Already installed:
    Django==1.9.7
    No changes to save, skipping save.

If Django isn't installed, pipup will install it and save the pinned version of
the package to requirements.txt.  pipup is smart enough to walk up from your
current directory until it finds a requirements.txt to add it:

    $ pipup Django
    Looking for 'Django'
    Installing 'Django'...
    Django==1.9.7
    Changes saved to /Users/frank/work/src/pipup/requirements.txt

If we have an older version of Django installed, say `Django==1.8.4` we can use
the `--upgrade` or `-U` option to upgrade Django and update our requirements:

    $ pipup -U Django
    Looking for 'Django'
    Already installed:
    Django==1.8.4
    Upgrading:
    Django==1.9.7
    Changes saved to /Users/frank/work/src/pipup/requirements.txt
