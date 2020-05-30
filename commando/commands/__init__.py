from commando.commands.builtin import builtin_commands, missing_command
from commando.commands.scripts import script_commands
import inspect, subprocess

"""
A dispatch table that collects all built-in commands and scripts that can be
run by Commando.

We combine two dictionaries into one. Keys from the latter may override the
former. Using the double splat (**) is a Pythonic way to pass keyword
arguments.
"""
available_commands = {
    **builtin_commands,
    **script_commands()
}

"""
Run a built-in function.
"""
def run_function(cmd, args):
    # TODO: Catch errors
    # Ex. TypeError: help() takes 0 positional arguments but 1 was given
    if args:
        cmd(args)
    else:
        cmd()
"""
Run a script.
"""
def run_script(cmd, args):
    # Concatenate the command and arguments, if any.
    if args:
        cmd = f'{cmd} {args}'

    # TODO: Eventually we'll implement proper logging here.
    try:
        # NOTE: Do we ever want to use the list form of subprocess.run()?
        #process = subprocess.run(cmd, check=True, capture_output=True) # Python 3.7
        process = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # Python 3.6
        msg = f'status={process.returncode} stdout={process.stdout.decode("utf-8")} stderr={process.stderr.decode("utf-8")}'
        print(msg)
    except subprocess.CalledProcessError as process:
        msg = f'status={process.returncode} stdout={process.stdout.decode("utf-8")} stderr={process.stderr.decode("utf-8")}'
        print(msg)

"""
Determine if we have a built-in function of a script and run it accordinly.
"""
def run(cmd, args):
    if inspect.isfunction(cmd):
        run_function(cmd, args)
    else:
        run_script(cmd, args)

"""
Given form data sent by Slack when a slash command was received, determine if
we know how to run the intended command and do so.

The expected form data looks like the following data structure:

form_data = {
    channel_id:   channel_id,
    channel_name: channel_name,
    response_url: response_url,
    team_domain:  team_domain,
    team_id:      team_id,
    text:         text,
    token:        token,
    trigger_id:   trigger_id,
    user_id:      user_id,
    user_name:    user_name
}
"""
def process_command(form_data):
    if not form_data['text']:
        missing_command(form_data)
        return

    # text = 'my_command arg1 arg2 arg3'
    text = form_data['text']
    # command = 'my_command', args = 'arg1 arg2 arg3'
    command = text.split()[0]
    # There may be no arguments.
    try:
        args = text.split(" ", maxsplit=1)[1]
    except IndexError:
        args = None

    known_command = available_commands.get(command)
    if known_command:
        run(known_command, args)
    else:
        print('Command NOT found!')
