from pyexpat import model
from turtle import update
from venv import create
from django.db import models

# Create your models here.
class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        auto_now=True, blank=True, verbose_name='Updated Date', null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='Created Date', null=True)

    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
    name = models.CharField(
        max_length=100, default='SeçGEO', blank=True, verbose_name='Name', help_text="Enter the name of the site")
    description = models.TextField(
        max_length=254, default='A short description about the site.', blank=True, verbose_name='Description', help_text="Enter a short description about the site")
    parameter = models.TextField(
        max_length=254, blank=True, verbose_name='Parameter', help_text="Enter any additional parameter")

    def __str__(self):
        # return self.site_name
        return f"{self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['-created_date']

class ImageSetting(AbstractModel):
    name = models.CharField(default='', max_length=254, blank=True,
                            verbose_name='Image Name', help_text="This is variable of the setting")
    description = models.TextField(
        default='', blank=True, verbose_name='Image Description', help_text="This is variable of the setting")
    image_file = models.ImageField(
        default='', verbose_name='Image File', upload_to='images/', help_text="Upload an image file")
    #image_file = models.ImageField(
    #   default='', verbose_name='Image File', storage=ImageSettingStorage(), help_text="Upload an image file")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']
