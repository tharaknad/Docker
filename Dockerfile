#select the base-image of an conatiner
FROM ubuntu:latest


WORKDIR /application

COPY . /application

#Installing dependencies required for code Execution

RUN apt-get update && apt-get install -y python3 python3-pip

ENV NAME Caluclator

CMD ["python3" , "Scode.py"]
