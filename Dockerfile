# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy necessary files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project except what's ignored in .dockerignore
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Set environment variable so Streamlit doesn't prompt for input
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
