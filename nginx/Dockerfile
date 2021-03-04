ARG INTEGRATION 
FROM nginx:1.18.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN if [[ -z "$INTEGRATION" ]] ; then mv nginx.production.conf nginx.conf ; else mv nginx.integration.conf nginx.conf ; fi

COPY nginx.conf /etc/nginx/conf.d