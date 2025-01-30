from django.urls import path
from .views import (
    SexualIntercourseLogCreateView, MoodLogCreateView, BloodFlowLogCreateView,
    MedicationLogCreateView, SymptomLogCreateView
)

urlpatterns = [
    path('sexual-intercourse/', SexualIntercourseLogCreateView.as_view(), name='sexual-intercourse-log'),
    path('mood/', MoodLogCreateView.as_view(), name='mood-log'),
    path('blood-flow/', BloodFlowLogCreateView.as_view(), name='blood-flow-log'),
    path('medication/', MedicationLogCreateView.as_view(), name='medication-log'),
    path('symptom/', SymptomLogCreateView.as_view(), name='symptom-log'),
]