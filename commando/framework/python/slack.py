from commando import errors
from commando.framework.python.environment import slack_channel_id, slack_team_id, slack_team_domain, slack_user_id
from commando.framework.python.logging import error
from commando.slack_client import SlackClient
from commando.utils import slack_api_key

"""
A convenience function to help posting to a Slack channel.
The channel_id is optional; if it's not provided, the channel ID will be
gleaned from the environment.
"""
def slack_message(msg: str, channel_id = None):
    try:
        api_key = slack_api_key(slack_team_id())
    # May be one of (at least):
    # * botocore.exceptions.NoCredentialsError (missing AWS credentials)
    # * botocore.errorfactory.ResourceNotFoundException (secret does not exist)
    except Exception as e:
        exc = str(e)
        msg = f'Failed to retrieve Slack API token from Secrets Manager: {exc}'
        error(msg)
        return

    slack_client = SlackClient(api_key)
    channel_id   = channel_id or slack_channel_id()
    try:
        slack_client.post_message(channel_id, msg)
    except errors.SlackResponseError as e:
        exc = str(e)
        workspace = self.form_data['team_domain']
        teamd_id  = self.form_data['team_id']
        msg = f"Failed to post message to channel ID '{channel_id})' " \
               " in workspace {workspace} (ID: {team_id}): {exc}"
        error(msg)
        return

"""
Looks up the current Slack user's information. That is, the one that issued
a command.
For any failure, logs it and returns None.
"""
def current_user():
    try:
        api_key = slack_api_key(slack_team_id())
    except Exception as e:
        exc = str(e)
        msg = f'Failed to retrieve Slack API token from Secrets Manager: {exc}'
        error(msg)
        return None

    slack_client = SlackClient(api_key)
    user_id      = slack_user_id()
    try:
        current_user = slack_client.fetch_user(user_id)
    except Exception as e:
        exc = str(e)
        msg = f"Failed to retrieve info for user '{user_id}': {exc}"
        error(msg)
        return None

    return current_user
