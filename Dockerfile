FROM ubuntu

COPY ./app /app

WORKDIR app

RUN apt update; yes Yes | apt install python3-pip;

RUN /bin/bash -c "pip3 install -r requirements/requirements.txt;"

RUN /bin/bash -c "apt install ncat -y;"

RUN /bin/bash -c "apt install cron -y;"

RUN /bin/bash -c "apt install systemctl -y;"

RUN /bin/bash -c "echo 'echo * * * * * /app/reset_votes.sh >/dev/null 2>&1' crontab -"

RUN /bin/bash -c "chmod +x ./entrypoint.sh"
