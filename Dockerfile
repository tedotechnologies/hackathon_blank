FROM nvidia/cuda:12.0.1-devel-ubuntu22.04

RUN apt update
RUN apt install -y python3.10 python3-pip git

COPY --chown=1001:0 ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY src/ /app/src/
WORKDIR /app/src

EXPOSE 5000

CMD ["python3.10", "main.py"]
