from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Image, APPUser

# Form required for updating editing images
class ImageUploadForm(forms.ModelForm):
    uploadimage = forms.ImageField()

    def clean_uploadimage(self):
        image = self.cleaned_data.get('uploadimage')
        if image:
            if image._size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 5mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")
    class Meta:
        model = Image #django models a form corresponding to the Image object
        fields = ('uploadimage', 'caption')#list of fields required to be filled up or edited as a part of form

# Form required for registering
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 8:
                raise ValidationError("password length too small (min 9 chars)")
            return password
        else:
            raise ValidationError("Couldn't get the password")
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

# Form required for Login
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = APPUser
        fields = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
