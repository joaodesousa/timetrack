from django.contrib import admin
from .models import Timesheet, Servico
# Register your models here.
admin.site.register(Servico)
admin.site.register(Timesheet)