from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contacts 
# Create your views here.
def ContactsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'We received your message!')
            return redirect('generals:home')
        
    else:
        form = ContactForm()
            
    return render(
        request, 
        'contact.html', 
        {'form': form}
    )   