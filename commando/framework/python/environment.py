"""
A set of functions that return values of environment variables.
"""
import os

"""
Given the name of an environment variable, return its value or an empty string
(if undefined). The variable names are expected to be upper-case.
"""
def fetch_environment_variable(name: str):
    name = name.upper()
    return os.environ.get(name, '')

def slack_channel_id():
    return fetch_environment_variable('slack_channel_id')

def slack_channel_name():
    return fetch_environment_variable('slack_channel_name')

def slack_response_url():
    return fetch_environment_variable('slack_response_url')

def slack_team_domain():
    return fetch_environment_variable('slack_team_domain')

def slack_team_id():
    return fetch_environment_variable('slack_team_id')

def slack_text():
    return fetch_environment_variable('slack_text')

def slack_token():
    return fetch_environment_variable('slack_token')

def slack_trigger_id():
    return fetch_environment_variable('slack_trigger_id')

def slack_user_id():
    return fetch_environment_variable('slack_user_id')

def slack_user_name():
    return fetch_environment_variable('slack_user_name')
