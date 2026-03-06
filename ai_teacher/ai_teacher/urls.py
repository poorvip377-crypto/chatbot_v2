"""
URL configuration for ai_teacher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path,include
>>>>>>> 1599528dc1b563fe6c53fb9c4039f8961d63a1a4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
<<<<<<< HEAD
]
=======
]
>>>>>>> 1599528dc1b563fe6c53fb9c4039f8961d63a1a4
