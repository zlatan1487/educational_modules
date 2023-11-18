from django.contrib import admin
from education_modules.models import EducationalModule, Review
# Register your models here.


@admin.register(EducationalModule)
class EducationalModuleAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'title',
                    'description',  'created_at',
                    'is_active', 'avatar', 'owner',)
    list_filter = ('title',)
    search_fields = ('title', 'description',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'author',
                    'educational_module', 'created_at',)
