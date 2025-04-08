from django import forms 

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  message = forms.CharField(widget=forms.Textarea)
  
  # Add any additional fields you need for your form
  def send_email(self):
    # Logic to send email using the form data
    print(f"Sending email to {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")