from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class GE_API:
    def search(self, institution_type, contact_location):
        
        app_start = "ExampleAvailableTimeSlot"  #Appointment.start
        app_status = "ExampleAppointmentStatus" #Appointment.status
        app_patient_status = "ExampleAccepted" #Appointment.patient.status
        
        if institution_type= "pharmacy":
            loc = "Example Pharmacy Adress"     #location.adress['description']
                                                #Appointment.status = "proposed"
        else:  
            loc = "Example Clinic or Hospital Adress"        

        return [SlotSet("location_institution", loc), SlotSet("date", app_start)]

class ActionSearchPharmacy(Action):
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
        
        
        
class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("contact_name")
        #shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("contact_name"), None)
        dispatcher.utter_message(text="hey ")
        dispatcher.utter_message(text=name_entity)
        dispatcher.utter_message(text=", we are friends already")
        return []        
