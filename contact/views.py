from django.views.generic import ListView
from .models import Identity


class ContactListView(ListView):
    model = Identity

    def get_queryset(self):
        return Identity.objects.select_subclasses()
