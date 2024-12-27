#!/usr/bin/env bash

#!/bin/bash

# Set the Google Cloud project
PROJECT_ID="ogx-g-sheets-toc"
SERVICE_ACCOUNT_NAME="drive-api-service-account"
KEY_FILE_PATH="$HOME/.gcp/$SERVICE_ACCOUNT_NAME-key.json"

gcloud config set project $PROJECT_ID

# Authenticate with Google Cloud
gcloud auth login

# Create a service account
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
    --description="Service account for accessing Google Drive API" \
    --display-name=$SERVICE_ACCOUNT_NAME

# Assign roles to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/drive.file"

# Enable the required APIs
gcloud services enable drive.googleapis.com

# Generate and download the service account key
mkdir -p $(dirname $KEY_FILE_PATH)
gcloud iam service-accounts keys create $KEY_FILE_PATH \
    --iam-account="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

echo "Service account key saved to $KEY_FILE_PATH"

