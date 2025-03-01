from django.http import HttpResponse


def apartment_letter(request):
    return HttpResponse("welcome to the apartment page!")

