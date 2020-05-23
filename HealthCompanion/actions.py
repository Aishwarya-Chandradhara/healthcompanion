from rasa_sdk import Action
from rasa_sdk.events import SlotSet


def search(institution_type, contact_location):
    """
    Suggest a pharmacy in the proximity to contact_location
    :param institution_type:
    :param contact_location:
    :return:
    """
    if institution_type == "pharmacy":
        institution_name = "City Pharmacy"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12323457890"
        return [SlotSet("institution_name", institution_name),
                SlotSet("institution_address", institution_address),
                SlotSet("institution_phone", institution_phone)]
    else:
        # for all other institutions
        institution_name = "City Hospital"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12332227890"
        return [SlotSet("institution_name", institution_name),
                SlotSet("institution_address", institution_address),
                SlotSet("institution_phone", institution_phone)]


def make_appointment(institution_name, contact_name, contact_age, contact_phone, contact_gender, date, time):
    """
    Make appointment in the given hospital for the contact.
    :param institution_name:
    :param contact_name:
    :param contact_age:
    :param contact_phone:
    :param contact_gender:
    :param date:
    :param time:
    :return:
    """
    appointment_status = "pending"

    # make a call to some API to actually book the appointment.
    return [SlotSet("institution_name", appointment_status)]


def diagnose_symptoms(symptom1, symptom2=None, symptom3=None, allergies=None):
    """
    Diagnose symptoms and suggest what might be wrong
    :param symptom1:
    :param symptom2:
    :param symptom3:
    :param allergies:
    :return:
    """
    # symptom1 can't be empty or None
    flu_symptoms = [None, "Headache", "Fever", "Chills", "Cough", "Sore Throat", "Runny Nose", "Fatigue"]
    diarrhea_symptoms = [None, "Nausea", "Bloating", "Loose stools", "Abdominal pain", "Abdominal cramps"]

    if symptom1 in flu_symptoms and symptom2 in flu_symptoms and symptom3 in flu_symptoms:
        diagnosis_results = "Looks like Flu to me"
    if symptom1 in diarrhea_symptoms and symptom2 in diarrhea_symptoms and symptom3 in diarrhea_symptoms:
        diagnosis_results = "It looks like you have got Diarrhea"

    return [SlotSet("diagnosis_results", diagnosis_results)]


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

    def run(self, dispatcher, tracker, domain) -> List[EventType]:


class ActionAnalyseSymptoms(Action):
    def name(self):
        return "action_analyse_symptoms"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        # symptom1 = tracker.get_latest_entity_values("symptom1")
        # symptom2 = tracker.get_latest_entity_values("symptom2")
        # symptom3 = tracker.get_latest_entity_values("symptom3")
        # analysis_inputs = [symptom1, symptom2, symptom3]
        # outputs = analysis_tool(analysis_inputs)
        output = "mild cold"
        dispatcher.utter_messege(text="well,")
        dispatcher.utter_messege(text=tracker.get_latest_entity_values("contact_name"))
        dispatcher.utter_messege(text="you might have")
        dispatcher.utter_messege(text=output)
        dispatcher.utter_messege(
            text="However, we still highly recommend that you go visit a specialist. As we are not legally allowed to give diagnoses."
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
