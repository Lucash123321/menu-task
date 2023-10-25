from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path("test-named-url/", views.test_url, name="test"),
    path("test/big/url/", views.test_url, name="big-url"),
    path("<str:test>/", views.index, name="index"),
    ]
