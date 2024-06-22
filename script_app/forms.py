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
        label='Unique Selling Point',
        widget=CheckboxSelectMultiple
    )
