from django.shortcuts import render
from .forms import ScriptForm, MessageForm
from .services.llm_service import generate_messages
import logging

# Set up logger
logger = logging.getLogger(__name__)


def message_creation_view(request):
    message_form = MessageForm()
    script_form = ScriptForm()
    messages = []

    if 'generate_message' in request.POST:
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            product = message_form.cleaned_data['product']
            audience = message_form.cleaned_data['audience']
            problems = message_form.cleaned_data['problem']
            usps = message_form.cleaned_data['usp']

            # Generate messages
            messages = generate_messages(product, audience, problems, usps)
            script_form = ScriptForm(message_choices=[(message, message) for message in messages])

    elif 'generate_script' in request.POST:
        script_form = ScriptForm(request.POST)
        if script_form.is_valid():
            # Here, we would normally generate the script based on form input.
            # For now, just return a placeholder script.
            logger.info(f"Script form data: {script_form.cleaned_data}")
            script_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
            return render(request, 'script_app/form.html', {
                'message_form': message_form,
                'script_form': script_form,
                'messages': messages,
                'script_text': script_text,
            })

    return render(request, 'script_app/form.html', {
        'message_form': message_form,
        'script_form': script_form,
        'messages': messages,
        'script_text': '',
    })
