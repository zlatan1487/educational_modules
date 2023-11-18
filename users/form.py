from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from education_modules.forms import StyleFormMixin
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'first_name',
                  'last_name', 'date_of_birth', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = \
            forms.HiddenInput()
