from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import PostDaily
from .forms import PostDailyForm
from django.http import HttpResponseForbidden


class IndexView(TemplateView):
    """
    Indexを表示させるための関数
    index.htmlを表示させる
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        DBからPostDailyを取得して
        格納する。

        """
        context = super().get_context_data(**kwargs)
        # ここで必要なデータを取得し、コンテキストに追加する
        postdailies = (
            PostDaily.objects.all()
        )  # 例としてすべての PostDaily インスタンスを取得する
        context["postdailies"] = postdailies
        return context


class SignupView(CreateView):
    """ユーザー登録用ビュー"""

    form_class = SignUpForm  # 作成した登録用フォームを設定
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")  # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response


# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


# LogoutViewを追加
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")


def DailyView(request):
    if request.method == "POST":
        form = PostDailyForm(request.POST)
        if form.is_valid():
            days = form.cleaned_data["days"]
            # クエリセットを取得
            exists = PostDaily.objects.filter(days=days, created_by_id=request.user.id).exists()

            # クエリセットの長さを取得
            if not exists:
                postdaily = PostDaily()
                postdaily.days = form.cleaned_data["days"]
                postdaily.title = form.cleaned_data["title"]
                postdaily.description = form.cleaned_data["description"]
                postdaily.created_by = request.user
                postdaily.save()
                return redirect("/")
            else:
                # フォームにエラーメッセージを追加
                form.add_error(None, "指定された日付はすでに存在します。")
        return render(request, "daily_report.html", {"form": form})       
    form = PostDailyForm()
    return render(request, "daily_report.html", {"form": form})


# 各詳細画面
def Detail(request, pk):
    instance = get_object_or_404(PostDaily, pk=pk)
    return render(request, "detail.html", {"instance": instance})


# 削除画面
def delete_post(request, pk):
    instance = get_object_or_404(PostDaily, pk=pk)
    instance.delete()
    return redirect("/")  # 削除後は適切なリダイレクト先を設定する


# 編集画面
def edit(request, pk):
    instance = get_object_or_404(PostDaily, pk=pk)
    if instance.created_by_id != request.user.id:
        return HttpResponseForbidden("このユーザでは許可されていません")
    if request.method == "POST":
        form = PostDailyForm(request.POST, instance=instance)
        if form.is_valid():
            instance.days = form.cleaned_data["days"]
            instance.title = form.cleaned_data["title"]
            instance.description = form.cleaned_data["description"]
            instance.created_by = request.user
            instance.save()
            return redirect("/")
    else:
        form = PostDailyForm(instance=instance)
        return render(request, "edit.html", {"form": form})


