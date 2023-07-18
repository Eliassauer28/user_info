FROM python:3.9-slim

# Copy requirements file and install requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Copy the entire project directory (including setup.py and src/)
COPY . /app/

# Change to the app directory
WORKDIR /app

# Install the application in editable mode
RUN pip install -e .

# Set PYTHONPATH
ENV PYTHONPATH=/app:$PYTHONPATH

# Change the working directory to /app/src
WORKDIR /app
