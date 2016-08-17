
from datetime import date
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.reverse import reverse

from .models import Church, Person, Interest, SkillAndProfession,\
    SpiritualMilestone, Ministry, MemberStatus, ChurchRegionalInfo, \
    ContactInfo, ResidentialAddress, MailAddress


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
                  'vision', 'logo', 'banner', 'max_mentees_mentor',
                  'max_subgroup_person', 'max_subgroup_members', 'regional_info',
                  'links')

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
        instance.max_mentees_mentor = validated_data.get(
            'max_mentees_mentor', instance.max_mentees_mentor)
        instance.max_subgroup_person = validated_data.get(
            'max_subgroup_person', instance.max_subgroup_person)
        instance.max_subgroup_members = validated_data.get(
            'max_subgroup_members', instance.max_subgroup_members)
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


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = ('primary_contact_num',
                  'other_contact_num', 'alternate_email',)


class ResidentialAddressSerializer(serializers.ModelSerializer):

    latitude = serializers.DecimalField(
        max_digits=9, decimal_places=7, read_only=True)
    longitude = serializers.DecimalField(
        max_digits=10, decimal_places=7, read_only=True)

    class Meta:
        model = ResidentialAddress
        fields = ('street', 'country', 'city', 'zip_post_code', 'state_province',
                  'latitude', 'longitude',)


class MailAddressSerializer(serializers.ModelSerializer):

    latitude = serializers.DecimalField(
        max_digits=9, decimal_places=7, read_only=True)
    longitude = serializers.DecimalField(
        max_digits=10, decimal_places=7, read_only=True)

    class Meta:
        model = MailAddress
        fields = ('street', 'country', 'city', 'zip_post_code', 'state_province',
                  'latitude', 'longitude',)


class PersonSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()
    marital_status_display = serializers.SerializerMethodField()
    age = serializers.IntegerField(read_only=True)
    date_of_birth = serializers.DateField(
        format=settings.DATE_FORMAT, input_formats=settings.DATE_INPUT_FORMATS)
    contact_info = ContactInfoSerializer(required=False, allow_null=True)
    residential_address = ResidentialAddressSerializer(
        required=False, allow_null=True)
    mail_address = MailAddressSerializer(required=False, allow_null=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'middle_initial', 'last_name',
                  'date_of_birth', 'age', 'gender', 'gender_display',
                  'marital_status', 'marital_status_display',
                  'church', 'member_status', 'contact_info',
                  'residential_address', 'mail_address', 'links')

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_marital_status_display(self, obj):
        return obj.get_marital_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('person-detail', kwargs={'pk': obj.pk}, request=request),
        }

    def validate(self, data):
        if data['date_of_birth']:
            dob = data['date_of_birth']
            today = date.today()
            data['age'] = today.year - dob.year - \
                ((today.month, today.day) < (dob.month, dob.day))
        return data

    def create(self, validated_data):
        contact_info_data = validated_data.pop('contact_info')
        residential_address_data = validated_data.pop('residential_address')
        mail_address_data = validated_data.pop('mail_address')
        person_data = Person.objects.create(**validated_data)
        if contact_info_data:
            ContactInfo.objects.create(
                person=person_data, **contact_info_data)
        if residential_address_data:
            ResidentialAddress.objects.create(
                person=person_data, **residential_address_data)
        if mail_address_data:
            MailAddress.objects.create(
                person=person_data, **mail_address_data)
        return person_data

    def update(self, instance, validated_data):
        contact_info_data = validated_data.pop('contact_info')
        residential_address_data = validated_data.pop('residential_address')
        mail_address_data = validated_data.pop('mail_address')
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.middle_initial = validated_data.get(
            'middle_initial', instance.middle_initial)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.date_of_birth = validated_data.get(
            'date_of_birth', instance.date_of_birth)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.marital_status = validated_data.get(
            'marital_status', instance.marital_status)
        instance.church = validated_data.get('church', instance.church)
        instance.member_status = validated_data.get(
            'member_status', instance.member_status)
        instance.save()
        if contact_info_data:
            if hasattr(instance, 'contact_info'):
                contact_info = instance.contact_info
                contact_info.primary_contact_num = contact_info_data.get(
                    'primary_contact_num', contact_info.primary_contact_num)
                contact_info.other_contact_num = contact_info_data.get(
                    'other_contact_num', contact_info.other_contact_num)
                contact_info.alternate_email = contact_info_data.get(
                    'alternate_email', contact_info.alternate_email)
                contact_info.save()
            else:
                instance.contact_info = ContactInfo(
                    person=instance,
                    primary_contact_num=contact_info_data.get(
                        'primary_contact_num'),
                    other_contact_num=contact_info_data.get(
                        'other_contact_num'),
                    alternate_email=contact_info_data.get('alternate_email'))
                instance.contact_info.save()
        if residential_address_data:
            if hasattr(instance, 'residential_address'):
                residential_address = instance.residential_address
                residential_address.street = residential_address_data.get(
                    'street', residential_address.street)
                residential_address.country = residential_address_data.get(
                    'country', residential_address.country)
                residential_address.city = residential_address_data.get(
                    'city', residential_address.city)
                residential_address.zip_post_code = residential_address_data.get(
                    'zip_post_code', residential_address.zip_post_code)
                residential_address.state_province = residential_address_data.get(
                    'state_province', residential_address.state_province)
                residential_address.latitude = residential_address_data.get(
                    'latitude', residential_address.latitude)
                residential_address.longitude = residential_address_data.get(
                    'longitude', residential_address.longitude)
                residential_address.save()
            else:
                instance.residential_address = ResidentialAddress(
                    person=instance,
                    street=residential_address_data.get('street'),
                    country=residential_address_data.get('country'),
                    city=residential_address_data.get('city'),
                    zip_post_code=residential_address_data.get(
                        'zip_post_code'),
                    state_province=residential_address_data.get(
                        'state_province'),
                    latitude=residential_address_data.get('latitude'),
                    longitude=residential_address_data.get('longitude'))
                instance.residential_address.save()
        if mail_address_data:
            if hasattr(instance, 'mail_address'):
                mail_address = instance.mail_address
                mail_address.street = mail_address_data.get(
                    'street', mail_address.street)
                mail_address.country = mail_address_data.get(
                    'country', mail_address.country)
                mail_address.city = mail_address_data.get(
                    'city', mail_address.city)
                mail_address.zip_post_code = mail_address_data.get(
                    'zip_post_code', mail_address.zip_post_code)
                mail_address.state_province = mail_address_data.get(
                    'state_province', mail_address.state_province)
                mail_address.latitude = mail_address_data.get(
                    'latitude', mail_address.latitude)
                mail_address.longitude = mail_address_data.get(
                    'longitude', mail_address.longitude)
                mail_address.save()
            else:
                instance.mail_address = MailAddress(
                    person=instance,
                    street=mail_address_data.get('street'),
                    country=mail_address_data.get('country'),
                    city=mail_address_data.get('city'),
                    zip_post_code=mail_address_data.get(
                        'zip_post_code'),
                    state_province=mail_address_data.get(
                        'state_province'),
                    latitude=mail_address_data.get('latitude'),
                    longitude=mail_address_data.get('longitude'))
                instance.mail_address.save()
        return instance
