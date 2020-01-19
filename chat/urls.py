from django.urls import path, re_path


from .views import ThreadView, InboxView

app_name = 'messages'
urlpatterns = [
    path("", InboxView.as_view()),
  
    re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
    
]