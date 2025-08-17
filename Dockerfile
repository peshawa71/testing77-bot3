# Use a lightweight Python image
FROM python:3.10-slim

# Install ffmpeg (needed by MoviePy)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory to root
WORKDIR /

# Copy everything into container
COPY . /

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py
CMD ["python", "main.py"]
