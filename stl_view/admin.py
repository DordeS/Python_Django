from django.contrib import admin
from stl_view.models import Stl_view

# Register your models here.
class Stl_viewAdmin(admin.ModelAdmin):
  pass

admin.site.register(Stl_view, Stl_viewAdmin)