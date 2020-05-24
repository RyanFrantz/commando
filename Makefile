AWS_ECR_URL     := 127032180067.dkr.ecr.us-east-2.amazonaws.com
# If we're not being run via CircleCI, alias `docker` to address permissions
# related to contacting the daemon. In CircleCI, a remote Docker daemon is
# created for us and a set of envrionment variables that `docker` will see
# are created within the context of the user running the commands. `sudo`
# changes the context and those variables can't be seen.
ifndef CIRCLECI
DOCKER_CMD      := sudo docker
else
DOCKER_CMD      := docker
endif
DOCKER_IMAGE    := commando
# The ECR credential helper helps `docker` integrate with/use AWS credentials.
ECR_BREW_PKG    := docker-credential-helper-ecr
ECR_HELPER      := docker-credential-ecr-login
ECR_RELEASE_URL := https://amazon-ecr-credential-helper-releases.s3.us-east-2.amazonaws.com/0.3.1/linux-amd64/${ECR_HELPER}
# GIT_COMMIT_SHA is a standard flavor variable. We do this so that when calling
# `make deps` from inside a container, say, we don't get a confusing error that
# `git` can't be found.
GIT_COMMIT_SHA  = $(shell git rev-parse --short=12 HEAD)
THIS_OS         := $(shell uname -s)

# Generate ~/.aws/credentials
.PHONY: aws_creds
aws_creds:
ifndef CIRCLECI
	echo "soon"
else
	support/circleci/gen_aws_creds.sh
endif

PYTHON_REQS := $(shell tr '\n' '\|' < requirements.txt | sed -e 's/|$$//')
# Install dependencies.
.PHONY: deps
deps: venv
	@if bash -c "cmp -s <(python3 -m pip freeze | grep -E \"(${PYTHON_REQS})\" | sort) <(sort requirements.txt)"; then \
		echo "Python packages are installed!"; \
	else \
		python3 -m pip install --no-cache-dir -r requirements.txt > /dev/null; \
	fi

# Build a Docker image for this repo.
.PHONY: docker
docker: dockerdeps
	$(DOCKER_CMD) build . -t $(DOCKER_IMAGE):$(GIT_COMMIT_SHA) -t $(AWS_ECR_URL)/$(DOCKER_IMAGE):$(GIT_COMMIT_SHA)
	# TODO: Consider using a version tag for legibility, in the future.
	$(DOCKER_CMD) tag $(AWS_ECR_URL)/$(DOCKER_IMAGE):$(GIT_COMMIT_SHA) $(AWS_ECR_URL)/$(DOCKER_IMAGE):latest

.PHONY: docker_mac_deps
docker_mac_deps:
	@if ! which ${ECR_HELPER} > /dev/null; then \
		echo "Installing ${ECR_HELPER}..."; \
		brew install ${ECR_BREW_PKG}; \
		$(ECR_HELPER) -v; \
	fi

# "Linux" here means "Ubuntu".
.PHONY: docker_linux_deps
docker_linux_deps:
	@if ! which ${ECR_HELPER} > /dev/null; then \
		echo "Downloading ${ECR_HELPER}..."; \
		curl -s ${ECR_RELEASE_URL} -o /tmp/${ECR_HELPER}; \
		echo "Making it executable..."; \
		chmod 750 /tmp/${ECR_HELPER}; \
		echo "Moving it to /usr/local/bin..."; \
		sudo mv /tmp/${ECR_HELPER} /usr/local/bin/; \
		$(ECR_HELPER) -v; \
	fi

.PHONY: dockerdeps
dockerdeps:
ifeq (${THIS_OS},Darwin)
	@$(MAKE) docker_mac_deps
else
ifeq ($(THIS_OS),Linux)
	@$(MAKE) docker_linux_deps
endif
endif
	 @support/general/gen_docker_config.sh

# Publish a Docker image. On failure, output ecr-login logs for info.
.PHONY: push
push:
	$(DOCKER_CMD) push $(AWS_ECR_URL)/$(DOCKER_IMAGE):latest || (cat ~/.ecr/log/ecr-login.log; false)

.PHONY: serve
serve: venv
	@python3 server.py

# Run unit tests.
.PHONY: test
test: deps testdeps
	python3 -m pytest tests/

PYTHON_TEST_REQS := $(shell tr '\n' '\|' < test_requirements.txt | sed -e 's/|$$//')
.PHONY: testdeps
testdeps: venv
	@if bash -c "cmp -s <(python3 -m pip freeze | grep -E \"(${PYTHON_TEST_REQS})\" | sort) <(sort test_requirements.txt)"; then \
		echo "Python testing packages are installed!"; \
	else \
		python3 -m pip install --no-cache-dir -r test_requirements.txt > /dev/null; \
	fi

# Make sure we're running in a virtualenv.
# Test if we're already in one. If not, test that one is available and prompt
# us to activate it. We can't activate from here because doing so runs in a
# transient subshell..
# If there is no virtualenv, initialize the virtualenv.
# NOTE: If sys.prefix and sys.base_prefix are the same, we're not in a venv.
.PHONY: venv
venv:
	@if python3 -c 'import sys; sys.exit(1) if sys.prefix == sys.base_prefix else sys.exit(0)'; then \
		echo "We're in a virtualenv!"; \
	else \
		echo "Testing for existing venv..."; \
		if [ -f bin/activate ]; then \
			echo "Run 'source bin/activate' to activate the virtualenv."; \
			exit 1; \
		else \
			echo "Initializing a new virtualenv..."; \
			python3 -m venv .; \
			echo "Run 'source bin/activate' to activate the virtualenv."; \
			exit 1; \
		fi \
	fi
