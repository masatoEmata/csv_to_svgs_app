#!/bin/sh

echo "Set environment variables"
export GCP_PJ_ID=$(gcloud config get-value project)
echo "GCP Project ID: $GCP_PJ_ID"
export IMAGE_NAME=csv-to-svgs-img
export CONTAINER_NAME=csv-to-svgs-cnt
export ZONE=asia-northeast1-a
export MACHINE=f1-micro
