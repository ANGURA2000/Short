from django.shortcuts import render
from django.http import HttpResponse
# from .models import Contact
from .forms import ContactForm


def index(requests):
    return render(requests, 'index.html')

def contact(requests):
    return render(requests,'contact.html')

def privacy(requests):
    return render(requests,'privacy-policy.html')

def reportmal(requests):
    return render(requests, 'report-malicious-url.html')

def termsof(requests):
    return render(requests,'terms-of-service.html')


def urlclick(requests):
    return render(requests,'url-click-counter.html')


# # views.py
# from django.shortcuts import render, redirect
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Optionally, redirect to a success page or perform other actions
#             return redirect('success_page_contact')
   

#         else:
#             # Add this line to check for form validation errors
#             print(form.errors)  
#     else:
#         form = ContactForm()
   
    
#     return render(request, 'contact.html', {'form': form})

# from django.shortcuts import render
# from .forms import ContactForm
# from .models import ContactMessage

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             name = form.cleaned_data['Name']
#             email = form.cleaned_data['Email']
#             message = form.cleaned_data['Message']
#             contact_message = ContactMessage.objects.create(Name=name, Email=email, Message=message)
#             contact_message.save()
#             return render(request, 'contact_success.html')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'contactform': form})


from django.shortcuts import render
from .forms import ContactForm,ReportmalForm
from .models import ContactMessage,ReportMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, 'contact.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def reportmal(request):
    if request.method == 'POST':
        form = ReportmalForm(request.POST)
        if form.is_valid():
            #Save the form data to the database
            form.save()
            return render(request, 'report-malicious-url.html')
    else:
            form = ReportmalForm()
    return render(request, 'report-malicious-url.html', {'form': form})    



    # urlshortener/views.py

# main/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL

def index(request):
    return render(request, 'index.html')

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = ShortURL.create_short_url(long_url)
        return render(request, 'result.html', {'short_url': short_url,'long_url' : long_url})

    return redirect('main:index')  # Redirect to index page if not a POST request

# import hashlib

# def shorten_url(url):
#     hash_object = hashlib.sha256(url.encode())
#     short_identifier = hash_object.hexdigest()[:8]
#     return short_identifier


def redirect_to_long_url(request, short_key):
    long_url = ShortURL.get_long_url(short_key)
    if long_url:
        return redirect(long_url)
    else:
        return HttpResponse("Invalid short URL")






 

