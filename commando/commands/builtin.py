from commando import errors
from commando.commands.scripts import script_commands
from commando.slack_client import SlackClient
from commando.utils import gen_logger, slack_api_key

class BuiltinCommand:
    """
    Initialize a logger and save the form data received in the initial
    Slack interaction.
    """
    def __init__(self, form_data: dict):
        self.logger    = gen_logger('builtin-commands')
        self.form_data = form_data

    def slack_message(self, msg):
        try:
            api_key = slack_api_key(self.form_data['team_id'])
        # May be one of (at least):
        # * botocore.exceptions.NoCredentialsError (missing AWS credentials)
        # * botocore.errorfactory.ResourceNotFoundException (secret does not exist)
        except Exception as e:
            exc = str(e)
            msg = f'Failed to retrieve Slack API token from Secrets Manager: {exc}'
            self.logger.error(msg)
            return

        slack_client = SlackClient(api_key)
        channel_id   = self.form_data['channel_id']
        try:
            slack_client.post_message(channel_id, msg)
        except errors.SlackResponseError as e:
            exc = str(e)
            channel_name = self.form_data['channel_name']
            workspace    = self.form_data['team_name']
            teamd_id     = self.form_data['team_id']
            msg = f"Failed to post message to '{channel_name} (ID: {channel_id}) " \
                   " in workspace {workspace} (ID: {team_id}): {exc}"
            self.logger.error(msg)
            return

    """
    No command was specified. Prompt the user to list available commands.
    """
    def missing_command(self):
        msg = 'No command was specified. Run `/commando list` to see available commands.'
        self.slack_message(msg)

    def help(self):
        self.slack_message("I'm here to help!")

    """
    Provide the user with a list of available commands we know about.
    """
    def list(self):
        available_commands = {
            **BuiltinCommand.commands(),
            **script_commands()
        }
        commands = ', '.join('`' + cmd + '`' for cmd in sorted(available_commands))
        msg = f'The following commands are available: {commands}'
        self.slack_message(msg)

    """
    A dispatch table that collects all built-in commands that can be run by Commando.
    This registers our built-in commands in a way that allows us to use a
    BuiltinCommand class to manage behavior while also exporting the functions
    that back the commands. We expect that whatever uses this table instantiates
    a BuiltinCommand object and uses getattr() to find the attribute that backs
    the command. I think there is a better way to do this but this work for the
    time being.
    """
    @staticmethod
    def commands():
        builtin_commands = {
            'help': BuiltinCommand.help,
            'list': BuiltinCommand.list
        }
        return builtin_commands
