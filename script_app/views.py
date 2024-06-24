from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm, ScriptForm
from .services.llm_service import generate_messages_service, generate_script_service
import json
import logging

# Set up logger
logger = logging.getLogger(__name__)


def script_generator_view(request):
    message_form = MessageForm()
    script_form = ScriptForm()
    messages = []
    script = ""

    return render(request, 'script_app/form.html', {
        'message_form': message_form,
        'script_form': script_form,
        'messages': messages,
        'script': script
    })


def generate_messages_view(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            product = message_form.cleaned_data['product']
            audience = message_form.cleaned_data['audience']
            problems = message_form.cleaned_data['problem']
            usps = message_form.cleaned_data['usp']
            additional_context = message_form.cleaned_data['additional_context']

            # Generate messages
            messages = generate_messages_service(product, audience, problems, usps, additional_context)
            return JsonResponse({"messages": messages})
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def generate_script_view(request):
    if request.method == "POST":
        script_form = ScriptForm(request.POST)
        if script_form.is_valid():
            script_length = script_form.cleaned_data['script_length']
            call_to_action = script_form.cleaned_data['call_to_action']
            additional_context = script_form.cleaned_data['additional_context']

            selected_messages = json.loads(request.POST.get('selected_messages', '[]'))
            audience = request.POST.get('audience', '')

            script = generate_script_service(selected_messages, audience, script_length, call_to_action, additional_context)
            return JsonResponse({"script": script})
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)

    return JsonResponse({"error":"Invalid request method"}, status=405)

