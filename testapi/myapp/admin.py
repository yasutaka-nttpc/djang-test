from django.contrib import admin

# Register your models here.
from .models import Pop3, Imap, Smtpauth, Submission


@admin.register(Pop3)
class Pop3(admin.ModelAdmin):
  pass

@admin.register(Imap)
class Imap(admin.ModelAdmin):
  pass

@admin.register(Smtpauth)
class Smtpauth(admin.ModelAdmin):
  pass

@admin.register(Submission)
class Submission(admin.ModelAdmin):
  pass
