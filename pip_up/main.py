import argparse
import copy
import subprocess
import sys
import os
import warnings

from termcolor import cprint

from pip_up.req_files import ReqFile
from pip_up.freeze import Freeze

warnings.filterwarnings("ignore")


def build_arg_parser():
    """
    Build argparse parser
    """
    parser = argparse.ArgumentParser(
        description='Install or upgrade a pip package and save it to requirements.txt',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--save',
        dest='save',
        action='store_true',
        help="Don't store in requirements.txt",
    )

    parser.add_argument(
        '--requirements',
        dest='requirements_file',
        default='requirements.txt',
        help='Name of requirements file',
    )

    parser.add_argument(
        '-U', '--upgrade',
        dest='upgrade',
        action='store_true',
        help="Upgrade package even if already installed",
    )

    parser.add_argument(
        '-f', '--find',
        dest='find',
        action='store_true',
        help="Find and return currently installed requirement",
    )

    parser.add_argument(
        '-n', '--no-copy',
        dest='clipboard',
        action='store_false',
        help="Do not copy package file requirement lines to clipboard",
    )

    parser.add_argument(
        'packages',
        type=str,
        nargs='+',
        help='PyPi packages to install',
    )

    return parser


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
    freeze = Freeze()
    values = []

    for p in packages:
        res = freeze.find(p)
        if res:
            values.extend(res)
            print("\n".join(res))
        else:
            cprint(" *** Could not find '{}' ***".format(p), 'red')

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
            cprint("ERROR: '{}' seems to exist:".format(p), 'red')
            print("\n".join(found))
            cprint('exiting...', 'red')
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
        cprint('No packages changed.', 'red')

    return values


def main_entry():
    parser = build_arg_parser()
    args = parser.parse_args()

    # Grab current requirements
    if '/' in args.requirements_file:
        req = ReqFile(file_path=args.requirement_file)
    else:
        req = ReqFile(file_name=args.requirements_file)

    if args.find:
        cprint("Looking for '{}'".format(", ".join(args.packages)))
        packages = handle_find(req=req, packages=args.packages)
    else:
        if args.upgrade:
            cprint("Installing '{}'".format(", ".join(args.packages)))
        else:
            cprint("Installing and/or upgrading '{}'".format(", ".join(args.packages)))

        packages = handle_install(
            req=req,
            packages=args.packages,
            upgrade=args.upgrade,
        )

        # Optionally save
        if args.save:
            if req.save(packages):
                cprint('Changes saved to {}'.format(req.file_path), 'green')
            else:
                cprint('No changes to save, skipping save.', 'green')

    # Optionally copy to the clipboard
    if args.clipboard:
        write_to_clipboard("\n".join(packages))


    sys.exit(0)

