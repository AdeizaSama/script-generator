# script_app/services/llm_service.py
import json
import logging
import anthropic
import os
from random import sample
from script_app.model.teachtap_core_inputs import AUDIENCE_INFO, PROBLEMS_INFO, USP_INFO, EXAMPLE_MESSAGES
from script_app.model.prompts import get_messaging_prompt, get_script_prompt

logger = logging.getLogger(__name__)
client = anthropic.Anthropic(api_key=os.getenv('CLAUDE_API_KEY'))


def get_prompt_inputs(product, audience, problems, usps):
    product_info = f"TeachTap is an educational mobile app that uses GenAI to bring historical characters back to life as the teachers, in the style of Tiktok. It is designed to help high school students get top grades in their upcoming exams by providing a fun, motivating and efficient way of learning."
    audience_info = AUDIENCE_INFO[audience]
    problems_info = "--" + "\n\n--".join([PROBLEMS_INFO[problem]['description'] for problem in problems]) if problems else "N/A"
    usp_info = "--" + "\n\n--".join([USP_INFO[usp]['description'] for usp in usps]) if usps else "N/A"
    example_messages = "--" + "\n\n--".join(
        [message['description'] for message in sample(
            [msg for msg in EXAMPLE_MESSAGES if msg['target_audience'] == audience], 3
        )]
    )
    return product_info, audience_info, problems_info, usp_info, example_messages


def make_llm_request(prompt, tools, max_tokens=1024):
    logger.info(f"Prompt:\n{prompt}")
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


def generate_messages_service(product, audience, problems, usps, additional_context):
    product_info, audience_info, problems_info, usp_info, example_messages = get_prompt_inputs(product, audience, problems, usps)
    prompt = get_messaging_prompt(product_info, audience_info, problems_info, usp_info, additional_context, example_messages)
    # logger.info(f"Prompt: {prompt}")
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
    messages = completion.input['messages']
    return messages if messages else ["Failed to generate messages. Please try again."]


def generate_script_service(selected_messages, audience, script_length, call_to_action, additional_context):
    tools = [
        {
            "name": "generate_script",
            "description": "Generate a script for an ad.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": "generated ad script"
                    }
                },
                "required": ["script"]
            }
        }
    ]

    prompt = get_script_prompt(selected_messages, audience, script_length, call_to_action, additional_context)
    completion = make_llm_request(prompt, tools)
    script = completion.input['script']
    if script:
        return script, prompt
    else:
        return "Failed to generate script. Please try again.", prompt


def refine_script_service(chat_history, message):
    tools = [
        {
            "name": "generate_script",
            "description": "Generate a script for an ad.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": "The fully generated ad script with concept and scene descriptions"
                    }
                },
                "required": ["script"]
            }
        }
    ]
    chat_history.append({"role": "user", "content": message})
    prompt = json.dumps(chat_history)
    completion = make_llm_request(prompt, tools)
    script = completion.input['script']
    return script if script else "Failed to generate chat response. Please try again."
