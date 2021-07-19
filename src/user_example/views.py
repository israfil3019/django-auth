from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "user_example/home.html")

@login_required
def special(request):
    return render(request, "user_example/special.html")