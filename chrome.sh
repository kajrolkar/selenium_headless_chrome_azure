#!/bin/bash
set -eu

apt update

echo "Update the repository and any packages..."

sudo apt update && sudo apt upgrade -y

sudo apt install wget curl unzip -y

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome-stable_current_amd64.deb

sudo apt --fix-broken install -y

echo $(google-chrome-stable --version)

curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable"'