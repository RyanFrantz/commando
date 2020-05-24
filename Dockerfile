FROM ubuntu:18.04
LABEL name        "commando"
LABEL maintainer  "Jeli, Inc."
LABEL description "A container from which to run Jeli's Commando Slack App."
LABEL summary     "Run Jeli's Commando Slack App."
LABEL release     ""
LABEL version     ""
LABEL vendor      "Jeli, Inc."
RUN groupadd -r commando && useradd -d /home/commando -m -r -g commando commando
# Automatically creates the directory.
WORKDIR /commando
# Copy these files separately so we can install deps in a separate layer
# for fast builds. In the future, we might want to use multistage builds.
COPY Makefile packages.txt requirements.txt /commando/
# Install a number of system packages, read from a file.
# '--no-install-recommends' prevents ~400MB of bloat.
RUN apt-get update && \
 apt-get install --no-install-recommends -y $(grep -vE "^\s*#" packages.txt  | tr "\n" " ") && \
 apt-get clean
# Install dependencies and clean up packages used for the build process.
RUN DOCKER_IS_BUILDING=true make deps && \
 apt-get purge -y $(grep -vE "(^\s*#|^python3$)" packages.txt  | tr "\n" " ") && \
 apt-get clean && \
 rm -f Makefile packages.txt requirements.txt
# Copy only what's necessary for production (i.e. no tests).
COPY commando/ /commando/commando/
COPY routes/ /commando/routes/
COPY server.py /commando/
RUN chown -R commando:commando /commando
USER commando
# Set the LANG value else flask throws an error (it's not set in the container).
# See https://click.palletsprojects.com/en/7.x/python3/#python-3-surrogate-handling
ENV LANG en_US.utf8
ENTRYPOINT ["python3", "server.py"]
