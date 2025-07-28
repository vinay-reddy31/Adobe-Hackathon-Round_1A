# 1. Use a lightweight official Python image with AMD64 CPU
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all files from your local folder into the container
COPY . .

# 4. Install all Python dependencies (from requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run your script automatically when the container starts
CMD ["python", "main.py"]
