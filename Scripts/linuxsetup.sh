#!/bin/bash

# Update package list and upgrade packages
echo "Updating package list and upgrading packages"
apt update && apt upgrade -y

# Install htop and duf
echo "Installing htop"
apt install -y htop

echo "Installing duf"
apt install -y duf

echo "Setup completed!"