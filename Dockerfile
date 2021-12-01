FROM ubuntu:20.04

ENV TZ=Europe/Brussels

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

RUN apt-get -y install python3 python3-pip python3-tk python3-markupsafe ghostscript pdf2svg

COPY requirements.txt /l-systems/

WORKDIR /l-systems

RUN cat requirements.txt

RUN pip install -r requirements.txt

COPY . /l-systems

CMD ["chmod", "666", "/*"]

#CMD [ "/usr/bin/python3", "lSystem.py" ]

ENTRYPOINT ["python3", "lSystem.py"]
