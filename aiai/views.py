from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Item, Store, Demo
from .forms import ItemForm, StoreForm, DemoForm


def index(request):
    return render_to_response('index/index.html')
    

class DemoView(CreateView):
    model = Demo
    form_class= DemoForm
    template_name = "demo/demo_form.html"
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')
        
class DemoListView(ListView):
    model = Demo
    template_name = "demo/list_all.html"
    
    def get_queryset(self):
        return Demo.objects.order_by('-id')
        
class DemoUpdateView(UpdateView):
    #this is not right.
    #moving on to other important issues.
    #will come back once i have thought about it more.
    model = Demo
    fields = ['followed_up']
    template_name = 'demo/followed_up.html'

class ItemView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item/item_form.html"
    
    def get_success_url(self):
        #item uri is id #
        return reverse_lazy('item_detail', args=[self.object.id])
        
    
    def form_valid(self, form):
        pass
        
class ItemDetailView(DetailView):
    model = Item        
        

class StoreView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = "store/store_form.html"

class StoreDetailView(DetailView):
    model = Store