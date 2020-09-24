FROM ubuntu:18.04
LABEL name        "commando"
LABEL maintainer  "Ryan Frantz"
LABEL description "A container from which to run Commando Slack App."
LABEL summary     "Run Commando Slack App."
LABEL release     ""
LABEL version     ""
LABEL vendor      "Ryan Frantz"
RUN groupadd -r commando && useradd -d /home/commando -m -r -g commando commando
# Automatically creates the directory.
WORKDIR /commando
# Copy these files separately so we can install deps in a separate layer
# for fast builds. In the future, we might want to use multistage builds.
COPY Makefile dev-packages.txt packages.txt requirements.txt test_requirements.txt /commando/
# Install a number of system packages, read from a file.
# '--no-install-recommends' prevents ~400MB of bloat.
RUN apt-get update && \
 apt-get install --no-install-recommends -y \
 $(grep -vE "^\s*#" packages.txt  | tr "\n" " ") \
 $(grep -vE "^\s*#" dev-packages.txt  | tr "\n" " ") && \
 apt-get clean && \
 curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscliv2.zip && \
 unzip /tmp/awscliv2.zip -d /tmp && \
 /tmp/aws/install && \
 rm -rf /tmp/aws*
# Create our virtualenv and ensure we use it.
# NOTE: We can't use the activate convenience because each RUN statement is
# a separate process.
ENV VIRTUAL_ENV=/commando
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH
# Install dependencies and clean up packages used for the build process.
RUN make deps && \
 apt-get purge -y $(grep -vE "(^\s*#)" dev-packages.txt  | tr "\n" " ") && \
 apt-get clean && \
 rm -f Makefile dev-packages.txt packages.txt requirements.txt test_requirements.txt
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
