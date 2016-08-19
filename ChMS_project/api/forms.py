import django_filters

from .models import PersonInterest, PersonSkillAndProfession, \
    PersonSpiritualMilestone


class PersonInterestFilter(django_filters.FilterSet):

    class Meta:
        model = PersonInterest
        fields = ('person', 'interest',)


class PersonSkillAndProfessionFilter(django_filters.FilterSet):

    class Meta:
        model = PersonSkillAndProfession
        fields = ('person', 'skill_and_profession',)


class PersonSpiritualMilestoneFilter(django_filters.FilterSet):

    class Meta:
        model = PersonSpiritualMilestone
        fields = ('person', 'spiritual_milestone',)
