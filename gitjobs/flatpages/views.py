from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings

class HomepageView(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        user = request.user
        context = {
            'user':user,
        }
        return render(
            request,
            self.template_name,
            context
        )