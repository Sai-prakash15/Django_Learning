"""Induction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from File_Uploads import views
from Models.views import Transactions, my_view, Middleware  # Sleep_Async
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/status/', include('Rest_framework_status.api.urls')),
    path('csrf/', include('Csrf.urls')),
    path('file_upload/', include('File_Uploads.urls')),
    path('success/url/', views.success),
    path('polls/', include('polls.urls')),
    path('accounts/', include('Signals.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('orms/', include('Models.urls')),
    path('dbtransactions/', Transactions.as_view()),
    path('sleep_async/', my_view),
    path('caching/', include('Caching.urls')),
    path('encrypt_decrypt/', Middleware.as_view()),
]
