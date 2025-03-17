#  Python with version

FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies

RUN apk add --no-cache \
    build-base \
    gcc \
    g++ \
    python3-dev \
    musl-dev \
    libffi-dev
    
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . . 

# Command to run on container start
CMD ["python", "app.py"]