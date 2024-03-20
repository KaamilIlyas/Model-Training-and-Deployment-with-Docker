# Base image with Python
FROM python:3.8

# Create a working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install required libraries
RUN pip install -r requirements.txt

# Copy the dataset and training script
COPY bank.csv .
COPY train.py .

# Copy the trained model file
COPY model.pkl ./app/model.pkl

# Entrypoint command to run the script
ENTRYPOINT ["python", "train.py"]
