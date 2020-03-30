from django import forms

class ContactForm(forms.Form):
    '''
    form to collect user information for contact
    '''
    name                    = forms.CharField(required=True)
    email                   = forms.EmailField(required=True)
    phone_number            = forms.CharField(required=True)
    message                 = forms.CharField(widget=forms.Textarea, required=True)


class CharityOrgRegForm(forms.Form):
    '''
    form to regisster charity organizations
    '''
    name                    = forms.CharField(required=True)
    email                   = forms.EmailField(required=True)
    phone_number            = forms.CharField(required=True)
    location                = forms.CharField(required=False)