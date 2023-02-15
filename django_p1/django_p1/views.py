from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse('404: Page not Found! WAH!')

def page404(request):
    return HttpResponseNotFound("404, maybe?")