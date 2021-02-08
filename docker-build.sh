docker build engineerx/ -t hsndocker/backend:latest
docker build engineerx/dockerfiles/unittest/ -t hsndocker/backend-unittest:latest
docker build nginx/ -t hsndocker/backend-nginx:latest
docker build postgres/ -t hsndocker/backend-postgres:latest
