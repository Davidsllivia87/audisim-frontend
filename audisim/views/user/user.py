from django.shortcuts import render

def user_index(request):
    return render(request, 'audisim/user/user_base.html')