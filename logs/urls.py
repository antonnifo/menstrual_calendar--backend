from django.urls import path
from .views import (
    SexualIntercourseLogCreateView, SexualIntercourseLogListView, SexualIntercourseLogDetailView,
    MoodLogCreateView, MoodLogListView, MoodLogDetailView,
    BloodFlowLogCreateView, BloodFlowLogListView, BloodFlowLogDetailView,
    MedicationLogCreateView, MedicationLogListView, MedicationLogDetailView,
    SymptomLogCreateView, SymptomLogListView, SymptomLogDetailView
)

urlpatterns = [
    # Sexual Intercourse Log URLs
    path('sexual-intercourse/', SexualIntercourseLogCreateView.as_view(), name='sexual-intercourse-create'),
    path('sexual-intercourse/list/', SexualIntercourseLogListView.as_view(), name='sexual-intercourse-list'),
    path('sexual-intercourse/<int:pk>/', SexualIntercourseLogDetailView.as_view(), name='sexual-intercourse-detail'),

    # Mood Log URLs
    path('mood/', MoodLogCreateView.as_view(), name='mood-create'),
    path('mood/list/', MoodLogListView.as_view(), name='mood-list'),
    path('mood/<int:pk>/', MoodLogDetailView.as_view(), name='mood-detail'),

    # Blood Flow Log URLs
    path('blood-flow/', BloodFlowLogCreateView.as_view(), name='blood-flow-create'),
    path('blood-flow/list/', BloodFlowLogListView.as_view(), name='blood-flow-list'),
    path('blood-flow/<int:pk>/', BloodFlowLogDetailView.as_view(), name='blood-flow-detail'),

    # Medication Log URLs
    path('medication/', MedicationLogCreateView.as_view(), name='medication-create'),
    path('medication/list/', MedicationLogListView.as_view(), name='medication-list'),
    path('medication/<int:pk>/', MedicationLogDetailView.as_view(), name='medication-detail'),

    # Symptom Log URLs
    path('symptom/', SymptomLogCreateView.as_view(), name='symptom-create'),
    path('symptom/list/', SymptomLogListView.as_view(), name='symptom-list'),
    path('symptom/<int:pk>/', SymptomLogDetailView.as_view(), name='symptom-detail'),
]