#!/usr/bin/bash

sudo openapi-generator-cli generate -i ../swagger/swagger.yaml -g python-fastapi -o ../server
sudo chmod a+w -R ../server