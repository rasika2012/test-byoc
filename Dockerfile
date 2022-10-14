FROM node:18-alpine3.15

USER 10050

RUN npm i -g express

ENTRYPOINT ["node", "server.js"]
