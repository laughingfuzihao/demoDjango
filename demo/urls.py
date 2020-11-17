# demo 子路由

from django.conf.urls import url
from django.contrib import admin

from demo import views

urlpatterns = [
    # http://localhost:8000/demo/hello/
    url(r'^hello/', views.hello),
    url(r'^add/',views.add),
    url(r'^search/', views.select),
    url(r'^update/', views.update),
    url(r'^delete/', views.delete),
]
