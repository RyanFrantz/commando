#!/bin/bash

function deploy() {
curl \
  -F "channel_id=DREAMBIG" \
  -F 'token=So12345678asdfghjk' \
  -F 'team_id=TEAMJELI1' \
  -F 'team_domain=jelitalk' \
  -F 'channel_id=DREAMBIG' \
  -F 'channel_name=directmessage' \
  -F 'user_id=UFGUTHD2M' \
  -F 'user_name=ryan' \
  -F 'command=%2Fcommando' \
  -F 'text=deploy' \
  -F 'response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKVN58V5K%2F1125858804757%2FrFWbh7OK8JYOkzP9QycvKWsZ' \
  -F 'trigger_id=1139860966177.675753301189.41b8edc5999f487c4b3ddbdc1b69ee52' \
  localhost:5000/run
}

function fail() {
curl \
  -F "channel_id=DREAMBIG" \
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

#deploy
fail
