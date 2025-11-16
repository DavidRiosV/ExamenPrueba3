from django.shortcuts import render
from django.db.models import Q,Prefetch,Sum


def index(request):
    return render(request, 'Examen/index.html')

#------------------------------------------------------------------------------------------

# Errores
def mi_error_404(request,exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'errors/400.html', None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errors/403.html', None,None,403)

def mi_error_500(request):
    return render(request, 'errors/500.html', None,None,500)