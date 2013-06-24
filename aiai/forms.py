from django.forms import ModelForm
from aiai.models. import Item, Store

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields('name', 'description', 'store_number', 'image_file',)
        

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ('store_number', 'region', 'pause_between_posts', 
        'pause_between_publish', 'phone_number', 'manager_name', 
        'ficticious_name', 'email',)