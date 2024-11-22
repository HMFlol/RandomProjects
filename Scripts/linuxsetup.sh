#!/bin/bash

# Update package list and upgrade packages
echo "Updating package list and upgrading packages"
sudo apt update && apt upgrade -y

# Install htop and duf
echo "Installing htop"
sudo apt install -y htop

echo "Installing duf"
sudo apt install -y duf

echo "Setup completed!"