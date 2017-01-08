from django.shortcuts import render

def client_index(request):
    return render(request, 'audisim/client/client_base.html')