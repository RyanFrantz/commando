from commando import errors
from commando.slack_client import SlackClient
from commando.utils import gen_logger, slack_api_key

"""
No command was specified. Prompt the user to list available commands.
"""
def missing_command(form_data: dict):
    logger = gen_logger('missing-command')

    try:
        api_key = slack_api_key(form_data['team_id'])
    # May be one of (at least):
    # * botocore.exceptions.NoCredentialsError (missing AWS credentials)
    # * botocore.errorfactory.ResourceNotFoundException (secret does not exist)
    except Exception as e:
        exc = str(e)
        msg = f'Failed to retrieve Slack API token from Secrets Manager: {exc}'
        logger.error(msg)
        return

    help_msg = 'No command was specified. Run `/commando list` to see available commands.'
    slack_client = SlackClient(api_key)
    channel_id = form_data['channel_id']
    try:
        slack_client.post_message(channel_id, help_msg)
    except errors.SlackResponseError as e:
        exc = str(e)
        channel_name = form_data['channel_name']
        workspace    = form_data['team_name']
        teamd_id     = form_data['team_id']
        msg = f"Failed to post message to '{channel_name} (ID: {channel_id}) " \
               " in workspace {workspace} (ID: {team_id}): {exc}"
        logger.error(msg)
        return


def help():
    # TODO: Output to Slack.
    print("I'm here to help!")

"""
A dispatch table that collects all built-in commands hat can be run by Commando.
"""
builtin_commands = {
    'help': help
}
