import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

PeriodChoice = {
    'days':IntervalSchedule.DAYS,
    'hours':IntervalSchedule.HOURS,
    'minutes':IntervalSchedule.MINUTES,
    'seconds':IntervalSchedule.SECONDS,
    'microseconds':IntervalSchedule.MICROSECONDS
    }

class ScheduleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args,**kwargs):
        resolution = request.data.get("resolution")
        firebase_id = request.data.get("firebase_id")
        interval = request.data.get("interval")
        period = PeriodChoice[request.data.get("period")]
        phone_number = request.user.phone
        schedule, _ = IntervalSchedule.objects.get_or_create(every=interval,period=period,)
        PeriodicTask.objects.create(
            interval=schedule,                  
            name=firebase_id,          
            task='backend.celery_settings.schedule', 
            args=json.dumps([resolution,phone_number]),
        )
        return Response({"status":"ok"})

    def delete(self, request, *args,**kwargs):
        firebase_id = request.data.get("firebase_id")
        PeriodicTask.objects.filter(name=firebase_id).delete()
        return Response({"status":"ok"})

    def patch(self, request, *args,**kwargs):
        resolution = request.data.get("resolution")
        firebase_id = request.data.get("firebase_id")
        interval = request.data.get("interval")
        period = PeriodChoice[request.data.get("period")]
        phone_number = request.user.phone
        schedule, _ = IntervalSchedule.objects.get_or_create(every=interval,period=period,)
        PeriodicTask.objects.filter(name=firebase_id).update(
            interval=schedule,
            args=json.dumps([resolution,phone_number]),
        )
        return Response({"status":"ok"})
        
