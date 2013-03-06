from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=256, null=True)
    line1 = models.CharField(max_length=256)
    line2 = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=8)
    country = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return "{0}\n{1}\n{2}\n{3}, {4}\n{5}\n{6}".format(self.name, self.line1, self.line2, self.city, self.state, self.zip, self.country)
    