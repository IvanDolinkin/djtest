from django.urls import path

from measurement.views import SensorCreateView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
