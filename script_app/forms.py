from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .model.teachtap_core_inputs import PROBLEMS_INFO, USP_INFO


class MessageForm(forms.Form):
    PRODUCT_CHOICES = [
        ('TeachTap', 'TeachTap'),
    ]
    AUDIENCE_CHOICES = [
        ('Parents', 'Parents'),
        ('Students', 'Students')
    ]
    PROBLEMS_CHOICES = [(key, value['title']) for key, value in PROBLEMS_INFO.items()]
    USP_CHOICES = [(key, value['title']) for key, value in USP_INFO.items()]

    product = forms.ChoiceField(choices=PRODUCT_CHOICES, label='Product')
    audience = forms.ChoiceField(choices=AUDIENCE_CHOICES, label='Audience')
    problem = forms.MultipleChoiceField(
        choices=PROBLEMS_CHOICES,
        label='Problem',
        widget=CheckboxSelectMultiple
    )
    usp = forms.MultipleChoiceField(
        choices=USP_CHOICES,
        label='Unique Selling Proposition',
        widget=CheckboxSelectMultiple
    )
    additional_context = forms.CharField(
        label='Additional Context',
        required=False,
        widget=forms.Textarea
    )


class ScriptForm(forms.Form):
    SCRIPT_LENGTH_CHOICES = [
        ('30 to 60 words', '30 to 60 words'),
        ('60 to 120 words', '60 to 120 words'),
        ('120 to 240 words', '120 to 240 words')
    ]

    selected_messages = forms.CharField(label='Selected Messages')

    script_length = forms.ChoiceField(choices=SCRIPT_LENGTH_CHOICES, label='Script Length')
    call_to_action = forms.CharField(label='Call To Action')
    additional_context = forms.CharField(
        label='Additional Context',
        required=False,
        widget=forms.Textarea
    )