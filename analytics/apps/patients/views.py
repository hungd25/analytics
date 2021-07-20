from django.http import JsonResponse
from django.db.models import Min, Max, Avg, Count
from analytics.apps.patients.models import Patient
from django.core.serializers import serialize


def query(request):
    """
    mininum clinical event value, grouped by patient and event type
    maximum clinical event value, grouped by patient and event type
    average clinical event value, grouped by patient and event type
    count of clinical events, grouped by patient and event type
    time of earliest clinical event, grouped by patient and event type
    time of latest clinical event, grouped by patient and event type
    """
    event_stats = Patient.objects.values('PATIENT_ID', 'EVENT_TYPE').annotate(MIN_VALUE=Min('EVENT_VALUE'),
                                                                              MAX_VALUE=Max('EVENT_VALUE'),
                                                                              AVG_VALUE=Avg('EVENT_VALUE'),
                                                                              COUNT_EVENTS=Count('EVENT_VALUE'))
    event_stats = list(event_stats)
    latest_event = Patient.objects.values('PATIENT_ID', 'EVENT_TYPE').latest()
    earliest_event = Patient.objects.values('PATIENT_ID', 'EVENT_TYPE').earliest()
    event_stats.append({'LATEST_EVENT': latest_event, 'EARLIEST_EVENT': earliest_event})
    data = {'EVENT_STATS': event_stats}

    return JsonResponse(data, json_dumps_params=dict(indent=4, sort_keys=True))
