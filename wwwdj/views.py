from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render

from wwwdj.forms import ContactForm

def home(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      obj = form.save()
      mail_subject = '%s %s, %s' % (obj.first_name, obj.last_name, obj.date),
      mail_message = render_to_string('partials/email.html', {
        'message': obj.message,
        'first_name': obj.first_name,
        'last_name': obj.last_name,
        'phone': obj.phone,
        'email': obj.email,
      })
      mail_recipient = ['alexheist@mycwi.cc']
      email = EmailMessage(
        mail_subject, mail_message, to=[mail_recipient]
      )
      email.send()
      form = ContactForm()
  else:
    form = ContactForm()
  context = {
    'form': form,
  }
  return render(request, 'home.html', context)
