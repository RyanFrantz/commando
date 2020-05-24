#!/bin/bash

# gen_aws_creds.sh - Generate ~/.aws/credentials

# This script assumes it's being run by, and for, a circleci job. As such the
# envrionment variables referenced herein must be defined in the circleci
# project for which it's being run.

AWS_DIR=${HOME}/.aws
CONFIG_PATH=${AWS_DIR}/config
CREDS_PATH=${AWS_DIR}/credentials

mkdir -p $AWS_DIR

echo "Generating AWS config at ${CONFIG_PATH}..."
cat << EOCONFIG > $CONFIG_PATH
[default]
region = us-east-2
output = json
EOCONFIG

echo "Generating AWS credentials at ${CREDS_PATH}..."
cat << EOCREDS > $CREDS_PATH
[default]
aws_access_key_id=${CIRCLECI_AWS_ACCESS_KEY_ID}
aws_secret_access_key=${CIRCLECI_AWS_SECRET_ACCESS_KEY}
EOCREDS
