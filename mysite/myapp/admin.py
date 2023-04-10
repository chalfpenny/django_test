from django.contrib import admin

from .models import Customer


class CustomModelAdmin(admin.ModelAdmin):
    
    def __init__(self, model, admin_site):
        self.list_per_page = 20
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)

class CustomerAdmin(CustomModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
