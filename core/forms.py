from django import forms

class ScrapeBookForm(forms.Form):
    url = forms.URLField(label="Kitob URL", required=True)
