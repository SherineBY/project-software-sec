FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install dnslib
CMD ["python", "server.py"]
