from django.db import models

# Create your models here.

class StatesTurnouts(models.Model):
    StateName = models.Charfield (max_length = 250)
    Ballots=models.PositiveIntegerField(primary_key=True, validators = [MaxValueValidator(9999999999)])
    VEP=models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    VAP=models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    VCP=models.IntegerField(max_length=200)

class StatesDemographic (models.Model):
    StateName= models.Charfield(max_length = 250)
    Male = models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    Female = models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    WhiteAmerican= models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    AfricanAmerican=models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    Education= models.DecimalField(max_digits=4,decimal_places=1)
