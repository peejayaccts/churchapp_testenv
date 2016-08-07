from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.reverse import reverse

from .models import Church, Person, Interest, SkillAndProfession,\
    SpiritualMilestone, Ministry, MemberStatus, ChurchRegionalInfo


class ChurchRegionalInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChurchRegionalInfo
        fields = ('date_format', 'timezone', 'language',
                  'country', 'state_province', 'city', 'zip_post_code')


class ChurchSerializer(serializers.ModelSerializer):

    church_type_display = serializers.SerializerMethodField()
    # regional_info = serializers.PrimaryKeyRelatedField(
    #    read_only=True, allow_null=True)
    regional_info = ChurchRegionalInfoSerializer(
        required=False, allow_null=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = Church
        fields = ('id', 'name', 'church_type', 'church_type_display',
                  'vision', 'logo', 'banner', 'regional_info', 'links')

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

    def create(self, validated_data):
        church_regional_info_data = validated_data.pop('regional_info')
        church_data = Church.objects.create(**validated_data)
        if church_regional_info_data:
            ChurchRegionalInfo.objects.create(
                church=church_data, **church_regional_info_data)
        return church_data

    def update(self, instance, validated_data):
        regional_info_data = validated_data.pop('regional_info')
        instance.name = validated_data.get('name', instance.name)
        instance.vision = validated_data.get('vision', instance.vision)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.banner = validated_data.get('banner', instance.banner)
        instance.save()
        if regional_info_data:
            if hasattr(instance, 'regional_info'):
                regional_info = instance.regional_info
                regional_info.date_format = regional_info_data.get(
                    'date_format', regional_info.date_format)
                regional_info.timezone = regional_info_data.get(
                    'timezone', regional_info.timezone)
                regional_info.language = regional_info_data.get(
                    'language', regional_info.language)
                regional_info.country = regional_info_data.get(
                    'country', regional_info.country)
                regional_info.state_province = regional_info_data.get(
                    'state_province', regional_info.state_province)
                regional_info.city = regional_info_data.get(
                    'city', regional_info.city)
                regional_info.zip_post_code = regional_info_data.get(
                    'zip_post_code', regional_info.zip_post_code)
                regional_info.save()
            else:
                instance.regional_info = ChurchRegionalInfo(
                    church=instance,
                    date_format=regional_info_data.get('date_format'),
                    timezone=regional_info_data.get('timezone'),
                    language=regional_info_data.get('language'),
                    country=regional_info_data.get('country'),
                    state_province=regional_info_data.get('state_province'),
                    city=regional_info_data.get('city'),
                    zip_post_code=regional_info_data.get('zip_post_code'))
                instance.regional_info.save()
        return instance


class PersonSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()
    marital_status_display = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'middle_initial', 'last_name', 'gender',
                  'gender_display', 'marital_status', 'marital_status_display',
                  'is_born_again_christian', 'alternate_email_address',)

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_marital_status_display(self, obj):
        return obj.get_marital_status_display()


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
