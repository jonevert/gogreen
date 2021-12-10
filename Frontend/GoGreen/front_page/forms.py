from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets, ModelForm
from django import forms


class ImprovedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
