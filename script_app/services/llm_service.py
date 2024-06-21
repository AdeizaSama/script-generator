# script_app/services/openai_service.py
import json
import logging
import anthropic
import os

from script_app.model.prompts import get_messaging_prompt, get_hooks_prompt

# Set up logger
logger = logging.getLogger(__name__)
logger.info(f"Claude API Key: {os.getenv('CLAUDE_API_KEY')}")
client = anthropic.Anthropic(api_key=os.getenv('CLAUDE_API_KEY'))


def make_llm_request(prompt, tools, max_tokens=1024):
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        messages=[{"role": "user", "content": prompt}],
        tools=tools if tools else None,
        temperature=1,
        max_tokens=max_tokens
    )

    response_content = response.content
    # if tools are used, return the tool_use_entry obj, if not return
    if tools:
        value = next((item for item in response_content if item.type == "tool_use"), None)
    else:
        value = next((item for item in response_content if item.type == "text"), None)

    if value is not None:
        logger.info(f"Response val: {value}")
        return value
    else:
        return None


def generate_messages(product, audience, problems, usps):
    prompt = get_messaging_prompt(product, audience, problems, usps)
    logger.info(f"Prompt: {prompt}")
    tools = [
        {
            "name": "generate_messages",
            "description": "Generate ten very compelling marketing messages to the target audience.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "messages": {
                        "type": "array",
                        "description": "list of generated marketing messages",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["messages"]
            }
        }
    ]

    completion = make_llm_request(prompt, tools)
    messages = completion['messages']
    return messages if messages else ["Failed to generate messages. Please try again."]

def generate_hooks(product_name, target_audience, narrator, core_message, additional_context):
    prompt = build_hooks_prompt(product_name, target_audience, narrator, core_message, additional_context)
    logger.info(f"Prompt: {prompt}")
    tools = [
        {
            "name": "generate_hooks",
            "description": "Generate five short hooks for for the start of an ad script.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "hooks": {
                        "type": "array",
                        "description": "list of generated ad hook options",
                        "items": {
                            "type": "string"
                        }
                    },
                },
                "required": ["hooks"]
            }
        }
    ]

    completion = make_llm_request(prompt, tools)
    hooks = completion['hooks']
    return hooks if hooks else ["Failed to generate hooks. Please try again."]
