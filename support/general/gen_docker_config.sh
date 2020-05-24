#!/bin/bash

# gen_docker_config.sh - Generate ~/.docker/config.json

# If no Docker config exists, add a generic config that specifies support
# for using ecr-login.

DOCKER_DIR=${HOME}/.docker
CONFIG_PATH=${DOCKER_DIR}/config.json

gen_docker_config() {
  echo "Generating Docker configuration at ${CONFIG_PATH}..."
  mkdir -p $DOCKER_DIR
  cat << EOF > $CONFIG_PATH
{
    "credsStore": "ecr-login",
    "credHelpers": {
        "127032180067.dkr.ecr.us-east-2.amazonaws.com": "ecr-login"
    }
}
EOF
}

test -f $CONFIG_PATH || gen_docker_config
