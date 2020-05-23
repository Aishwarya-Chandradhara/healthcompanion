from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class GE_API:
    def search(self, institution_type, institution_location, contact_location, time=None, date=None, ):
        
        appointment_time = time  #Appointment.start
        appointment_status = "pending" #Appointment.status
        
        if institution_type= "pharmacy":
            # suggest a pharmacy in the proximity to contact_location
            institution_name = "City Pharmacy"
            appointment_status = "not needed"
            institution_address = "City Strasse, Paderborn"
            institution_phone = "12323457890"
            return [SlotSet("institution_name", institution_name), SlotSet("institution_address", institution_address), SlotSet("institution_phone", institution_phone), SlotSet("appointment_status", appointment_status)]
        else:
            # for all other institutions
            institution_name = "City Hospital"
            appointment_status = "pending"
            institution_address = "City Strasse, Paderborn"
            institution_phone = "12332227890"
            return [SlotSet("institution_name", institution_name), SlotSet("institution_address", institution_address), SlotSet("institution_phone", institution_phone), SlotSet("appointment_status", appointment_status)]

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

    def run(self, dispatcher, tracker, domain)-> List[EventType]:
        
class ActionAnalyseSymptoms(Action):
    def name(self):
        return "action_analyse_symptoms"
    
    def run(self, dispatcher, tracker, domain)-> List[EventType]:
        # symptom1 = tracker.get_latest_entity_values("symptom1")
        # symptom2 = tracker.get_latest_entity_values("symptom2")
        # symptom3 = tracker.get_latest_entity_values("symptom3")
        # analysis_inputs = [symptom1, symptom2, symptom3]
        # outputs = analysis_tool(analysis_inputs)
        output = "mild cold"
        dispatcher.utter_messege(text = "well,")
        dispatcher.utter_messege(text = tracker.get_latest_entity_values("contact_name"))
        dispatcher.utter_messege(text = "you might have")
        dispatcher.utter_messege(text = output)
        dispatcher.utter_messege(text = "However, we still highly recommend that you go visit a specialist. As we are not legally allowed to give diagnoses."
        return []
                                 
class ActionGreetUser(Action):
    """Greets the user using his name"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("contact_name")
        name_entity = next(tracker.get_latest_entity_values("contact_name"), None)
        dispatcher.utter_message(text="hey ")
        dispatcher.utter_message(text=name_entity)
        dispatcher.utter_message(text=", we are friends already")
        return []        
