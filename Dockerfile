# Use a lightweight Python image
FROM python:3.10-slim

# Install ffmpeg + ImageMagick
RUN apt-get update && apt-get install -y ffmpeg imagemagick && rm -rf /var/lib/apt/lists/*

# Set working directory to root
WORKDIR /

# Copy all files
COPY . /

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your script
CMD ["python", "main.py"]
