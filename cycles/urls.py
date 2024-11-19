from django.urls import path
from .views import CycleCreateView, CycleDetailView, CycleUpdateView, CycleDeleteView, UserCycleListView

urlpatterns = [
    path('add-cycle/', CycleCreateView.as_view(), name='cycle-create'),
    path('get-cycle/<int:pk>/', CycleDetailView.as_view(), name='cycle-detail'),
    path('all-cycles/<str:user_id>/', UserCycleListView.as_view(), name='all-cycles'),
    path('edit-cycle/<int:id>/', CycleUpdateView.as_view(), name='cycle-update'),
    path('delete-cycle/<int:id>/', CycleDeleteView.as_view(), name='cycle-delete'),
]
