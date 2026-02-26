from django.urls import path
from .views import (
    MappingCreateView,
    MappingListView,
    PatientDoctorsView,
    MappingDeleteView,
)

urlpatterns = [
    path('', MappingListView.as_view()),
    path('create/', MappingCreateView.as_view()),
    path('patient/<int:patient_id>/', PatientDoctorsView.as_view()),
    path('<int:pk>/', MappingDeleteView.as_view()),
]