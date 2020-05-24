# Slash Commands

Interacting with Slack apps occurs via a few
[entrypoints](https://api.slack.com/interactivity/entry-points). Commando
currently supports a single slash command (`commando`) to invoke a workflow.

## `commando` Workflow

1. The `/commando` slash command is issued, resulting in an HTTPS call to the
   `/run` endpoint.
2. We split the `text` form field's value on whitespace, take the first item,
   and try to execute a script by the same name.
3. The form fields are passed as a single argument to the script in the form of
   a JSON object. The script is expected to parse it accordingly, using the
   content as needed.
