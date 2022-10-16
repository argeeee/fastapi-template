#!/usr/bin/bash

sudo openapi-generator-cli generate -i ../swagger/swagger.yaml -g typescript-node -o ../client
sudo chmod a+w -R ../client
