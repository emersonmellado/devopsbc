#!/bin/bash

echo "Downloading Jenkins Key and adding it to apt-key"
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -

echo "======================================="
echo "Adding Jenkins repository to apt sources"
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

echo "Adding packages to local keyserver"
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xFCEF32E745F2C3D5

echo "Updating all packages available"
sudo apt-get update

echo "Installing jenkins"
sudo apt-get install jenkins
