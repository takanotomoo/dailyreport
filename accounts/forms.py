"""
これはadminです
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import User
from .models import PostDaily
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )


class LoginForm(AuthenticationForm):
    """ログインフォーム

    Args:
        AuthenticationForm (AuthenticationForm): Django デフォルトの認証フォーム
    """
    class Meta:
        model = User


# フォームを追加
class PostDailyForm(forms.ModelForm):
    class Meta:
        model = PostDaily
        fields = ('title', 'days', 'description')
        widgets = {
            'days': forms.NumberInput(attrs={
                "type": "date"
            })
        }
