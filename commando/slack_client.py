import json, logging, requests
from datetime import datetime
from commando import errors, utils

"""
Encapsulate properties of a client for making requests to Slack.
"""
class SlackClient(object):
    """
    Create a client with the specified API key (required).
    """
    def __init__(self, api_key=None):
        self.logger  = utils.gen_logger('slack-client')

        if not api_key:
            msg = "Missing 'api_key' argument in SlackClient constructor."
            self.logger.error(msg)
            raise RuntimeError(msg)

        self.api_key  = api_key
        self.base_url = 'https://slack.com/api'

    def headers(self):
        headers = {
            'Content-Type': 'application/json'
        }
        return headers

    """
    Issue a POST request to the chat.postMessage API method.
    """
    def post_message(self, channel_id: str, message: str):
        url = '{}/chat.postMessage?token={}'.format(self.base_url, self.api_key)
        url += f'&channel={channel_id}'
        url += f'&text={message}'

        response = requests.post(url)
        response_body = json.loads(response.content.decode("utf-8"))
        if not response_body['ok']: # A bool
            raise errors.SlackResponseError(response_body)

    """
    Open a view (modal).
    """
    def open_view(self, trigger_id: str, view: str):
        url = '{}/views.open?token={}'.format(self.base_url, self.api_key)
        url += f'&trigger_id={trigger_id}'
        url += f'&view={view}'

        response = requests.post(url)
        response_body = json.loads(response.content.decode("utf-8"))
        if not response_body['ok']: # A bool
            raise errors.SlackResponseError(response_body)
