# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
class SearchView(models.Model):
    a_id = models.IntegerField()
    acc = models.CharField(primary_key=True, max_length=255)
    acode = models.CharField(max_length=255,blank=False)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    kingdom = models.CharField(max_length=255, blank=True)
    phylum = models.CharField(max_length=255, blank=True)
    taxclass = models.CharField(max_length=255, blank=True)
    taxorder = models.CharField(max_length=255, blank=True)
    family = models.CharField(max_length=255, blank=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    forma = models.CharField(max_length=255, blank=True)
    elcode = models.CharField(max_length=255, blank=True)
    gelcode = models.IntegerField(blank=True, null=True)
    iunccode = models.CharField(max_length=255, blank=True)
    g_rank = models.CharField(max_length=255, blank=True)
    s_rank = models.CharField(max_length=255, blank=True)
    nativity = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    c_id = models.IntegerField()
    vernacularname = models.CharField(max_length=255, blank=True)
    
    class Meta:
        managed = False
        db_table = 'search_view'
        ordering = ['acode']

class Acctax(models.Model):
    a_id = models.IntegerField()
    acode = models.CharField(primary_key=True, max_length=255)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    kingdom = models.CharField(max_length=255, blank=True)
    phylum = models.CharField(max_length=255, blank=True)
    taxclass = models.CharField(max_length=255, blank=True)
    taxorder = models.CharField(max_length=255, blank=True)
    family = models.CharField(max_length=255, blank=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    forma = models.CharField(max_length=255, blank=True)
    elcode = models.CharField(max_length=255, blank=True)
    gelcode = models.IntegerField(blank=True, null=True)
    iunccode = models.CharField(max_length=255, blank=True)
    g_rank = models.CharField(max_length=255, blank=True)
    s_rank = models.CharField(max_length=255, blank=True)
    nativity = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'acctax'
        ordering = ['-a_id']

class Comtax(models.Model):
    c_id = models.IntegerField(primary_key=True)
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    vernacularname = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'comtax'

class Syntax(models.Model):
    s_id = models.IntegerField()
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    scode = models.CharField(primary_key=True, max_length=255)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    family = models.CharField(max_length=255, blank=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'syntax'

