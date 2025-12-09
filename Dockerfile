# STEP 1: Pull a lightweight, stable Python base image
FROM python:3.11-slim

# STEP 2: Set the working directory inside the container
WORKDIR /app

# STEP 3: Copy dependency definition file first (for layer caching)
COPY requirements.txt .

# STEP 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Copy application source code and test script
COPY app.py .
COPY test_app.py .

# STEP 6: Expose the Flask application port
EXPOSE 5000

# STEP 7: Run the Flask application
CMD ["python", "app.py"]
