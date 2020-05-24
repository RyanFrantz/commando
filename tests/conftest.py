import json, os, pytest
from commando import create_app
from fixtures.fastapi import *
from fixtures.commando import *

"""
pytest automatically detects this file.
Most fixtures are imported from the 'fixtures' subdirectory so that we can
maintain clean, legible code.
"""
