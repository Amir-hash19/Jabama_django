from django.http import HttpResponse


def cottage_letter(request):
    return HttpResponse ("this is cottage page!")
