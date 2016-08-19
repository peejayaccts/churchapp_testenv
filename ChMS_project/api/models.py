from django.db import models

from django.utils.translation import ugettext_lazy as _


class Church(models.Model):
    """
    Main or Daughter Church of the Church Management Application.
    """
    CHURCH_TYPE_MAIN = 'M'
    CHURCH_TYPE_DAUGHTER = 'D'
    CHURCH_TYPE_CHOICES = (
        (CHURCH_TYPE_MAIN, _('Main')),
        (CHURCH_TYPE_DAUGHTER, _('Daughter')),
    )
    name = models.CharField(max_length=255, unique=True, blank=False)
    church_type = models.CharField(
        max_length=1, choices=CHURCH_TYPE_CHOICES, default=CHURCH_TYPE_DAUGHTER)
    vision = models.CharField(max_length=255, blank=True)
    logo = models.CharField(max_length=255, blank=True)
    banner = models.CharField(max_length=255, blank=True)
    max_mentees_mentor = models.IntegerField(blank=False, default=2)
    max_subgroup_person = models.IntegerField(blank=False, default=3)
    max_subgroup_members = models.IntegerField(blank=False, default=12)

    def __str__(self):
        return self.name


class ChurchRegionalInfo(models.Model):
    """
    Regional Information for Main or Daughter Church.
    """
    church = models.OneToOneField(Church,
                                  on_delete=models.CASCADE,
                                  primary_key=True,
                                  related_name='regional_info')
    date_format = models.CharField(max_length=255, blank=False)
    timezone = models.CharField(max_length=255, blank=False)
    language = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    state_province = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=True)
    zip_post_code = models.IntegerField(blank=False)

    def __str__(self):
        return self.date_format + ' ' + self.timezone


class Interest(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return (self.name.title())


class SkillAndProfession(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return (self.name.title())


class SpiritualMilestone(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return (self.name.title())


class Ministry(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return (self.name.title())


class MemberStatus(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return (self.name.title())


class Person(models.Model):
    """
    A User of the Church Management Application.
    This includes, System Administrator, Senior Pastor, Super User, Member, etc.
    """
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )
    MARITAL_STATUS_SINGLE = 'S'
    MARITAL_STATUS_MARRIED = 'M'
    MARITAL_STATUS_CHOICES = (
        (MARITAL_STATUS_SINGLE, _('Single')),
        (MARITAL_STATUS_MARRIED, _('Married')),
    )

    first_name = models.CharField(max_length=255, blank=False)
    middle_initial = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField(blank=False)
    age = models.IntegerField(blank=False)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE)
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_STATUS_CHOICES, default=MARITAL_STATUS_SINGLE)
    church = models.ForeignKey(Church, blank=False, null=False)
    member_status = models.ForeignKey(
        MemberStatus, blank=False, null=False)

    def __str__(self):
        return (self.first_name + ' ' + self.middle_initial + ' ' +
                self.last_name)


class ContactInfo(models.Model):
    """
    Contact Information for Person.
    """
    person = models.OneToOneField(Person,
                                  on_delete=models.CASCADE,
                                  primary_key=True,
                                  related_name='contact_info')
    primary_contact_num = models.CharField(max_length=255, blank=False)
    other_contact_num = models.CharField(max_length=255, blank=True, null=True)
    alternate_email = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.person + ' ' + self.primary_contact_num


class ResidentialAddress(models.Model):
    """
    Residential Address of Person.
    """
    person = models.OneToOneField(Person,
                                  on_delete=models.CASCADE,
                                  primary_key=True,
                                  related_name='residential_address')
    street = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    zip_post_code = models.PositiveIntegerField(blank=False)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, blank=True, null=True)

    def __str__(self):
        return self.person + ' ' + self.street + ' ' + self.country


class MailAddress(models.Model):
    """
    Mail Address of Person.
    """
    person = models.OneToOneField(Person,
                                  on_delete=models.CASCADE,
                                  primary_key=True,
                                  related_name='mail_address')
    street = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    zip_post_code = models.PositiveIntegerField(blank=False)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, blank=True, null=True)

    def __str__(self):
        return self.person + ' ' + self.street + ' ' + self.country


class PersonInterest(models.Model):
    """
    Mapping of Interests and People
    """
    person = models.ForeignKey(Person, blank=False, null=False)
    interest = models.ForeignKey(Interest, blank=False, null=False)

    def __str__(self):
        return (self.person + ' ' + self.Interest)
