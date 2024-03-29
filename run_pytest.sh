#!/bin/bash

# Set the directory where your tests are located
TEST_DIR="tests"

# Name of the virtual environment directory
VENV_DIR="venv"

# Path to requirements.txt
REQUIREMENTS_FILE="requirements.txt"

# Function to install pip if not installed
install_pip() {
    echo "Installing pip..."
    python3 -m ensurepip --upgrade --default-pip
}

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    install_pip
fi

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    # Create the virtual environment
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Check if requirements.txt exists and install dependencies
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "No requirements.txt found. Skipping dependencies installation."
fi

# Run pytest
echo "Running pytest for test cases in $TEST_DIR..."
pytest -m smoke $TEST_DIR

# Check if pytest ran successfully
if [ $? -eq 0 ]; then
    echo "Pytest finished successfully."
else
    echo "Pytest encountered errors."
fi

# Deactivate the virtual environment
deactivate