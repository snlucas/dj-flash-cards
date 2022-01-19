from django.views.generic import ListView
from .models import Card


class FlashCardListView(ListView):
    model = Card
    context_object_name = "cards"
    template_name = "flash_card/home.html"
