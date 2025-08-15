import site
from django.shortcuts import render
from scv.models import GeneralSetting

# Create your views here.


def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj


def sview_context(request):
    # GeneralSetting
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')

    # ImageSetting

    # Skill

    # Experience

    # Education

    # Social Media

    # Document

    return {
        'site_title': site_title,
        'site_keywords': site_keywords,

    }


def index(request):
    # site_title = GeneralSetting.objects.get(name='site_title').parameter
    # context = {
    #     'site_title': site_title,
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')
