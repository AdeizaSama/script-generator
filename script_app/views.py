from django.shortcuts import render
from .forms import HookForm, ScriptForm
import logging

# Set up logger
logger = logging.getLogger(__name__)


def hook_creation_view(request):
    hook_form = HookForm()
    script_form = ScriptForm()
    hooks = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']  # Placeholder hooks

    if request.method == 'POST':
        if 'generate_hook' in request.POST:
            hook_form = HookForm(request.POST)
            if hook_form.is_valid():
                # Here, we would normally generate the hooks based on form input.
                # For now, just log the input and use placeholder hooks.
                logger.info(f"Hook form data: {hook_form.cleaned_data}")
                hooks = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']  # Placeholder hooks

        elif 'generate_script' in request.POST:
            script_form = ScriptForm(request.POST)
            if script_form.is_valid():
                # Here, we would normally generate the script based on form input.
                # For now, just return a placeholder script.
                logger.info(f"Script form data: {script_form.cleaned_data}")
                script_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                return render(request, 'script_app/form.html', {
                    'hook_form': hook_form,
                    'script_form': script_form,
                    'hooks': hooks,
                    'script_text': script_text,
                })

    return render(request, 'script_app/form.html', {
        'hook_form': hook_form,
        'script_form': script_form,
        'hooks': hooks,
        'script_text': '',
    })