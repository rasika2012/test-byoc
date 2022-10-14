FROM node:18-alpine3.15

WORKDIR /app

COPY ./ /app/
RUN npm ci

USER 10050

ENTRYPOINT ["npm", "run", "start"]
