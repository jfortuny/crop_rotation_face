from django.shortcuts import render, redirect
from django.contrib import  messages
from datetime import datetime
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        print("HELLO")
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        if request.POST['canSMS'] == "on":
            canSMS = True
        else:
            canSMS = False
        subject = request.POST['subject']
        message = request.POST['msg']
        contact_date = datetime.now()

        contact = Contact(user_id=user_id,
                          name=name,
                          email=email,
                          phone=phone,
                          canSMS=canSMS,
                          subject=subject,
                          message=message,
                          contact_date=contact_date)
        contact.save()

        messages.success(request, "Message submitted; we will contact you soon.")

        return redirect('index')
