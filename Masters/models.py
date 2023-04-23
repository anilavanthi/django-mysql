from django.db import models

from django.conf import settings
from Common.utils import getcode
import datetime


class Country(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='countrycreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='countryupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(Country,'COUNTRY')
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class State(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='statescreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='statesupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(State,'STAT')
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, related_name='districts', on_delete=models.RESTRICT, null=True)
    state = models.ForeignKey(State, related_name='districts', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districtscreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districtsupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(District,'DIST')
        super(District, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.RESTRICT, null=True)
    state = models.ForeignKey(State, related_name='cities', on_delete=models.RESTRICT, null=True)
    district = models.ForeignKey(District, related_name='cities', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='citiescreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='citiesupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(City,'CITY')
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"



class Area(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, related_name='areas', on_delete=models.RESTRICT, null=True)
    district = models.ForeignKey(District, related_name='areas', on_delete=models.RESTRICT, null=True)
    state = models.ForeignKey(State, related_name='areas', on_delete=models.RESTRICT, null=True)
    pincode = models.CharField(max_length=10, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='areascreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='areasupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        if self.id is None and (self.code == "" or self.code == None):
            self.code = getcode(Area,'AREA')
        super(Area, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Branch(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address=models.CharField(max_length=300, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='branchcreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='branchupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Branch, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Religion(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='religioncreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='religionupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Religion, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Caste(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='castecreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='casteupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Caste, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubCaste(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    caste = models.ForeignKey(Caste, related_name='subcaste', on_delete=models.RESTRICT, null=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subcastecreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subcasteupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)


    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(State,'STAT')
        super(SubCaste, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Occupation(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='occupationcreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='occupationupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Occupation, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Education(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='educationcreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='educationupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Education, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Language(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='languagecreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='languageupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Source(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sourcecreated', on_delete=models.RESTRICT, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True, auto_now=True)
    modifiedby = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sourceupdated', on_delete=models.RESTRICT,  null=True)
    status = models.SmallIntegerField(default=1, null=True)

    def save(self, *args, **kwargs):
        # if self.id is None and (self.code == "" or self.code == None):
        #     self.code = getcode(Branch,'BRANCH')
        super(Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.name







    


















