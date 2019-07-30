#  This is API docker file that is used to connect
#  the Swagger/Flask API to Gunicorn, via Supervisord.
#  Web3.py is then used to interact with the contracts
#  (written and tested in truffle)

FROM python:3.6

RUN  apt-get update -y && \
     apt-get upgrade -y

# API
RUN mkdir -p /usr/src/package
COPY ./package /usr/src/package
WORKDIR /usr/src/package
RUN pip install -e .

# Deployment
RUN apt-get install supervisor -y
RUN pip install gunicorn

# Supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start processes
CMD ["/usr/bin/supervisord"]