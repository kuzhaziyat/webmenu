from django.http import HttpResponse


def menuView(request):
    return HttpResponse('Hello, World!')