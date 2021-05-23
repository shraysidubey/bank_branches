from django.db import models

class Bank(models.Model):
    b_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=49)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank_id = models.ForeignKey(Bank)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)


    def __unicode__(self):
        return self.address