FROM node:16-alpine

RUN mkdir -p /usr/app/ && chown -R node:node /usr/app
WORKDIR /usr/app/
COPY --chown=node:node . .

USER node


RUN npm install


RUN npm run build


EXPOSE 3000
CMD ["npm", "run", "dev"]