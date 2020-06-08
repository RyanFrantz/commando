#!/bin/bash

function deploy() {
curl \
  -F 'channel_id=DKJA3CVU3' \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=deploy' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function deploy_webapp() {
curl \
  -F 'channel_id=DKJA3CVU3' \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=deploy webapp' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function missing_cmd() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function help() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=help' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function list() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=list' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function command_not_found() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=not_a_valid_command' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function run_python_example() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=python-example' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function whoami() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=whoami' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function weather() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=weather' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

# Because `time` is a shell builtin.
function call_time() {
curl \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TKVN58V5K' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DKJA3CVU3' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UKXHG8T5M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=time' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

#deploy
#deploy
#deploy_webapp
#missing_cmd
#help
#command_not_found
#list
#run_python_example
#whoami
#weather
call_time
