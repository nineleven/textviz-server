from django.urls import path

from . import views

urlpatterns = [
    path('get_available_texts/', views.SampleTextsView.as_view(), name='get_available_texts'),
    path('get_text/', views.SpecificTextView.as_view(), name='get_text'),
    path('encode_text/', views.EncodeTextsView.as_view(), name='encode_text'),
]
