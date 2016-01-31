import argparse

from pip_up.req_files import ReqFile


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
        'packages',
        type=str,
        nargs='+',
        help='PyPi packages to install',
    )

    return parser


def main_entry():
    parser = build_arg_parser()
    args = parser.parse_args()

    print("Save: {}".format(args.save))
    print("Requirements: {}".format(args.requirements_file))
    print("Packages: {}".format(args.packages))

    r = ReqFile()
    print(r.lines)
