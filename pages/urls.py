from django.urls import path

from .views import HomePageView, userlist

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('userlist/', userlist.as_view(), name="userlist"),
]

