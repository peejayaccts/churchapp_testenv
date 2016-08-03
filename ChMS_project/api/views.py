from django.shortcuts import render

from rest_framework import authentication, permissions, viewsets, filters, mixins

from .models import Church, Person, Interest, SkillAndProfession, \
    SpiritualMilestone
from .serializers import ChurchSerializer, PersonSerializer
from .serializers import InterestSerializer, SkillAndProfessionSerializer, \
    SpiritualMilestoneSerializer
from .forms import PersonFilter


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
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class ChurchViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API Endpoint for listing and creating daughter churches"""
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    search_fields = ('church_name', )
    ordering_fields = ('church_name', 'church_type', )


class PersonViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API Endpoint for listing and creating daughter churches"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter
    search_fields = ('first_name', 'last_name',)
    ordering_fields = ('first_name', 'last_name', )


class InterestViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, updating, deleting Interest List
    """

    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', )


class SkillAndProfessionViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, updating, deleting Skills and Professions List
    """

    queryset = SkillAndProfession.objects.all()
    serializer_class = SkillAndProfessionSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', )


class SpiritualMilestoneViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, updating, deleting Spiritual Milestones List
    """

    queryset = SpiritualMilestone.objects.all()
    serializer_class = SpiritualMilestoneSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', )
