from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


def test(request):
    return render(request, 'pages/test.html')