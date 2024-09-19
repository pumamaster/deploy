from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Photo, Fondo

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(vertical=True).order_by('-id')
        context['fondo'] = Fondo.objects.first()
        return context
    
class Index2(TemplateView):
    template_name = "index2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(vertical=False).order_by('-id')
        context['fondo'] = Fondo.objects.first()
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fondo'] = Fondo.objects.first()
        return context
    
    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        if nombre and correo and asunto and mensaje:
            # Envío de correo a ambas direcciones
            mensaje_correo = f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"
            send_mail(
                asunto,
                mensaje_correo,
                settings.DEFAULT_FROM_EMAIL,  # Desde
                ['alejandrogongis03@thecreativefusion.com', 'lizmendoza773214@thecreativefusion.com','lizmendoza773214@gmail.com','alejandrogongis03@gmail.com'],  # Para: Lista de destinatarios
                fail_silently=False,
            )
            messages.success(request, "Te responderemos a la brevedad")
            return redirect('index')
        else:
            messages.error(request, "Por favor, completa todos los campos.")
            return redirect('index')

        return render(request, self.template_name)
