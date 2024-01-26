from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
  # inlines = [InstructorInline]
  search_fields = ["email"]
  list_filter = ["email"]
  fields = ["email", "name", "lastname"]
  list_display = ("id", "email")

admin.site.register(User, UserAdmin)