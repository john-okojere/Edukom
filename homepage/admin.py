from django.contrib import admin
from .import models

admin.site.register( models.AboutChild)
admin.site.register( models.Guardian)
admin.site.register( models.Location)
admin.site.register( models.Lesson)