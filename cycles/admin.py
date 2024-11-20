from django.contrib import admin
from .models import Cycles 

# Register your models here.
@admin.register(Cycles)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'period_start', 'period_end', 'fertile_start','fertile_end','ovulation','predicted_period_start', 'predicted_period_end')
