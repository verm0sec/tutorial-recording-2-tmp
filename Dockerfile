# Use an official Python runtime as a parent image. We'll use the slim-buster version
# which is a smaller version of Debian Linux with Python pre-installed.
FROM python:3.9-slim-buster

# Set the working directory in the container to /app. This is where our application
# code will reside.
WORKDIR /app

# Copy the entire application directory (including app.py) from the host machine
# to the /app directory in the container.
COPY . .

# Set an environment variable named APP_ENV and set its value to 'production'.
ENV APP_ENV=production

# Make the app.py script executable.
RUN chmod +x app.py

# Define the command to run when the container starts.
CMD ["python", "app.py"]
