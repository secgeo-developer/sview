from django.contrib import admin

# Register your models here.
from .models import GeneralSetting

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'parameter', 'created_date', 'updated_date')
    search_fields = ('name', 'description', 'parameter')

    class Meta:
        model = GeneralSetting
        fields = '__all__'