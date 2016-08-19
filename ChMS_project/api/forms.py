import django_filters

from .models import PersonInterest, PersonSkillAndProfession


class PersonInterestFilter(django_filters.FilterSet):

    class Meta:
        model = PersonInterest
        fields = ('person', 'interest',)


class PersonSkillAndProfessionFilter(django_filters.FilterSet):

    class Meta:
        model = PersonSkillAndProfession
        fields = ('person', 'skill_and_profession',)
