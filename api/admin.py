from django.contrib import admin
from . import models

admin.site.site_header = "Agyenim Boateng"
admin.site.site_title = "Agyenim Boateng"

admin.site.register(models.Announcement)
admin.site.register(models.Faqs)
admin.site.register(models.Contact)
admin.site.register(models.Blog)
admin.site.register(models.Team)
