#!/bin/bash

# Exit if any command fails
set -e

# Optional: customize commit message with timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
MESSAGE="update: $TIMESTAMP"

# Stage all changes
git add .

# Commit with a timestamped message
git commit -m "$MESSAGE"

# Push to GitHub
git push origin main

# Output success message
echo "✅ Deployed to abikesa.github.io/links at $TIMESTAMP"
