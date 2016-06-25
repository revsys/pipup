import click
import copy
import subprocess
import sys
import os
import warnings

from .req_files import ReqFile
from .freeze import Freeze

warnings.filterwarnings("ignore")

freeze = Freeze()


def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={
            'LANG': 'en_US.UTF-8',
        },
        stdin=subprocess.PIPE,
    )
    process.communicate(output.encode('utf-8'))


def handle_find(req, packages, clipboard=False):
    """ Find one or more packages """
    values = []

    for p in packages:
        res = freeze.find(p)
        if res:
            values.extend(res)
            print("\n".join(res))
        else:
            click.secho(" *** Could not find '{}' ***".format(p), fg='red')

    return values


def handle_install(req, packages, upgrade=False):
    """ Install or upgrade a package """
    originals = []
    values = []
    f = Freeze()

    # Get all of the original matching lines to output only those lines that
    # changed
    for p in packages:

        found = f.find(p)

        if not upgrade and found:
            click.secho("ERROR: '{}' seems to exist:".format(p), fg='red')
            click.echo("\n".join(found))
            click.secho('exiting...', fg='red')
            sys.exit(-1)

        originals.extend(found)

    cmd = ['pip', 'install']
    if upgrade:
        cmd.append('-U')

    for p in packages:
        command = copy.copy(cmd)
        command.append(p)

        output = subprocess.check_output(
            args=command,
            cwd=os.getcwd(),
        )

        f = Freeze()
        val = f.find(p)

        for v in val:
            if v not in originals:
                values.append(v)

    if not values:
        click.secho('No packages changed.', fg='red')

    return values


@click.command()
@click.option('--upgrade', '-U', default=False, help="Upgrade if package already exists", is_flag=True)
@click.option('--skip', '-s', default=False, help="Skip saving to requirements.txt", is_flag=True)
@click.option('--requirements', '-r', default=None, help="Path to requirements.txt file to update", type=click.Path(exists=True))
@click.argument('packages', nargs=-1)
def cli(upgrade, skip, requirements, packages):
    """
    Smart management of requirements.txt files
    """
    if not packages:
        click.secho("No packages listed, try pipup --help")
        sys.exit(-1)

    # Grab current requirements
    if requirements is not None:
        req = ReqFile(path=requirements)
    else:
        req = ReqFile()

    found_packages = []
    upgraded_packages = []
    installed_packages = []

    click.secho("Looking for '{}'".format(", ".join(packages)), fg='green')
    for pkg in packages:
        found = freeze.find(pkg)

        if found:
            found_packages.extend(found)
            click.secho("Already installed:", fg='green')
            for f in found:
                click.secho(f)

            if upgrade:
                click.secho("Upgrading:", fg='green')
                upgrades = handle_install(
                    req=req,
                    packages=[pkg],
                    upgrade=upgrade,
                )

                for u in upgrades:
                    click.secho(u)

                upgraded_packages.extend(upgrades)
        else:
            click.secho("Installing '{}'...".format(pkg), fg='green')

            installs = handle_install(
                req=req,
                packages=[pkg],
                upgrade=upgrade,
            )

            for i in installs:
                click.secho(i)

            installed_packages.extend(installs)

        # Save unless we're told otherwise
        if not skip:
            all_packages = installed_packages + upgraded_packages
            if not req.exists:
                click.secho("Can't find a requirements.txt! You'll need to either create one or update yours manually.", fg='red')

            if req.save(all_packages):
                click.secho('Changes saved to {}'.format(req.file_path), fg='green')
            else:
                click.secho('No changes to save, skipping save.', fg='green')
