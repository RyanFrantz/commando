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

    """
    A generator function that supports paginated responses. It will yield a
    response object for each request. If it notes a 'next_cursor' value in the
    response body it will craft the approriate next request URL and issue it.
    This function re-raises exceptions it may encounter.
    """
    def paged_responses(self, url):
        orig_url = url # We may need to concatenate cursor parameters.
        while True:
            try:
                response = requests.get(url)
                yield response
            except requests.exceptions.RequestException as e:
                msg = "Failed to complete request to '{}': {}".format(url, e)
                self.logger.error(msg)
                raise

            try:
                response_body = json.loads(response.content.decode("utf-8"))
                try:
                    next_cursor = response_body['response_metadata']['next_cursor']
                    if next_cursor:
                        # Include the cursor parameter for the next iteration.
                        url = orig_url + '&cursor={}'.format(next_cursor)
                    else:
                        # Sometimes the key exists but the value is an empty string.
                        msg = 'There are no more paged responses'
                        self.logger.info(msg)
                        break
                except KeyError:
                    msg = 'There are no more paged responses'
                    self.logger.info(msg)
                    # There are no more pages to request.
                    break
            except json.decoder.JSONDecodeError as e:
                msg = "Failed to parse JSON response for '{}': {}".format(url, e)
                self.logger.error(msg)
                raise

    """
    General support for issuing GET requests for a resource.
    Expects a URL and Slack resource type (i.e. messages, members). The
    resource type refers to the dictionary key under which the objects we're
    looking for reside.
    Returns an HTTP status code, status message, and a list of the given resource.
    """
    def get_resource(self, url, resource_type):
        all_resources = []
        try:
            for response in self.paged_responses(url):
                response_body = json.loads(response.content.decode("utf-8"))
                # Slack returns HTTP 200 with an error message on failure (ok: False)
                # Cases we've seen so far include invalid_auth and channel_not_found.
                if not response_body['ok']: # A bool
                    raise errors.SlackResponseError(response_body['error'])
                resources     = response_body[resource_type]
                all_resources += resources
        except KeyError as e:
            msg = "Failed to locate '{}' resource in response for '{}".format(resource_type, url)
            self.logger.error(msg)
            raise
        except json.decoder.JSONDecodeError as e:
            msg = "Failed to parse JSON response for '{}': {}".format(url, e)
            self.logger.error(msg)
            raise
        # Re-raise anything else; it likely bubbled up from paged_responses and was logged.
        except Exception as e:
            msg = 'Unhandled exception: {}'.format(e)
            self.logger.error(msg)
            raise

        return all_resources

    """
    Similar to get_resource() except it only expects a single resource to be
    returned (i.e. there should be no paged responses).
    """
    def get_single_resource(self, url, resource_type):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            msg = "Failed to complete request to '{}': {}".format(url, e)
            self.logger.error(msg)
            raise

        try:
            response_body = json.loads(response.content.decode("utf-8"))
            # Slack returns HTTP 200 with an error message on failure (ok: False)
            # Cases we've seen so far include invalid_auth and channel_not_found.
            if not response_body['ok']: # A bool
                raise errors.SlackResponseError(response_body['error'])
            return response_body[resource_type]
        except KeyError as e:
            msg = "Failed to locate '{}' resource in response for '{}".format(resource_type, url)
            self.logger.error(msg)
            raise
        except json.decoder.JSONDecodeError as e:
            msg = "Failed to parse JSON response for '{}': {}".format(url, e)
            self.logger.error(msg)
            raise
        # Re-raise anything else; it likely bubbled up from paged_responses and was logged.
        except Exception as e:
            msg = 'Unhandled exception: {}'.format(e)
            self.logger.error(msg)
            raise

    """
    Fetch a Slack user.
    """
    def fetch_user(self, user_id: str):
        url = f'{self.base_url}/users.info?token={self.api_key}&user={user_id}'
        try:
            user = self.get_single_resource(url, 'user')
        except Exception as e:
            msg = f'Failed to fetch resource: {str(e)}'
            self.logger.error(msg)
            raise

        return user
