#!/bin/bash

echo "Installing Petoron Time Burn Cipher (PTBC) dependencies..."

# Step 1: Ensure Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install it manually and re-run this script."
    exit 1
fi

#Step 2: Install pip if missing
if ! command -v pip3 &> /dev/null
then
    echo "Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

# Step 3: Install argon2-cffi
echo "📦 Installing argon2-cffi..."
pip3 install --user argon2-cffi

echo "✅ Dependencies installed:))"
