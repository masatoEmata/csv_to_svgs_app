#!/bin/sh

echo "Set environment variables"
source ./environ.sh

echo "Authenticate with Google Cloud SDK"
gcloud auth login
gcloud config set project ${GCP_PJ_ID}

echo "Configure Docker to use Google Cloud Container Registry"
gcloud auth configure-docker

echo "Push the built Docker image to Google Cloud Container Registry"
docker-compose push

echo "Create a GCE instance with the container"
gcloud compute instances create-with-container ${CONTAINER_NAME} \
    --container-image gcr.io/${GCP_PJ_ID}/${IMAGE_NAME}:latest \
    --zone ${ZONE} \
    --machine-type ${MACHINE}

echo "Open port 8000 on the GCE instance"
gcloud compute firewall-rules create allow-web-8000-csv-to-svgs \
    --allow tcp:8000 \
    --source-ranges 0.0.0.0/0 \
    --target-tags=${CONTAINER_NAME}

gcloud compute firewall-rules update allow-web-8000-csv-to-svgs \
    --allow tcp:8000 \
    --source-ranges 0.0.0.0/0 \
    --target-tags=${CONTAINER_NAME}
