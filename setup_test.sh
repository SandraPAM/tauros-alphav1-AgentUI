#!/bin/bash

# 1. Set the Agent Name (Default: my_agent)
# If $1 is empty, use "my_agent"
AGENT_NAME=${1:-my_agent}

# 2. Set Additional Packages (Optional)
# Captures the second argument if provided
EXTRA_PACKAGES=$2

echo "Creating environment for: $AGENT_NAME..."

# 3. Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Install Dependencies
pip3 install google-adk
if [ -n "$EXTRA_PACKAGES" ]; then
    echo "Installing additional packages: $EXTRA_PACKAGES"
    pip3 install $EXTRA_PACKAGES
fi

# 5. Create the Agent
adk create "$AGENT_NAME"

echo "Setup complete! Remember to run 'source .venv/bin/activate' to enter the environment."
