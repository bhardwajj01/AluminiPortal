from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import router as account_router

urlpatterns = [
    path("",include(account_router.urls)),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
