#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Navigate to the client directory
cd client

# Install dependencies
echo "Installing dependencies..."
npm ci

# Build the project
npm run build

# Navigate up one directory
cd ../

# Navigate to the server directory
cd server

# Export Flask app environment variable
export FLASK_APP=app.py

# Run the Flask application
echo "Running the Flask application..."
flask run --host=0.0.0.0 --port=5000

echo "Flask application is running!"
