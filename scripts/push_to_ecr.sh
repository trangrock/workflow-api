#!/bin/env bash

# REPO=workflow-api

# eval $(aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin https://${AWS_ACCOUNT_NUMBER}.dkr.ecr.eu-west-1.amazonaws.com)
# docker build -t $REPO:$VERSION -f Dockerfile .
# docker tag $REPO:$VERSION $AWS_ACCOUNT_NUMBER.dkr.ecr.eu-west-1.amazonaws.com/$REPO:$VERSION;
# docker tag $REPO:$VERSION $AWS_ACCOUNT_NUMBER.dkr.ecr.eu-west-1.amazonaws.com/$REPO:latest;
# docker push $AWS_ACCOUNT_NUMBER.dkr.ecr.eu-west-1.amazonaws.com/$REPO:$VERSION;
# docker push $AWS_ACCOUNT_NUMBER.dkr.ecr.eu-west-1.amazonaws.com/$REPO:latest;
