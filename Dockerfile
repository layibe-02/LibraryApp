# Utilisez une image de base avec Python
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install python3 gcc libc-dev -y

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install psycopg2 

RUN mkdir /libraryproject

# Définissez le répertoire de travail
WORKDIR /libraryproject

COPY ./libraryproject /libraryproject

# Exposez le port sur lequel votre application écoute
EXPOSE 8001

COPY ./libraryproject/start.sh  .
RUN sed -i 's/\r$//g' /libraryproject/start.sh
RUN chmod +x /libraryproject/start.sh

ENTRYPOINT [ "/libraryproject/start.sh" ]
# Commande pour démarrer l'application
