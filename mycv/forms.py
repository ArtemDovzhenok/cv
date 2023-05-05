from captcha.fields import CaptchaField
from django import forms
from django.urls import path, include

from .models import Comment


class GuestCommentForm(forms.ModelForm):
    mycaptcha = CaptchaField()
    class Meta:
         model = Comment
         fields = '__all__'


class PasswordInputValue(forms.Form):
    namberCount = forms.IntegerField(min_value=1, max_value=10, label='Введіть кіл-сть паролів',
                                     help_text='Максимально 10 паролів')
    passwordLen = forms.IntegerField(min_value=8, max_value=50,label='Введіть бажану довжину паролю',
                                     help_text='Максимально 50 символів')


class MailForm(forms.Form):
    emailAdress = forms.EmailField()
    subject = forms.CharField(max_length=50)
    bodyText = forms.CharField(widget=forms.Textarea(attrs={'name':'bodyText', 'rows':3, 'cols':30}))
