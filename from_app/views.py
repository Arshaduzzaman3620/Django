from django.shortcuts import render, redirect
from .forms import ContactForm

# Home page view
def home_view(request):
    return render(request, 'from_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()  # Call the method to send email
            return redirect('contact-success')  # Redirect to a success page
    else:
        form = ContactForm()  # Initialize an empty form if GET request

    # Always return the form and context to render the contact page
    context = {'form': form}
    return render(request, 'from_app/contact.html', context)

def contact_success_view(request):
    return render(request, 'from_app/contact_success.html')
