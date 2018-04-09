#!/bin/bash
# This installs the hello.go package locally after updates

# Install the local package to the $GOBIN/hello target
go install hello

# Link the new source file to the /usr/bin
# sudo ln /home/ubuntu/Git/DevSkills/golang/bin/hello /usr/bin/hello  -f

# local snap build+refresh
snapcraft
# sudo snap remove hello
sudo snap install hello_*_amd64.snap --devmode --dangerous
