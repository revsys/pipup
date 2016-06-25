# pipup - Better requirements.txt management

## Usage

Using pipup is easy:

    $ pipup Django

If Django is already installed, pipup will display the current version for you
like this:

    $ pipup Django
    Django is already installed!
    Django==1.8.11

If Django isn't installed, pipup will install it and save the pinned version of
the package to requirements.txt.  pipup is smart enough to walk up from your
current directory until it finds a requirements.txt to add it.
