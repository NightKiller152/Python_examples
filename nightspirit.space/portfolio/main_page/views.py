from django.views.generic import TemplateView
from django_user_agents.utils import get_user_agent
from django.shortcuts import render


def index(request):
    user_agent = get_user_agent(request)

    if user_agent.is_mobile:
        return render(request, 'main_page/m_home.html')
    else:
        return render(request, 'main_page/home.html')


def contacts(request):
    user_agent = get_user_agent(request)

    if user_agent.is_mobile:
        return render(request, 'main_page/m_contacts.html')
    else:
        return render(request, 'main_page/contacts.html')
