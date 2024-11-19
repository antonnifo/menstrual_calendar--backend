from rest_framework import serializers
from .models import Cycles

class CyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycles
        fields = ['id', 'period_start', 'period_end', 'fertile_start', 'fertile_end', 'ovulation','predicted_period_start', 'predicted_period_end', 'created_at', 'edited_at']
        read_only_fields = ['id', 'created_at', 'edited_at']