from django.db import models

# Create your models here.
class yearly_temperature(models.Model):
    year = models.IntegerField()
    jan_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    feb_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    mar_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    apr_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    may_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    jun_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    jul_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    aug_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    sep_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    oct_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    nov_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    dec_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    win_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    spr_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    sum_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    aut_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    ann_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0)

