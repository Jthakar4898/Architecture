from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})


# contactform for client
class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"



# upload project form for client
class UploadprojectForm(forms.ModelForm):
    class Meta:
        model = Uploadproject
        fields = "__all__"

# upload portfolio from admin site
class PortfoliopageForm(forms.ModelForm):
    class Meta:
        model = Portfoliopage
        fields = "__all__"

class PersonaldetailForm(forms.ModelForm):
    class Meta:
        model =Personaldetail
        fields = "__all__"

