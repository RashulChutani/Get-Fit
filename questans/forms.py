from django import forms
from .models import Questions

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['title','group','slug']
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'group': forms.Select(
				attrs={
					'class': 'form-control'
					}
				),
            'slug': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
			}