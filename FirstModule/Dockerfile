# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.10-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container

COPY ./FirstModule ./FirstModule
COPY ./SharedUtils ./SharedUtils

ENV PYTHONPATH "${PYTHONPATH}:/app"
# ENTRYPOINT ["python", "hb2Stripes/main.py"]

