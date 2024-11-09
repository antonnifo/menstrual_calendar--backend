from django.db import models
from users.models import CustomUser

# Create your models here.
class Cycles(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    fertile_start = models.DateField()
    fertile_end = models.DateField()
    predicted_period_start = models.DateField()
    predicted_period_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
