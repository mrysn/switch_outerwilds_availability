FROM python:3

ADD switch_outerwilds.py /
ADD pip_requirements.txt /
ADD .secret.server /
ADD .secret.from /
ADD .secret.to /
ADD .secret.pass /

RUN pip install -r pip_requirements.txt

CMD ["python","./switch_outerwilds.py"]