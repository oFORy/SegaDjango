from django.db import models


class Countries(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Name = models.TextField(db_column='Name')  # Field name made lowercase.

    def __str__(self):
        return str(self.Name)

    class Meta:
        managed = False
        db_table = 'Countries'
        ordering = ['Id']


class Currencies(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label')  # Field name made lowercase.
    shortlabel = models.TextField(db_column='ShortLabel')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    walletnumber = models.TextField(db_column='WalletNumber')  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl')  # Field name made lowercase.

    def __str__(self):
        return str(self.shortlabel)

    class Meta:
        managed = False
        db_table = 'Currencies'
        ordering = ['Id']


class Currencycountry(models.Model):
    countriesid = models.ManyToManyField(Countries, db_column='CountriesId')
    currencyid = models.ManyToManyField(Currencies, db_column='CurrencyId')

    class Meta:
        managed = False
        db_table = 'CurrencyCountry'


class Histories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    username = models.TextField(db_column='UserName')  # Field name made lowercase.
    userlogin = models.TextField(db_column='UserLogin')  # Field name made lowercase.
    idcurrency = models.IntegerField(db_column='IdCurrency')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    actiontype = models.IntegerField(db_column='ActionType')  # Field name made lowercase.
    idcountry = models.IntegerField(db_column='IdCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Histories'