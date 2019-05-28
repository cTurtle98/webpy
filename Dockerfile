FROM alpine:latest
MAINTAINER "Ciaran admin@cturtle98.com"

RUN apt add --update python3 python3-pip
RUN pip3 install flask
COPY web.py /app/web.py
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["web.py"]
