from django.urls import path
from .views import CarUpdateView

urlpatterns = [
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
]
