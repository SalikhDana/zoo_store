from django.contrib import admin
from .models import Animal, Commands
# Register your models here.
class AnimalInline(admin.StackedInline):
    model = Commands
    extra = 2

class AnimalAdmin(admin.ModelAdmin):
    fields = ['animal_name', 'animal_desc', 'animal_price', 'animal_date']
    inlines = [AnimalInline]
    list_filter = ['animal_date']


admin.site.register(Animal, AnimalAdmin)

admin.site.register(Commands)