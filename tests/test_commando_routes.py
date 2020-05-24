import json, mock
from commando import errors

"""
Test the routes for the Jeli Commando Slack app.
"""

def test_commando(client, run_form):
    url = '/run'
    response = client.post(url, data={})
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'field required'
