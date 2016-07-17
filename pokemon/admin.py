from django.contrib import admin

from .models import Pokemon, Trainer, Team

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Trainer)
admin.site.register(Team)
