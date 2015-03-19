from django import forms


class ContactFrom(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    email = forms.EmailField(label="email", max_length=100)
    message = forms.CharField(widget=forms.Textarea, label="message")