"""demoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from demo import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/',views.hello),
    url(r'^hello2/',views.hello2),
    url(r'^hello3/',views.hello3),
    url(r'^home/',views.home),
    # demo 子路由 http://localhost:8000/demo/hello/
    url(r'^demo/',include('demo.urls'))

]
