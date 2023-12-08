#!/bin/sh
# Only for local development. No need to pass docker container.

# Project variables
export GCP_PJ_ID=XXX
gcloud config set project ${GCP_PJ_ID}
echo project id is: $(gcloud config get-value project)

export REGION=asia-northeast1
export ZONE=${REGION}-a
echo REGION is: ${REGION}
export MACHINE=g1-small

# Docker variables
export SERVICE=csv-to-svgs
export LOCAL_IMAGE=${SERVICE}-img
export LOCAL_CONTAINER=${SERVICE}-con
export DEPLOY_DMAIN=${REGION}-docker.pkg.dev
export DEPLOY_REPO=${SERVICE}-repo
export IMAGE=${DEPLOY_DMAIN}/${GCP_PJ_ID}/${DEPLOY_REPO}/${SERVICE}
