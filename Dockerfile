# Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY main.py .
COPY content .
COPY css .
COPY images .
COPY template.html .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
