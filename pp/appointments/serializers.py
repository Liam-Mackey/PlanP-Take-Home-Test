from django.forms.models import model_to_dict
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    datetime = serializers.DateTimeField(required=True)
    reason = serializers.CharField(required=True)
    new_patient = serializers.BooleanField(required=True)
    contact_phone_number = serializers.CharField()

    class Meta:
        model = Appointment
        fields = ("id", "datetime", "reason", "new_patient", "contact_phone_number")

    def create(self, data):
        appointment = Appointment()
        appointment.datetime = data.get('datetime')
        appointment.reason = data.get('reason')
        appointment.new_patient = data.get('new_patient')
        appointment.contact_phone_number = data.get('contact_phone_number')
        appointment.save()
        return model_to_dict(appointment)   

    def update(self, instance, data):
        instance.datetime = data.get('datetime', instance.datetime)
        instance.reason = data.get('reason', instance.reason)
        instance.new_patient = data.get('new_patient', instance.new_patient)
        instance.contact_phone_number = data.get('contact_phone_number', instance.contact_phone_number)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return None