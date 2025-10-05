from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate,login
from django.views.generic import View
#For rest framework 
from rest_framework import viewsets
from .serializers import CollectionSerializer, PieceSerializer

class index(generic.ListView):
    template_name = "genre/genretemplate.html"

    def get_queryset(self):
        return Collection.objects.all() 

class details(generic.DetailView):
    model = Collection
    template_name = "genre/detailtemplate.html"

class UserFormView(View):
    form_class=UserForm
    template_name="genre/formtemplate.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.save()
            user.set_password(password)
            user.save()

            newuser = authenticate(username=username, password=password)
            if newuser is not None:
                if newuser.is_active:
                    login(request,newuser)
                    return redirect("/genre")

        return render(request, self.template_name, {'form': form})
    
class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer


    