from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("accounts.urls")) # accounts.urls.pyを読み込むための設定を追加
]

