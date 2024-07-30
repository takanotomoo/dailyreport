from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = "accounts"

# URLパターンを登録するための変数
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"), 
    path('daily_report/', views.DailyView, name="daily_report"),
    path('detail/<int:pk>/', views.Detail, name="detail"),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('new/', views.new, name="new"),
]
