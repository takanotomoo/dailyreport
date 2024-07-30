"""
これはadminです
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import User
from .models import PostDaily
from django import forms
from .models import To_do


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


class LoginFrom(AuthenticationForm):
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


# フォームを仮で追加(将来的に削除)
class To_doForm(forms.ModelForm):
    class Meta:
        model = To_do
        fields = (
            'deadline',
            'task',
        )
        widgets = {
            'deadline': forms.NumberInput(attrs={
                "type": "date"
            })
        }
