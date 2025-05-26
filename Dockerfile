# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source
COPY ./src ./src

# Change to source directory
WORKDIR /app/src

# Command to run the script
CMD ["python", "hello.py"]

