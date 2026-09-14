# Automated Onboarding Tool

## Overview
A Python-based API integration script designed to automate zero-touch user provisioning, manage SaaS access, and enforce Mobile Device Management (MDM) policies for distributed teams.

## Architecture
*(Insert a link to a Draw.io or Excalidraw diagram here)*

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set your environment variables for directory access (e.g., `export DIRECTORY_API_KEY="your_token"`).
4. Execute the script: `python3 onboard.py`

## Security Considerations
* **Zero Trust:** API keys and sensitive tokens are strictly managed via environment variables and are never hardcoded into the application logic.
* **Least Privilege:** Service accounts executing this script are scoped exclusively to the required directory and MDM endpoints.
