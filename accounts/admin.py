"""
これはadminです
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, PostDaily

admin.site.register(User)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
admin.site.register(PostDaily)  # PostDailyモデルを登録
