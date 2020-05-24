import glob
from os.path import basename, dirname, isfile, join, realpath

ignore_list = [
    'README.md'
]

"""
Find any scripts in the commando/scripts/ directory and generate a dispatch
table.
"""
def script_commands():
    script_dispatch = {}
    this_dir = dirname(__file__)
    scripts_dir = realpath(join(this_dir, '..', 'scripts'))
    script_paths = glob.glob(join(scripts_dir, '*'))
    for path in script_paths:
        if not isfile(path):
            continue

        name = basename(path)
        if name in ignore_list:
            continue

        script_dispatch[name] = path

    return script_dispatch
