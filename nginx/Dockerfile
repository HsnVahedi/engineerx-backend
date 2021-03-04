ARG CONF_FILE=nginx.production.conf
FROM nginx:1.18.0-alpine

COPY $CONF_FILE /etc/nginx/conf.d
RUN if [ "$CONF_FILE" = "nginx.production.conf" ]; then \
        mv /etc/nginx/conf.d/nginx.production.conf /etc/nginx/conf.d/nginx.conf; \
    else \
        mv /etc/nginx/conf.d/nginx.integration.conf /etc/nginx/conf.d/nginx.conf; \
    fi