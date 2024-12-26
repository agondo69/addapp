# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required Python dependencies
RUN pip install flask

# Expose port 5000 for Flask
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]
