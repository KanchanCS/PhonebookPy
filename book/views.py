from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Contact


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html',  {'contacts': contacts})

def contact_details(request, id):
        contact = get_object_or_404(Contact, pk=id)
        context = {"contact": contact}
        return render(request, 'details.html', context)

def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect("book:home")
    else:
        form = ContactForm()
    return render(request, "create.html", {"form": form})

def edit_contact(request, id):
    pi = get_object_or_404(Contact,pk=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('book:home')  
    else:
        form = ContactForm(instance=pi)        
    return render(request, 'edit_contact.html', {'form':form})    

def delete_contact(request, id):
    if request.method == 'POST':
        pi = Contact.objects.get(pk=id)
        pi.delete()
        return redirect('book:home')
