import os
import subprocess
import warnings

warnings.filterwarnings("ignore")


class Freeze(object):
    """
    Handle getting information from 'pip freeze'
    """

    def __init__(self):
        self.lines = []

    def get(self):
        output = subprocess.check_output(
            args=['pip', 'freeze'],
            cwd=os.getcwd(),
        )

        for line in output.split(b'\n'):
            line = line.strip()
            self.lines.append(line)

    def find(self, pattern, clipboard=False):
        """ Find a pattern or package in pip list """
        FOUND = []

        # Get a pip freeze if we haven't already
        if not self.lines:
            self.get()

        for l in self.lines:
            l = l.decode('utf-8')
            if pattern in l:
                FOUND.append(l)

        if clipboard:
            # Write contents to clipboard
            self.write_to_clipboard(b"\n".join(FOUND))

        return FOUND
