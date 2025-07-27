# --- Base Image ---
FROM python:3.10-slim

# --- Set Working Directory ---
WORKDIR /app

# --- Install System Dependencies ---
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# --- Copy Dependency Files ---
COPY requirements.txt .

# --- Install Python Dependencies ---
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy Application Code ---
COPY . .

# --- Expose Port ---
EXPOSE 8000

# --- Set Environment Variables ---
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# --- Default Command ---
CMD ["bash"]