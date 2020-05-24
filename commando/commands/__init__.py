from commando.commands.builtin import builtin_commands
from commando.commands.scripts import script_commands

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
