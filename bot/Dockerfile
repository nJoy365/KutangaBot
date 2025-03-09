# Use Python 3.10
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot files
COPY . .

# Set environment variables from .env
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "bot.py"]
