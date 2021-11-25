import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class queryForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    content = forms.Textarea()
    image = forms.ImageField(required=False)
    now = datetime.date.today()

    def transfer_to_email(self):

        pass

