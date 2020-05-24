import os

"""
Provide support functions that can be used across all fixture code.
"""

"""
Return an absolute path to a fixture data file given its relative path beneath
tests/fixtures/data. This is a convenience function to reduce typing.
"""
def fixture_path(relative_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, 'fixtures/data', relative_path)

"""
Read a fixture file and return its contents.
"""
def get_fixture_data(relative_path):
    full_path = fixture_path(relative_path)
    with open(full_path) as f:
        data = f.read()
    return data
