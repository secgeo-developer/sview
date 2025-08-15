from django.contrib import admin

# Register your models here.
from scv.models import GeneralSetting, ImageSetting, SocialMedia

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

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'icon')
    search_fields = ('link', 'icon')

    class Meta:
        model = SocialMedia
        fields = '__all__'