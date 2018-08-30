from django.contrib import admin
from .models import Post, Unit, Doctor, Drug

class DrugAdmin(admin.ModelAdmin):
    list_display = ('drug_name', 'drug_place')

admin.site.register(Post)
admin.site.register(Unit)
admin.site.register(Doctor)
admin.site.register(Drug, DrugAdmin)


