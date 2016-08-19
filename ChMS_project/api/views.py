from django.shortcuts import render

from rest_framework import authentication, permissions, viewsets, filters, mixins

from .models import Church, Person, Interest, SkillAndProfession, \
    SpiritualMilestone, Ministry, MemberStatus, PersonInterest
from .serializers import ChurchSerializer, PersonSerializer
from .serializers import InterestSerializer, SkillAndProfessionSerializer, \
    SpiritualMilestoneSerializer, MinistrySerializer, MemberStatusSerializer, \
    PersonInterestSerializer
from .forms import PersonInterestFilter


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


class ChurchViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """API Endpoint for listing and creating daughter churches"""
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', 'church_type', )


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


class MinistryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, updating, deleting Ministry List
    """

    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', )


class MemberStatusViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, updating, deleting Member Statuses List
    """

    queryset = MemberStatus.objects.all()
    serializer_class = MemberStatusSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', )
    ordering_fields = ('name', )


class PersonViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """
    API Endpoint for listing and creating daughter churches
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('first_name', 'last_name',)
    ordering_fields = ('first_name', 'last_name', )


class PersonInterestViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    API Endpoint for listing, creating, and deleting maps for Person and Interest
    """

    queryset = PersonInterest.objects.all()
    serializer_class = PersonInterestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PersonInterestFilter
