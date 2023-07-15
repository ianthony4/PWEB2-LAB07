from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django.core.mail import send_mail
from django.http import HttpResponse

def enviar_correo(request):
    subject = 'Hola desde Django'
    message = 'Este es un ejemplo de envío de correo desde Django.'
    from_email = 'anthonyleo2001@gmail.com'
    recipient_list = ['wosoke8405@kameili.com']
    
    send_mail(subject, message, from_email, recipient_list)
    
    return HttpResponse('<h1>Correo enviado</h1>')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id":7,
            "customer_name": "Anthony Chaisa Fernandez",
            "amount":21,
            "today":"14/07/23", 
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
#    def generate_view(self, request, *args, **kwargs):
#        template = get_template('invoice.html')
#        context = {
#            "invoice_id":123,
#            "customer_name": "Anthony Chaisa",
#            "amount":1399.99,
#            "today":"Today", 
#        }
#        html = template.render(context)
#        return HttpResponse(html)



