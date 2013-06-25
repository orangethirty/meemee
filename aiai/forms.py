from django.forms import ModelForm
from aiai.models import Item, Store, Demo


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'store_number', 'image_file',)
        

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ('store_number', 'region', 'pause_between_post', 
        'pause_before_publish', 'phone_number', 'manager_name', 
        'ficticious_name', 'email',)
        

class DemoForm(ModelForm):
    class Meta:
        model = Demo
        fields = ('name', 'email', 'phone_number',)