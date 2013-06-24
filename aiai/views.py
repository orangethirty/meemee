from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, DetailView
from django.core.urlresolvers import reverse_lazy

from .models import Item, Store
from .form import ItemForm, StoreForm


class ItemView(CreateView):
    model = Item
    form_class = ItemForm
    
    def get_success_url(self):
        #item uri is id #
        return reverse_lazy('item_detail', args=[self.object.id])
        
    
    def form_valid(self, form):
        
        
class ItemDetailView(DetailView):
    model = Item        
        

class StoreView(CreateView):
    model = Store
    form_class = StoreForm
    

class StoreDetailView(DetailView):
    model = Store