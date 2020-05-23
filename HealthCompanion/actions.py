from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class GE_API:
    def search(self, institution_type, location):

        Appointment.status = "proposed"
        location.adress['description']

        return [SlotSet("location_institution", Location.Adress['description']), SlotSet("date_and_time", Appointment.start)]

class ActionSearchInstitution(Action):
    def name(self):
        return "action_search_pharmacy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for a pharmacy near you")
        ge_api = GE_API()
        pharmacy = ge_api.search(tracker.get_slot("location_institution"))
        return [SlotSet("location_institution", pharmacy)]

class ActionSearchClinic(Action):
    def name(self):
        return "action_search_doctor"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for a doctor near you")
        ge_api = GE_API()
        clinic = ge_api.search(tracker.get_slot("pharmacy"))
        return [SlotSet("location_institution", clinic)]

class ActionAppointment(Action):
    def name(self):
        return "action_appointment"

    def run(self, date_and_time, contact_name, contact_age, ):
