from django import forms
from account.models import Member


class MemberJoinForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_email', 'user_name', 'user_pw1', 'user_pw2', 'user_birth']
        labels={
            'user_email': 'ID (E-mail)',
            'user_name': 'User name',
            'user_pw1': 'Password',
            'user_pw2': 'Confirm Password',
            'user_birth': 'Date of Birth'
        }
        widgets ={
            'user_email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'name': 'user_email'
                }
            ),
            'user_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_pw1': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_pw2': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_birth' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'format': '%Y-%m-%d',
                    'placeholder' : 'YYYY-MM-DD'
                }
            )
        }


class LogInForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_email', 'user_pw1']
        labels = {
            'user_email': 'ID (E-mail)',
            'user_pw1': 'Password',
        }
        widgets = {
            'user_email': forms.EmailInput(
                attrs={
                    'class': 'form-control'

                }
            ),

            'user_pw1': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class ModifyUserInfoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_email', 'user_name', 'user_pw1', 'user_pw2', 'user_birth']
        labels = {
            'user_email': 'ID (E-mail)',
            'user_name': 'User name',
            'user_pw1': 'Password',
            'user_pw2': 'Confirm Password',
            'user_birth': 'Date of Birth'
        }
        widgets = {
            'user_email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'name': 'user_email',
                    'readonly': True
                }
            ),
            'user_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_pw1': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_pw2': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'format': '%Y-%m-%d',
                    'placeholder': 'YYYY-MM-DD'
                }
            )
        }


