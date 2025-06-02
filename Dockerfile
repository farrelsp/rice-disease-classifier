# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install aws cli
RUN pip install awscli --upgrade --user

# Install packages in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "Prediction.py", "--server.port=8501", "--server.address=0.0.0.0"]
