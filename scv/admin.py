from django.contrib import admin

# Register your models here.
from scv.models import GeneralSetting, ImageSetting, SocialMedia, Education, Experience, Skill, Document

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'parameter', 'created_date', 'updated_date')
    search_fields = ('name', 'description', 'parameter')

    class Meta:
        model = GeneralSetting
        fields = '__all__'

@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_file')
    search_fields = ('name', 'description')

    class Meta:
        model = ImageSetting
        fields = '__all__'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage', 'order',
                    'updated_date', 'created_date')
    search_fields = ('name', 'order', 'percentage')

    class Meta:
        model = Skill
        fields = '__all__'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_title',
                    'position', 'start_date', 'end_date')
    search_fields = ('company_name', 'job_title', 'position')

    class Meta:
        model = Experience
        fields = '__all__'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'department',
                    'position', 'start_date', 'end_date')
    search_fields = ('school_name', 'department', 'position')

    class Meta:
        model = Education
        fields = '__all__'

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'icon')
    search_fields = ('link', 'icon')

    class Meta:
        model = SocialMedia
        fields = '__all__'


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'button_text', 'file', 'order', 'created_date', 'updated_date')
    search_fields = ('slug', 'button_text')

    class Meta:
        model = Document
        fields = '__all__'