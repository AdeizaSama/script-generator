from django.shortcuts import render
from .forms import HookForm, ScriptForm
from .services.llm_service import generate_hooks
import logging

# Set up logger
logger = logging.getLogger(__name__)


def hook_creation_view(request):
    hook_form = HookForm()
    script_form = ScriptForm()
    hooks = []

    if 'generate_hook' in request.POST:
        hook_form = HookForm(request.POST)
        if hook_form.is_valid():
            product_name = hook_form.cleaned_data['product_name']
            target_audience = hook_form.cleaned_data['target_audience']
            narrator = hook_form.cleaned_data['narrator']
            core_message = hook_form.cleaned_data['core_message']
            additional_context = hook_form.cleaned_data['additional_creator_context']

            # Generate hooks
            hooks = generate_hooks(product_name, target_audience, narrator, core_message, additional_context)
            script_form = ScriptForm(hook_choices=[(hook, hook) for hook in hooks])

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