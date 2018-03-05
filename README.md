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
the package to the requirements.txt in your current directory:

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

## Detailed options

    `--upgrade` or `-U` install or upgrade the requested package(s)
    `--skip` or `-s` install or upgrade, but don't save the changes into your requirements file
    `--requirements` or `-r` path to the requirements file you wish to update

**NOTE:** Originally we tried to be *smart* and walk your file system backwards until we found a requirements.txt, but this can easily write the pip changes to a random requirements.txt on your system if you use a certain, fairly common, directory structure for your Python projects.  To avoid this confusion, we're going to be explicit and require that you run pipup from the top of a project or specify the requirements path directly yourself.

# Keep in touch!

If you have a question about this project, please open a GitHub issue. If you love us and want to keep track of our goings-on, here's where you can find us online:

<a href="https://revsys.com"><img src="https://pbs.twimg.com/profile_images/915928618840285185/sUdRGIn1_400x400.jpg" height="50" /></a>
<a href="https://twitter.com/revsys"><img src="https://cdn1.iconfinder.com/data/icons/new_twitter_icon/256/bird_twitter_new_simple.png" height="43" /></a>
<a href="https://www.facebook.com/revsysllc/"><img src="https://cdn3.iconfinder.com/data/icons/picons-social/57/06-facebook-512.png" height="50" /></a>
<a href="https://github.com/revsys/"><img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" height="53" /></a>
<a href="https://gitlab.com/revsys"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/GitLab_Logo.svg/2000px-GitLab_Logo.svg.png" height="44" /></a>
