import boto3, json, logging
from commando.recording import handlers

"""
A set of methods that are common to various components.
"""

"""
Generate and return a logger object.
Expects a service type that will be used to name the logger as well as define
the service name in the log handlers.
"""
def gen_logger(service_type='generic'):
    logger_name = 'commando-{}'.format(service_type)
    logger      = logging.getLogger(logger_name)
    logger.addHandler(handlers.CommandoServiceHandler(service_type))
    logger.addHandler(handlers.CommandoServiceErrorHandler(service_type))
    logger.setLevel(logging.INFO)
    return logger

"""
Given a Slack team ID (identifies a workspace), attempt to look up the API key
we have for our app. This assumes the Jeli Slack app has been authorized to
operate within the given workspace and that we've successfully stored the
app's API key following the authorization process.
"""
def slack_api_key(team_id):
    # Must specify region_name if it's not defined in ~/.aws/config
    aws_client = boto3.client('secretsmanager', region_name='us-east-2')
    response   = aws_client.get_secret_value(SecretId=f'integrations/slack/{team_id}')
    secrets    = json.loads(response['SecretString'])
    return secrets.get('app_api_key', "")
