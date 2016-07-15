from django.shortcuts import render

from rest_framework import authentication, permissions, viewsets, filters

from .models import Church, Person
from .serializers import ChurchSerializer, PersonSerializer


class DefaultsMixin(object):
    """
    Default settings for view authentication, permissions,
    filtering and pagination.
    """
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.SearchFilter,
    )


class ChurchViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API Endpoint for listing and creating daughter churches"""
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    search_fields = ('church_name', )


class PersonViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API Endpoint for listing and creating daughter churches"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    search_fields = ('first_name', 'last_name',)
