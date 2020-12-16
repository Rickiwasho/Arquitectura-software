FROM python:latest
RUN git clone https://github.com/Rickiwasho/arquitectura-software.git \
    && pip install slack_sdk

WORKDIR /arquitectura-software/actividades/atreidesbot-slack/

CMD python3 atreidesbot.py \
    && python3 atreidesbot_test.py
