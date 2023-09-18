from django.contrib import admin
from .models import PersonToVisit, Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'person_to_visit')
    list_filter = ('person_to_visit',)
    search_fields = ('name', 'email')

admin.site.register(PersonToVisit)
