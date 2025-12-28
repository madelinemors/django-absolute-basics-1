from django.shortcuts import render, HttpResponse
from .models import TodoItem, WhatsAppItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items}) # request to the page, page, parameters (named)

def whatsapp(request):
    if request.method == 'POST':
        if form.is_valid():
            # Get the item instance based on the memo from the form
            item = WhatsAppItem.objects
            item = WhatsAppItem(name="test1",phoneNumber=form.cleaned_data['phoneNumber'],emailAddress=form.cleaned_data['emailAddress']);
            item.save()
            return redirect(request,'whatsapp.html')  # Redirect to the table display page after updating
    return render(request, "whatsapp.html")
