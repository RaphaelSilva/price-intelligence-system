FROM mcr.microsoft.com/playwright/python:v1.46.0-noble
WORKDIR /app

COPY package.json .

RUN npm install

ENTRYPOINT [ "./entrypoint.sh" ]