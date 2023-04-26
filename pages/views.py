from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Docteur

def hello(request):
    docteurs = Docteur.objects.all()
    return render(request, 'pages/hello.html',
                  {'doct' : docteurs})

def index(request):
    docteurs = Docteur.objects.all()
    return render(request, 'pages/index.html',
                  {'doct' : docteurs})

#def hello(request):
 #   docteurs = Docteur.objects.all()
  #  return HttpResponse(f"""
   #     <html>
    #        <head><title>Merchex</title><head>
    #        <body>
     #       <h1>Hello Django !</h1>
      #      <p>Mes groupes préférés sont :<p>
       # <ul>
        #    <li>{docteurs[0].name}</li>
        #    <li>{docteurs[1].name}</li>
        #    <li>{docteurs[2].name}</li>
        #    <li>{docteurs[3].name}</li>
       # </ul>
       #  </body>
        #</html>
    #""")

def about(request):
    return HttpResponse('<h1> A propos de nous!</h1> <p> On programme en python ici</p>')

