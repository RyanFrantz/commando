import requests
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from commando.commands import process_command

router = APIRouter()

@router.post('/run', tags=['Commando'], summary='Run a command')
def process_interaction(channel_id:   str = Form(...),
                        channel_name: str = Form(...),
                        command:      str = Form(...),
                        response_url: str = Form(...),
                        team_domain:  str = Form(...),
                        team_id:      str = Form(...),
                        text:         str = Form(None), # We may not receive anything.
                        token:        str = Form(...),
                        trigger_id:   str = Form(...),
                        user_id:      str = Form(...),
                        user_name:    str = Form(...),
                       ):

    """
    'command' here is the Slack slash command, not the command/executable/script
    the user expects to run. Because we're not using it we'll not pass it along,
    to avoid any downstream confusion between the context of "command" being
    a Slack slash command versus "command" being the code the user intends to
    have executed.

    NOTE: The command (and related arguments) the user intends to have run will
    be found in the 'text' form field.
    """
    form_data = {
        'channel_id':   channel_id,
        'channel_name': channel_name,
        'response_url': response_url,
        'team_domain':  team_domain,
        'team_id':      team_id,
        'text':         text,
        'token':        token,
        'trigger_id':   trigger_id,
        'user_id':      user_id,
        'user_name':    user_name
    }
    process_command(form_data)

    # Slack API docs indicate we should always at least respond with 200 to
    # indicate receipt.
    return JSONResponse(status_code=200)
