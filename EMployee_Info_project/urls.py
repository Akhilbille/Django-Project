"""EMployee_Info_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url



admin.site.site_header = "AP Citizen"
admin.site.index_title = 'ADMIN'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landingpage.urls")),
    path("",include("home.urls")),
    path("", include("signup.urls")),
    path("", include("login.urls")),
    path("", include("payment.urls")),
    path("", include("update.urls")),
    path("", include("contact_us.urls"))
]


# urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  [

  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),]


handler404 = 'landingpage.views.error_404'