from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Newsletter, Subscriber
from .forms import NewsletterForm, SubscriberForm, EmailForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


    
def index(request):
	newsletters = Newsletter.objects.all()
	return render(request, 'index.html', {'newsletters': newsletters})

@login_required
def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.owner = request.user
            newsletter.save()
            return redirect('newsletter_dashboard')
    else:
        form = NewsletterForm()
    return render(request, 'create_newsletter.html', {'form': form})
    

def add_subscriber(request, pk):
    newsletter = get_object_or_404(Newsletter, id=pk)
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber, created = Subscriber.objects.get_or_create(email=form.cleaned_data['email'])
            subscriber.newsletters.add(newsletter)
            return redirect('newsletter_home') 
    else:
        form = SubscriberForm()
    return render(request, 'add_subscriber.html', {'form': form, 'newsletter': newsletter})

@login_required
def send_newsletter(request, newsletter_id):
    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)
    subscribers = newsletter.subscribers.all()
    email_list = [subscriber.email for subscriber in subscribers]

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            html_message = render_to_string('email_template.html', {'message': message, 'newsletter': newsletter})
            plain_message = message

            # Set the from_email to include the sender's name and email
            from_email = f"<{newsletter.sender_email}>"

            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=from_email,
                to=email_list
            )
            email.attach_alternative(html_message, "text/html")
            email.send(fail_silently=False)

            return redirect('newsletter_dashboard')
    else:
        form = EmailForm()

    return render(request, 'send_newsletter.html', {'form': form, 'newsletter': newsletter})
    
    
def newsletter_dashboard(request):
	return render(request, 'newsletter_dashboard.html', {})