ARG CONF_FILE=nginx.production.conf
FROM nginx:1.18.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN mv $CONF_FILE nginx.conf
COPY nginx.conf /etc/nginx/conf.d