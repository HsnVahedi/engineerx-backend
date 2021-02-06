# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.8.1-slim-buster

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet
RUN apt-get install --yes --quiet --no-install-recommends build-essential
RUN apt-get install --yes --quiet --no-install-recommends libpq-dev
RUN apt-get install --yes --quiet --no-install-recommends libmariadbclient-dev
RUN apt-get install --yes --quiet --no-install-recommends libjpeg62-turbo-dev
RUN apt-get install --yes --quiet --no-install-recommends zlib1g-dev
RUN apt-get install --yes --quiet --no-install-recommends libwebp-dev
RUN apt-get install --yes --quiet --no-install-recommends python3-opencv
RUN rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install opencv-python
RUN pip install opencv-python

# Install the project requirements.
RUN pip install "Django==3.1"
RUN pip install "wagtail==2.11"
RUN pip install psycopg2
RUN pip install Faker

# Use /app folder as a directory where the source code is stored.
WORKDIR /app
COPY  . .
RUN rm manage.py && mv manage.prod.py manage.py
RUN rm engineerx/wsgi.py && mv engineerx/wsgi.prod.py engineerx/wsgi.py

# Collect static files.
# CMD python manage.py collectstatic --noinput

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
# CMD set -xe; python manage.py migrate --noinput; gunicorn engineerx.wsgi:application
