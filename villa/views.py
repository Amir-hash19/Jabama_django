from django.http import HttpResponse


def villa_letter(request):
    return HttpResponse("this is villa page !")