from django.views.generic import TemplateView
from django_user_agents.utils import get_user_agent
from django.shortcuts import render

def index(request):
    user_agent = get_user_agent(request)

    if user_agent.is_mobile:
        return render(request, 'projects/m_index.html')
    else:
        return render(request, 'projects/index.html')


def valutes(request):
    user_agent = get_user_agent(request)

    return render(request, 'projects/valutes.html')








