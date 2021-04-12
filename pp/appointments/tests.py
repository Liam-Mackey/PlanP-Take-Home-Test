import requests
import json
import datetime
from django.test import TestCase
from .models import Appointment

class AppointmentTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_appointments(self):
        response = requests.get('http://localhost:8000/api/v1/appointments/')
        data = response.json()
        self.assertTrue(len(json.loads(data)) > 0)


    def test_create_appointment(self):
        headers = {"Content-Type": "application/json"}
        post_data = {
            "datetime": str(datetime.datetime.now()),
            "reason": "NP",
            "new_patient": True,
            "contact_phone_number": "(987)908-3451"
        }
        response = requests.post("http://localhost:8000/api/v1/appointments/", json=post_data, headers=headers)
        print(response)
        data = response.json()
        self.assertEquals(json.loads(data)['contact_phone_number'], "(987)908-3451")

    def test_delete_appointment(self):
        response = requests.delete('http://localhost:8000/api/v1/appointments/' + pk + '/')
        self.assertEquals(response.status_code, 200)

    def test_get_appointment_by_pk(self):
        response = requests.get('http://localhost:8000/api/v1/appointments/' + pk + '/')
        data = response.json()
        self.assertTrue(json.loads(data)['contact_phone_number'], "(987)908-3451")