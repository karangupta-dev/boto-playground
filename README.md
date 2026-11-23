# boto-playground

Small Python notebooks for trying Amazon Bedrock with boto3.

## What you need

- Python 3.10 or newer
- An AWS account
- AWS credentials on your computer
- Access to the Claude Haiku 4.5 model in AWS Region `us-east-2`

## Setup

From a PowerShell terminal in this project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name boto-playground
```

Add your AWS credentials. If the AWS CLI is installed:

```powershell
aws configure
```

Or set these environment variables in PowerShell:

```powershell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
$env:AWS_DEFAULT_REGION="us-east-2"
```

Do not put real credentials in this project or commit them to Git.

## Run

Start Jupyter:

```powershell
jupyter notebook
```

Open and run:

- `0_basic_api_request/api_request.ipynb` - sends one question to Bedrock
- `1_multi_turn_conversation/conversation.ipynb` - sends a short conversation

Choose the `boto-playground` Python kernel if Jupyter asks.

## Files

- `0_basic_api_request/api_request.ipynb` - basic Bedrock API example
- `1_multi_turn_conversation/conversation.ipynb` - multi-turn chat example
- `bedrock_config.py` - shared Bedrock client and model configuration
- `util.py` - simple message and chat helper functions
