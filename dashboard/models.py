"""
dashboard models.
"""
from django.db.models import fields
from django.db import models as db_models

from opal import models
from opal.core import fields
from opal.core import lookuplists

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

class Checklist(models.EpisodeSubrecord):
    _is_singleton = True

    consented = db_models.IntegerField(default = 0 )
    equipment = db_models.IntegerField(default = 0 )
    blood     = db_models.IntegerField(default = 0 )
    seen_by_anaes = db_models.IntegerField(default = 0 )
    ward_ready = db_models.IntegerField(default = 0 )
    surg_available = db_models.IntegerField(default = 0)
    porter_sent = db_models.DateTimeField(blank = True, null = True)
    gone_collect = db_models.DateTimeField(blank = True, null = True)
    ready_code = db_models.IntegerField(default=0)
    op_ID = db_models.IntegerField
    #ITUBED

class OpList(models.EpisodeSubrecord):
    _is_singleton = True
    
    op_ID = db_models.IntegerField (null=True)
    order = db_models.IntegerField (null = True)
    Pat_ID = db_models.IntegerField (null=True)
    est_surg_time = db_models.IntegerField (default = 60)
    est_anaes_time = db_models.IntegerField (default = 15)
    SNOMED = db_models.CharField(max_length=255)
    ready = db_models.IntegerField(default = 0 )

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""
