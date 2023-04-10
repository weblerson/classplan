FROM node:18-alpine

RUN mkdir /app
WORKDIR /app

COPY package*.json .
RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080