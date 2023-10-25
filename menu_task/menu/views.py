from django.shortcuts import render


# Create your views here.
def index(request, test):
    return render(request, 'base.html')


def test_url(request):
    return render(request, 'base.html')