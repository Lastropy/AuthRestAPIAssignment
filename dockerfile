# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /src

# Copy the application code to the container
COPY . /src

# Install required dependencies
RUN pip install --no-cache-dir fastapi uvicorn[standard] passlib[bcrypt] python-jose

# Expose the port that the FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
