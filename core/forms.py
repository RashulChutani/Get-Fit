from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email','first_name','username','password',]
        widgets = {
            'email': forms.EmailInput(
				attrs={
					'class': 'form-control'
					}
				),
            'first_name': forms.Textarea(
				attrs={
					'class': 'form-control',
                    'style':'max-height: 2em'
					}
				),
            'password': forms.PasswordInput(
				attrs={
					'class': 'form-control'
					}
				),
            'username': forms.Textarea(
				attrs={
					'class': 'form-control',
                    'style':'max-height: 2em'
					}
				),
			}
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs = {
        'class' : 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }))