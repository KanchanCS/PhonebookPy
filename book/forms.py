from django.forms import ModelForm

from .models import Contact


class  ContactForm(ModelForm):
    

    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"