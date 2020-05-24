import pytest

@pytest.fixture
def run_form():
    """
    This example was captured via tcpdump.
    Details have been obscured to protect the innocent.
    """
    form_body = {
        'token':        'So12345678asdfghjk',
        'team_id':      'TEAMJELI1',
        'team_domain':  'jelitalk',
        'channel_id':   'DREAMBIG',
        'channel_name': 'directmessage',
        'user_id':      'UFGUTHD2M',
        'user_name':    'ryan',
        'command':      '%2Fincident-package',
        'text':         'some random text',
        'response_url': 'https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ',
        'trigger_id':   '1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52',
    }
    return form_body
