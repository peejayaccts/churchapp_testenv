from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Church, Person


class ChurchSerializer(serializers.ModelSerializer):
    church_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Church
        fields = ('id', 'church_name', 'church_type', 'church_type_display',
                  'logo_path', 'vision', 'language_format', 'timezone_format',)

    def get_church_type_display(self, obj):
        return obj.get_church_type_display()


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
