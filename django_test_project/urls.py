"""django_test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django_test_project.apps.listings import urls as listings_urls
from django_test_project.apps.users import urls as users_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Django test project API",
        default_version="v1",
        description="A simple demo API allowing to browse among listings and listings owners.",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("users/", include(users_urls, namespace="users")),
    path("listings/", include(listings_urls, namespace="listings")),
    path("admin/", admin.site.urls),
]
