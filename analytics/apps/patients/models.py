from django.db import models


# TODO: create your models here.
#PATIENT ID,PATIENT NAME,EVENT TYPE,EVENT VALUE,EVENT UNIT,EVENT TIME
#1,Jane,HR,82,beats/minute,2021-07-07T02:27:00Z

class Patient(models.Model):
    PATIENT_ID = models.IntegerField()
    PATIENT_NAME = models.CharField(max_length=200)
    EVENT_TYPE = models.CharField(max_length=100)
    EVENT_VALUE = models.IntegerField()
    EVENT_UNIT = models.CharField(max_length=100)
    EVENT_TIME = models.DateTimeField()

    class Meta:
        get_latest_by = 'EVENT_TIME'
