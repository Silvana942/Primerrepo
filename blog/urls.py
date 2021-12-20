"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path#permite comunicarse con otros archivos urls(en este caso porque se creo urls.py en cada app)
from apps.post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path('categorias/crear', views.crear_categorias, name='crear_categorias')
]
