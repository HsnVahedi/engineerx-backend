# Install node for cypress
ARG BACKEND_IMAGE=hsndocker/backend:latest
FROM $BACKEND_IMAGE

WORKDIR /integration

COPY package*.json /integration/
RUN npm install
COPY  . .