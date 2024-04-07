from django.contrib import admin

# Register your models here.
from .models import Product, member

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Product)
admin.site.register(member, MemberAdmin)
