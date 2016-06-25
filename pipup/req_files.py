import os
import re

import click

from .exceptions import (
    ReqFileNotFound, ReqFileNotReadable, ReqFileNotWritable
)

UNPINNED_RE = re.compile(r'^[0-9a-zA-Z_\-]+$')


class ReqFile(object):
    """
    Class to manage a requirements file
    """
    file_path = None

    def __init__(self, path=None, file_name='requirements.txt',
                 auto_read=True):
        self.file_name = file_name

        if path is None:
            self.file_path = self.find_requirements_file()
        else:
            self.file_path = path

        # Store requirements lines
        self.lines = []
        self.packages = {}

        if auto_read:
            self.read(self.file_path)

    def find_requirements_file(self):
        """
        Find the first requirements file matching file_name
        """
        for dirname, subdirs, files in os.walk(os.getcwd()):
            for fname in files:
                if fname == self.file_name:
                    return os.path.join(dirname, fname)

    def read(self, path):
        """
        Read in requirements file
        """
        if not os.path.exists(path):
            raise ReqFileNotFound("{} not found".format(path))

        if not os.access(path, os.R_OK):
            raise ReqFileNotReadable("{} not readable".format(path))

        if not os.access(path, os.W_OK):
            raise ReqFileNotWritable("{} not writeable".format(path))

        # Clear out any any existing lines
        self.lines = []

        with open(path) as f:
            for i, line in enumerate(f):
                self.parse_line(line, i)

    def parse_line(self, line, line_number):
        """
        Parse a line of our requirements file for later use
        """
        # Save line untouched to rewrite it
        self.lines.append(line.strip())

        if '==' in line:
            package, version = line.split('==')
            self.packages[package] = version

        if UNPINNED_RE.match(line):

            click.secho(
                "WARNING: Found unpinned package '{}' at line {}.".format(
                    line.strip(),
                    line_number,
                ),
                fg='red',
            )

    def save(self, lines):
        """
        Save these lines to the requirements.txt file
        """
        # Don't do anything if there isn't anything to do
        if not lines:
            return False

        # Always re-read in case something has changed
        self.read(self.file_path)

        new_lines = []

        for r in lines:
            FOUND = False

            for l in self.lines:
                l = l.strip()

                # Skip lines we can't handle
                if '==' not in l:
                    new_lines.append(l)
                    continue

                pkg, version = l.split('==', 1)

                if pkg in r:
                    new_lines.append(r)
                    FOUND = True
                else:
                    new_lines.append(l)

            if not FOUND:
                new_lines.append(r)

        with open(self.file_path, 'w') as f:
            for l in new_lines:
                f.write("{}\n".format(l))

        return True
