# from django import forms
# from .models import Contact

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'


# forms.py
# from django import forms
# from .models import ContactMessage

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = ['name', 'email', 'message']

from django import forms
from .models import ContactMessage,ReportMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class ReportmalForm(forms.ModelForm):
    class Meta:
        model = ReportMessage
        fields = ['invalidmal', 'comment']
