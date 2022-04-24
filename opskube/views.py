from django.http import HttpResponse

def project_view(request):
    return HttpResponse('<div><h1>This is project view</h1><em>Hello from piyush to opskube</em></div>')