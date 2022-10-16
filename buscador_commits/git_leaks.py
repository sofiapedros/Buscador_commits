from git import Repo
import re  # signal
import time
import sys
import signal

REPO_DIR = './skale-manager'
KEY_WORDS = ['credentials', 'password', 'key', 'username', 'private']


def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits


def load():
    time.sleep(1)


def handler_signal(signal, frame):
    print("\n\n[!] Out ............. \n")
    sys.exit(1)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler_signal)
    commits = extract(REPO_DIR)
    for commit in commits:
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                print('Commit: {} - {}'.format(commit.hexsha, commit.message))
