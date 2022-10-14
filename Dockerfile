FROM node:18-alpine3.15

RUN npm i -g express

USER 10050

COPY server.js server.js

ENTRYPOINT ["node", "./server.js"]
