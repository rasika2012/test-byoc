
# Use the official Python image as the base image
FROM python:3.9-slim-buster
USER 10050
# Set the working directory in the container
WORKDIR /app

# Copy the server file into the container
COPY test.py .

# Install the required packages
RUN pip install svgwrite

# Expose port 8000 for the server to listen on
EXPOSE 8000

# Start the server when the container is run
CMD ["python", "test.py"]