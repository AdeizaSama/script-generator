from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm
from .services.llm_service import generate_messages_service
import logging

# Set up logger
logger = logging.getLogger(__name__)


def message_creation_view(request):
    message_form = MessageForm()
    messages = []

    return render(request, 'script_app/form.html', {
        'message_form': message_form,
        'messages': messages,
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
