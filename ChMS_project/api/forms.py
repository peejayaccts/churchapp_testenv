import django_filters

from .models import PersonInterest


class PersonInterestFilter(django_filters.FilterSet):

    class Meta:
        model = PersonInterest
        fields = ('person', 'interest',)
