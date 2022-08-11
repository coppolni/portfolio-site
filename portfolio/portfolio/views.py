from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import FileResponse, Http404

class HomePage(TemplateView):
    template_name = 'index.html'

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']
            message = request.POST['message']

            data = {
                    'message_name': message_name,
                    'message_email': message_email,
                    'message': message
            }
            message = '''
            From: {}

            Email: {}

            New Message: {}
            '''.format(data['message_name'], data['message_email'], data['message'])
            send_mail(data['message_name'], message, message_email, ['nick.coppola2010@gmail.com'])

            return render(request, 'thanks.html', {'message_name': message_name})

        else:
            return render(request, 'index.html', {})

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class AttributionsPage(TemplateView):
    template_name = 'attributions.html'
