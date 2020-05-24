"""
This script is used to build a package for the code in this project.
Run me via: `python3 setup.py sdist`
Then check the `dist/` subdirectory for a new package.
"""
import io, re
from setuptools import find_packages, setup

# Read the version from __init__.py.
with io.open('commando/__init__.py', 'r') as v:
    version = re.search(r'__version__ = \'(.*?)\'', v.read()).group(1)

# Read the long description from the README.
with io.open('README.md', 'r') as r:
    long_description = r.read()

# Classify this module.
project_classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: POSIX :: Linux"
]

"""
Read the requirements.txt file, strip any comments, and generate a list of
packages required to support this package when it's installed.
"""
def additional_modules():
    f = io.open('requirements.txt')
    content = f.read()
    packages = [line for line in content.split("\n") if not line.startswith('#')]
    return packages

setup(
    author                        = 'Ryan Frantz',
    author_email                  = 'ryan@jeli.io',
    classifiers                   = project_classifiers,
    description                   = "Jeli's Commando Slack App",
    install_requires              = additional_modules(),
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    name                          = 'commando',
    packages                      = find_packages(),
    url                           = 'https://github.com/Jeli-Inc/commando',
    version                       = version,
)
