from django.views import generic

from .models import SalesItem


class SalesItemListView(generic.ListView):
    template_name = 's3cms/list.html'
    context_object_name = 'all_sales_items'

    def get_queryset(self):
        return SalesItem.objects.all()


class SalesItemDetailView(generic.DetailView):
    model = SalesItem
    template_name = 's3cms/detail.html'
