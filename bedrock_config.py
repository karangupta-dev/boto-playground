import boto3

region = "us-east-2"
model_id = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
client = boto3.client("bedrock-runtime", region_name=region)
