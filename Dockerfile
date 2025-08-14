# Use an official lightweight Linux image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your script or files here (optional)
# COPY . /app

# Default command to show ffmpeg version (you can override this)
CMD ["ffmpeg", "-version"]
