# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir ollama gradio

# Expose the port Gradio uses (default is 7860)
EXPOSE 7860

# Run the application
CMD ["gradio", "chat.py"]
