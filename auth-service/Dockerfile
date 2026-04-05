FROM node:18

WORKDIR /app

COPY index.js .

RUN npm init -y && npm install express

CMD ["node", "index.js"]