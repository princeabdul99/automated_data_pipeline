FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .       
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m", "etl_ingestion.main" ]



# <!-- CREATING DOCKER FILE FOR PYTHON IMAGE -->
# FROM: This specifies the base image to use for the Docker image.

# RUN: This runs a command inside the Docker container during the build process

# COPY: This copies file from the local file system to the Docker image.

# WORKDIR: This sets the working directory for subsequent commands in the Dockerfile.

# CMD: This specifies the command to run when the Docker container starts.

