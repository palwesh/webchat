from django.views.generic import TemplateView
from users.models import *

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    


class userlist(TemplateView):
    template_name = 'pages/userlist.html'

    def get_context_data(self,**kwargs):
        context = super(userlist,self).get_context_data(**kwargs)
        context['object_list'] = CustomUser.objects.all()
        return context
