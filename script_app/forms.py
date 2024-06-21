from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .model.teachtap_core_inputs import PROBLEMS_INFO, USP_INFO


class MessageForm(forms.Form):
    PRODUCT_CHOICES = [
        ('TeachTap', 'TeachTap'),
    ]
    AUDIENCE_CHOICES = [
        ('Parent', 'Parent'),
        ('Student', 'Student')
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
        label='Unique Selling Point',
        widget=CheckboxSelectMultiple
    )


class HookForm(forms.Form):
    PRODUCT_CHOICES = [
        ('TeachTales', 'TeachTales'),
        ('TeachTap', 'TeachTap'),
        ('Magic Academy', 'Magic Academy'),
    ]

    AUDIENCE_CHOICES = [
        ('Parent-facing', 'Parent-facing'),
        ('Student-facing', 'Student-facing'),
    ]

    product_name = forms.ChoiceField(choices=PRODUCT_CHOICES, label='Product Name')
    target_audience = forms.ChoiceField(choices=AUDIENCE_CHOICES, label='Target Audience')
    narrator = forms.CharField(label='Narrator', max_length=100)
    core_message = forms.CharField(label='Core Message', widget=forms.Textarea)
    additional_creator_context = forms.CharField(label='Additional Creator Context', widget=forms.Textarea)


class ScriptForm(forms.Form):
    LENGTH_CHOICES = [
        ('30-60 words', '30-60 words'),
        ('60-120 words', '60-120 words'),
        ('120-240 words', '120-240 words'),
    ]

    message = forms.ChoiceField(choices=[], label='Messaging')
    script_length = forms.ChoiceField(choices=LENGTH_CHOICES, label='Script Length')

    def __init__(self, *args, **kwargs):
        message_choices = kwargs.pop('message_choices', [])
        super(ScriptForm, self).__init__(*args, **kwargs)
        self.fields['message'].choices = message_choices
