from lagoon import paplay, pgrep
from pathlib import Path
import os, subprocess, sys, time

sleeptime = .5
soundpath = Path('/usr/share/sounds/freedesktop/stereo/complete.oga')
threshold = 5

class Child:

    def __init__(self, start):
        self.start = start

    def fire(self, now):
        if self.start + threshold <= now and soundpath.exists() and not os.fork():
            paplay.exec(soundpath)

def main_taskding():
    shpidstr, = sys.argv[1:]
    children = {}
    while True:
        nowchildren = {}
        now = time.time()
        try:
            with pgrep.bg('-P', shpidstr) as stdout:
                for line in stdout:
                    nowchildren[int(line)] = Child(now)
        except subprocess.CalledProcessError:
            break
        for pid in children.keys() - nowchildren.keys():
            children.pop(pid).fire(now)
        for pid, child in nowchildren.items():
            if pid not in children:
                children[pid] = child
        time.sleep(sleeptime)