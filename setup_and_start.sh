#!/bin/bash

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment"
        read -p "Press enter to continue..."
        exit 1
    fi
else
    echo "Virtual environment already exists"
fi

source ".venv/bin/activate"
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    read -p "Press enter to continue..."
    exit 1
fi

if [ -f "requirements.txt" ]; then
    echo "Installing packages..."
    pip install -r requirements.txt --quiet --no-warn-conflicts --disable-pip-version-check
    if [ $? -ne 0 ]; then
        echo "Failed to install packages from requirements.txt"
        read -p "Press enter to continue..."
        exit 1
    fi
else
    echo "No requirements.txt found - skipping package installation"
fi

echo "Ready! Virtual environment activated"


exec $SHELL