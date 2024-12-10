#!/usr/bin/env bash
set -e

PROJECT_MAIN_DIR_NAME="djangoAWS"

# Validate variables
if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
    echo "Error: PROJECT_MAIN_DIR_NAME is not set. Please set it to your project directory name." >&2
    exit 1
fi

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Create virtual environment
echo "Creating virtual environment..."
virtualenv "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv"

# Activate virtual environment
echo "Activating virtual environment..."
source "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv/bin/activate"
sudo chmod -R 755 /home/ubuntu/djangoAWS/

# Install dependencies
echo "Installing Python dependencies..."
pip install -r "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/requirements.txt"
pip install django-crispy-forms
pip install whitenoise
python3 -m pip install Pillow
sudo apt install sqlite3

echo "Dependencies installed successfully."
