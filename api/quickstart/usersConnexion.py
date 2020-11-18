from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def connexion(request):
    if request.method == 'POST':
        user = Person.objects.raw('SELECT * FROM UsersApi WHERE matricule  =' + request.POST.get("matricule") +' AND motDePasse  =' +request.POST.get("motDePasse"))
        if user is not None:
          print("ok")
        else:
          print("ko")
