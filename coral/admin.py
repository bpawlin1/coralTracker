from django.contrib import admin

# Register your models here.
from coral.models import Coral


class coralAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coral, coralAdmin)
