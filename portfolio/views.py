from django.shortcuts import render

# from django.shortcuts import render, redirect
# from .forms import ContactForm
# from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render(request, 'contact.html')



# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})
