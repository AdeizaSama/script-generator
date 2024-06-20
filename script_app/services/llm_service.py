# script_app/services/openai_service.py
import json
import logging
import anthropic
import os

# Set up logger
logger = logging.getLogger(__name__)
logger.info(f"Claude API Key: {os.getenv('CLAUDE_API_KEY')}")
client = anthropic.Anthropic(api_key=os.getenv('CLAUDE_API_KEY'))


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

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
        temperature=1,
        max_tokens=1024
    )

    response_content = response.content
    tool_use_entry = next((item for item in response_content if item.type == "tool_use"), None)
    if tool_use_entry is not None:
        logger.info(f"Tool Response: {tool_use_entry}")
        hooks = tool_use_entry.input['hooks']

        if hooks:
            return hooks
        else:
            return ["Failed to generate hooks. Please try again."]
    else:
        return ["Failed to generate hooks. Please try again."]


def build_hooks_prompt(product_name, target_audience, narrator, core_message, additional_context):
    product_details = "TeachTap is an educational mobile app that uses GenAI to bring historical characters back to " \
                      "life as the teachers, in the style of Tiktok. It is designed to help high school students get " \
                      "top grades in their upcoming exams by providing a fun, motivating and efficient way of learning."
    example_core_message = "High SAT scores open doors to elite universities: Without them, gaining admission to your " \
                           "dream school may be out of reach. A high SAT score gives you the competitive edge needed " \
                           "to succeed in today's highly selective admissions process."
    example_hook = "Top universities care about SAT scores. But is your child ready?"

    return f"""
    Context
    ---------
    You are an ad script writer for an educational technology company that makes apps. The product you are advertising is called {product_name}. Description of the app: {product_details}

    Task
    ---------
    1. Understand the Context, Task, Rules, Examples, and Core Inputs.
    2. Generate five captivating Hooks for the start of the ad, relative to the Core Inputs, which should captivate the Target Audience’s attention in the first few words.

    Rules
    ---------
    1. The hook must be one or two sentences long and a maximum of 10 words
    2. The first five words must trigger curiosity in the target audience, making them want to watch the next part of the ad.
    3. The hook must be funny, interesting, or hyperbolic.
    4. The hook must be relevant to the core message.

    Core Inputs
    ---------
    Target Audience: {target_audience}
    AI Figure/Narrator: {narrator}
    Core Message: {core_message}
    Additional Context from Creator: {additional_context}

    Example(s)
    ---------
    ```
    Core Message: {example_core_message}
    Hook: {example_hook}
    ```
    """
