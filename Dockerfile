FROM python:3.11

# Install Flask and other dependencies
RUN pip install flask flask_cors

# Copy the app code to the container
COPY . /app
WORKDIR /app

# Expose the app's port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
