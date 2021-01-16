FROM node:15.2.1-alpine3.10

RUN apk update

WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .

RUN npm run build

ENV HOST 0.0.0.0
