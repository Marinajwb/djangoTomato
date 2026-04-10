from django import forms
from django.core.exceptions import ValidationError
from users.models import User
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'placeholder' : '사용자명(3자리이상)'}
        ),)

    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
        attrs={'placeholder':'비밀번호 (4자리이상)'},
        ),)


class signupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(f'입력한 사용자명{username}은 이미 사용 중 입니다.')
        return username

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if( password1 != password2 ):
            #pw2 필드에 오류를 추가
            self.add_error('password2','비밀번화 확인란의 값이 다릅니다.')
    def save(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        short_description = self.cleaned_data["short_description"]
        profile_image = self.cleaned_data["profile_image"]
        user = User.objects.create_user(
            username  = username,
            password1 = password1,
            profile_image = profile_image,
            short_description = short_description,
        )
        return user