from django.urls import path
from .views import FlashCardListView


urlpatterns = [
    path("", FlashCardListView.as_view()),
]