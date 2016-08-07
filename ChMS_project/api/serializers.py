from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.reverse import reverse

from .models import Church, Person, Interest, SkillAndProfession,\
    SpiritualMilestone, Ministry, MemberStatus


class ChurchSerializer(serializers.ModelSerializer):

    church_type_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Church
        fields = ('id', 'name', 'church_type',
                  'church_type_display', 'vision', 'logo', 'banner', 'links')

    def get_church_type_display(self, obj):
        return obj.get_church_type_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('church-detail', kwargs={'pk': obj.pk}, request=request),
        }

    def validate_church_type(self, value):
        """
        Check that only Daughter Churches are allowed to be created
        """
        if value == 'M':
            raise serializers.ValidationError(
                "Only Daughter churches are allowed to be created.")
        return value


class PersonSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()
    marital_status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'middle_initial', 'last_name', 'gender',
                  'gender_display', 'marital_status', 'marital_status_display',
                  'is_born_again_christian', 'alternate_email_address',
                  'church', 'links',)

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_marital_status_display(self, obj):
        return obj.get_marital_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'church': reverse('church-detail',
                              kwargs={'pk': obj.church_id},
                              request=request),
        }


class InterestSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Interest
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('interest-detail', kwargs={'pk': obj.pk}, request=request),
        }


class SkillAndProfessionSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = SkillAndProfession
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('skill-detail', kwargs={'pk': obj.pk}, request=request),
        }


class SpiritualMilestoneSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = SpiritualMilestone
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('spiritual_milestone-detail', kwargs={'pk': obj.pk}, request=request),
        }


class MinistrySerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Ministry
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('ministry-detail', kwargs={'pk': obj.pk}, request=request),
        }


class MemberStatusSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = MemberStatus
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('member_status-detail', kwargs={'pk': obj.pk}, request=request),
        }
