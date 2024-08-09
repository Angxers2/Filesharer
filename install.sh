#!/bin/bash

# Function to show animation
show_animation() {
    local pid=$!
    local spin='-\|/'
    echo -n 'Installing dependencies '
    while kill -0 $pid 2>/dev/null; do
        local temp=${spin#?}
        printf "%c\b" "$spin"
        spin=$temp${spin%"$temp"}
        sleep 0.1
    done
    printf " Done!\n"
}

# Update and install dependencies
echo "Updating package lists..."
sudo apt-get update -y > /dev/null 2>&1

echo "Installing Python3 and pip..."
{
    sudo apt-get install -y python3 python3-pip > /dev/null 2>&1
} & show_animation

# Install required Python packages
echo "Installing Python packages..."
{
    pip3 install paramiko ftplib > /dev/null 2>&1
} & show_animation

# Confirm installation
echo "Installation completed successfully."

