#!/bin/bash
# This installs the hello.go package locally after updates

# Move to directory of project (safety)
cd /home/ubuntu/Git/DevSkills/golang/src/hello

# remove previous snap build
rm parts/ prime/ snap stage/ -rf

# Install the local package to the $GOBIN/hello target
go install hello

# local snap build
snapcraft

# install new snap locally
sudo snap install hello_*_amd64.snap --devmode --dangerous

# Link static bin to /usr/bin
# sudo ln /home/ubuntu/Git/DevSkills/golang/bin/hello /usr/bin/hello  -f
