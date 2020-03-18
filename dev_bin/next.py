from .common import findproject, runlines
from lagoon import git
import os

def main_next():
    'Go to next step in current git workflow.'
    gitdir = os.path.join(findproject(), '.git')
    if os.path.isdir(os.path.join(gitdir, 'rebase-apply')):
        if runlines(['git', 'status', '--porcelain']):
            git.rebase.__continue.print()
        else:
            git.rebase.__skip.print()
    elif os.path.isfile(os.path.join(gitdir, 'MERGE_HEAD')):
        git.commit.__no_edit.print()
    elif os.path.isfile(os.path.join(gitdir, 'CHERRY_PICK_HEAD')):
        git.cherry_pick.__continue.print()
    elif os.path.isfile(os.path.join(gitdir, 'REVERT_HEAD')):
        git.revert.__continue.print()
    else:
        raise Exception('Unknown git workflow, giving up.')