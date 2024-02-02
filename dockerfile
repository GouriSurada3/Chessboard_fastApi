# Use the official Python 3.9 image as the base image
FROM python:3.9

# Copy the requirements file to the root of the container
COPY ./requirement.txt /requirement.txt

# Install Python dependencies based on the requirements file
RUN pip install -r /requirement.txt

# Copy the entire local project directory to the root of the container
COPY . .

# Expose port 8000 to allow external connections
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
