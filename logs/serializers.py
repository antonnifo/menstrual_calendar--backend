from rest_framework import serializers
from .models import SexualIntercourseLog, MoodLog, BloodFlowLog, MedicationLog, SymptomLog

class SexualIntercourseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexualIntercourseLog
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class MoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodLog
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class BloodFlowLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodFlowLog
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class MedicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationLog
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class SymptomLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomLog
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
