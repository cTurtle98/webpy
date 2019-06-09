FROM alpine:latest
MAINTAINER "Ciaran admin@cturtle98.com"

#RUN apk update &&\
# apk upgrade

RUN apk add python3 py-pip

RUN pip3 install flask

COPY web.py /app/web.py

WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["web.py"]
