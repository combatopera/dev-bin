#HALP Satisfy PEP 8 with minimal impact.

from dev_bin.common import findproject
import subprocess, re

cols = 120

def main_brown():
    command = ['autopep8', '-rv', '--max-line-length', str(cols), findproject()]
    result = subprocess.run(command + ['-d'], stdout = subprocess.DEVNULL, stderr = subprocess.PIPE, universal_newlines = True)
    assert not result.returncode
    def paths():
        for line in result.stderr.splitlines():
            m = re.fullmatch(r'\[file:(.+)]', line)
            if m is not None:
                yield m.group(1)
    subprocess.check_call(['sed', '-ni', r'/\S/p'] + list(paths()))
    subprocess.check_call(command + ['-i'])