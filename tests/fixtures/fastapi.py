import json, pytest
from fastapi.testclient import TestClient
from commando import create_app
from support import *

"""
Declare FastAPI fixtures.
"""

"""
Returns our application as a generator object that can be used in our tests.
"""
@pytest.fixture
def app():
    yield create_app()

"""
Returns a client associated with the application we can use for testing.
This is nice because we don't have to be concerned with setting up a connection
to an IP/port for the service we're testing.
"""
@pytest.fixture
def client(app):
    return TestClient(app)
