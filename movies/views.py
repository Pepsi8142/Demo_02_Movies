from argparse import Action
from django.shortcuts import render
from rest_framework import viewsets, request
from .models import MovieData
from .serializers import MovieSerializer
from django.core.paginator import Paginator, EmptyPage

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    paginator = Paginator(queryset, 10)

    def get_queryset(self):
        queryset = MovieData.objects.all()
        super().get_queryset()
        return queryset
    # page = request.GET.get('page')


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='Action')
    serializer_class = MovieSerializer


class UnknownViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='Unknown')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='Comedy')
    serializer_class = MovieSerializer
