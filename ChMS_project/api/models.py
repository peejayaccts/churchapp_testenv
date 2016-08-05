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

    def __str__(self):
        return self.name


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
    middle_initial = models.CharField(max_length=1, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE)
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_STATUS_CHOICES, default=MARITAL_STATUS_SINGLE)
    is_born_again_christian = models.BooleanField()
    alternate_email_address = models.CharField(
        max_length=250, blank=True, default='')
    church = models.ForeignKey(Church, blank=False, null=False)

    def __str__(self):
        return (self.first_name + ' ' + self.middle_initial + ' ' +
                self.last_name)


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
