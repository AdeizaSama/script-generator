from django import forms


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

    hook = forms.ChoiceField(choices=[], label='Hook')
    script_length = forms.ChoiceField(choices=LENGTH_CHOICES, label='Script Length')

    def __init__(self, *args, **kwargs):
        hook_choices = kwargs.pop('hook_choices', [])
        super(ScriptForm, self).__init__(*args, **kwargs)
        self.fields['hook'].choices = hook_choices
