from django.urls import path

from measurement.views import SensorCreateView, SensorDetailView, MeasurementView, SensorListView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('sensorslist/', SensorListView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
