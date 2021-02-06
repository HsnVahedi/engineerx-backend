docker build ./engineerx/ -t engineerx/backend:latest
docker build .engineerx/dockerfiles/unittest/ -t engineerx/backend-unittest:latest
docker build ./nginx/ -t engineerx/backend-nginx:latest
docker build ./postgres/ -t engineerx/backend-postgres:latest