from django.forms import ModelForm, Textarea
from .models import Tour,User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({
                'class': 'form-control rounded',
                'style': 'height: 55px; border-radius: 10px;',
                'placeholder': field.label
            })
            if isinstance(field.widget, Textarea):
                field.widget.attrs.update({'style': 'height: 120px;'})

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email', 
            'address', 
            'phone_number',
            'profile_picture',
            'password1',
            'password2'
        ]


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"
        exclude = ['business']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'email', 
            'address', 
            'phone_number',
            'profile_picture'
        ]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for myField in self.fields:
                self.fields[myField].widget.attrs['class'] = 'form-control'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)