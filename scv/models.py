from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    # image_file = models.ImageField(
    #   default='', verbose_name='Image File', storage=ImageSettingStorage(), help_text="Upload an image file")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']

class Skill(AbstractModel):
    order = models.IntegerField(default=0, blank=True,
                                verbose_name='Skill Order', help_text="This is variable of the setting")
    name = models.CharField(default='', max_length=100, blank=True,
                            verbose_name='Skill Name', help_text="This is variable of the setting")
    percentage = models.IntegerField(default=50, blank=True,
                                     verbose_name='Skill Percentage',
                                     validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['order']

class Experience(AbstractModel):
    company_name = models.CharField(
        max_length=100, blank=True, verbose_name='Company Name', help_text="Enter the name of the company")
    job_title = models.CharField(
        max_length=100, blank=True, verbose_name='Job Title', help_text="Enter your job title")
    position = models.CharField(
        max_length=100, blank=True, verbose_name='Position', help_text="Enter your position")
    start_date = models.DateField(blank=True, null=True, verbose_name='Start Date',
                                  help_text="Enter the start date of your experience")
    end_date = models.DateField(default=None, blank=True, null=True,
                                verbose_name='End Date', help_text="Enter the end date of your experience")

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['-start_date']


class Education(AbstractModel):
    school_name = models.CharField(
        max_length=100, blank=True, verbose_name='Institution Name', help_text="Enter the name of the institution")
    department = models.CharField(
        max_length=254, blank=True, verbose_name='Department', help_text="Enter your department")
    position = models.CharField(
        max_length=100, blank=True, verbose_name='Position', help_text="Enter your position")
    start_date = models.DateField(blank=True, null=True, verbose_name='Start Date',
                                  help_text="Enter the start date of your education")
    end_date = models.DateField(default=None, blank=True, null=True,
                                verbose_name='End Date', help_text="Enter the end date of your education")

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-start_date']


class SocialMedia(AbstractModel):
    order = models.IntegerField(default=0, blank=True,
                                verbose_name='Order', help_text="Enter the order of the social media link")
    link = models.URLField(default='', max_length=200, blank=True, verbose_name='Link',
                           help_text="Enter the URL of your social media profile")
    icon = models.CharField(default='', max_length=100, blank=True, verbose_name='Icon',
                            help_text="Enter the icon class for your social media profile")

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ['order']

class Document(AbstractModel):
    order = models.IntegerField(default=0, blank=True,
                                verbose_name='Order', help_text="Enter the order of the document")
    slug = models.SlugField(default='', max_length=100, blank=True,
                            verbose_name='Document Slug', help_text="Enter the slug for the document")
    button_text = models.CharField(default='', max_length=254, blank=True,
                                   verbose_name='Button Text', help_text="Enter the button text")
    file = models.FileField(upload_to='documents/', blank=True,
                            verbose_name='Document File', help_text="Upload the document file")

    #file = models.FileField(storage=DocumentStorage(), blank=True,
    #                       verbose_name='Document File', help_text="Upload the document file")

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['order']