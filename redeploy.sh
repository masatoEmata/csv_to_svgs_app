#!/bin/sh

echo "1. Setting environment variables..."
source ./environ.sh

echo "2. Setting project..."
gcloud config set project ${GCP_PJ_ID}

echo "3. Pushing the built Docker image to Google Cloud Container Registry..."
docker-compose push

echo "4. Stopping GCE instance..."
gcloud compute instances stop ${CONTAINER_NAME} --zone ${ZONE}

echo "5. Updating the instance with the new container image..."
gcloud compute instances update-container ${CONTAINER_NAME} \
    --container-image gcr.io/${GCP_PJ_ID}/${IMAGE_NAME}:latest \
    --zone ${ZONE}

echo "6. Starting GCE instance..."
gcloud compute instances start ${CONTAINER_NAME} --zone ${ZONE}

echo "Deployment complete."
