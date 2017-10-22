"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from dashboard import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()

class OperatingList(core.patient_lists.PatientList):
    display_name = 'Op List'
    queryset = Episode.objects.all().order_by('?')

    #direct_add = False
    schema = [
        models.OpList,
        models.Checklist
    ]
