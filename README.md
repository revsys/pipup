# pipup - Better requirements.txt management

So why pipup you ask? It's a silly small utility, but it solves some real issues
I have on a daily basis. The 3 most common things I need to do with pip are:

1. See if a package is installed and if so what version is installed?
2. Install a package and then save the installed version info into requirements.txt
3. Upgrade a package and change the entry in requirements.txt

Sadly, pip doesn't help us here so this is why I've created pipup. Running just
`pipup <package name>` or `pipup -U <package name>` *just does what I want*.  No
more forgetting to include or update a requirements.txt entry for me!

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
