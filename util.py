import bedrock_config


def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant", 
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages, system_prompt=""):
    request = {
        "modelId": bedrock_config.model_id,
        "messages": messages
    }
    if system_prompt:
        request["system"] = [{"text": system_prompt}]

    response = bedrock_config.client.converse(**request)
    return response["output"]["message"]["content"][0]["text"]