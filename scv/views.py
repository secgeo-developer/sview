
from django.shortcuts import render
from scv.models import GeneralSetting, ImageSetting
# Create your views here.


def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj


def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).image_file
    except:
        obj = ''
    return obj


def sview_context(request):
    # GeneralSetting
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    site_author = get_general_setting('site_author')
    home_banner_area_jobs = get_general_setting('home_banner_area_jobs')
    home_banner_area_birth_date = get_general_setting(
        'home_banner_area_birth_date')
    home_banner_area_phone = get_general_setting('home_banner_area_phone')
    home_banner_area_email = get_general_setting('home_banner_area_email')
    home_banner_area_address = get_general_setting('home_banner_area_address')
    welcome_area_myself = get_general_setting('welcome_area_myself')

    # ImageSetting
    site_favicon = get_image_setting('site_favicon')
    home_banner_area_image = get_image_setting('home_banner_area_image')
 

    # Skill

    # Experience

    # Education

    # Social Media

    # Document

    return {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'site_author': site_author,
        'home_banner_area_jobs': home_banner_area_jobs,
        'home_banner_area_birth_date': home_banner_area_birth_date,
        'home_banner_area_phone': home_banner_area_phone,
        'home_banner_area_email': home_banner_area_email,
        'home_banner_area_address': home_banner_area_address,
        'welcome_area_myself': welcome_area_myself,
        'site_favicon': site_favicon,
        'home_banner_area_image': home_banner_area_image,
    }


def index(request):
    # site_title = GeneralSetting.objects.get(name='site_title').parameter
    # context = {
    #     'site_title': site_title,
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')
