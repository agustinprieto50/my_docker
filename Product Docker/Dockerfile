FROM python:3

RUN git clone https://github.com/agustinprieto50/my_docker.git
RUN pip3 install parameterized

WORKDIR /my_docker/product

CMD ["python3", "-m", "unittest"]
