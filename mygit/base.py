import os

from . import data


def is_ignored(path):
    return '.ugit' in path.replace('\\', '/').split('/')


def write_tree():
    for root, _, filenames in os.walk('.'):
        for filename in filenames:
            path = os.path.join(root, filename)
            if is_ignored(path):
                continue
            print(path)
