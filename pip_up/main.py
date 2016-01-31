import sys
import argparse
import subprocess

from termcolor import cprint

from pip_up.req_files import ReqFile
from pip_up.freeze import Freeze


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
        action='store_false',
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
        res = freeze.find(p, clipboard=False)
        if res:
            values.append(res)
        else:
            cprint(" *** Could not find '{}' ***".format(p), 'red')

    return values


def handle_install(req, packages, upgrade=False):
    pass


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
        packages = handle_install(
            req=req,
            packages=args.packages,
            upgrade=args.upgrade,
        )

    # Optionally copy to the clipboard
    if args.clipboard:
        write_to_clipboard("\n".join(packages))

    sys.exit(0)

