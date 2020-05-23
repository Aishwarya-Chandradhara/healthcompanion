from rasa_sdk import Action
from rasa_sdk.events import SlotSet


def search(institution_type, contact_location, dispatcher):
    """
    Suggest a pharmacy in the proximity to contact_location
    :param dispatcher:
    :param institution_type:
    :param contact_location:
    :return:
    """
    if institution_type == "pharmacy":
        institution_name = "City Pharmacy"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12323457890"
        dispatcher.utter_message(text="Found a {} named {} on {}. The contact number is {}".format(institution_type,
                                                                                                   institution_name,
                                                                                                   institution_address,
                                                                                                   institution_phone))
        return [SlotSet("institution_name", institution_name),
                SlotSet("institution_address", institution_address),
                SlotSet("institution_phone", institution_phone)]
    else:
        # for all other institutions
        institution_name = "City Hospital"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12332227890"
        dispatcher.utter_message(text="Found a {} named {} on {}. The contact number is {}".format(institution_type,
                                                                                                   institution_name,
                                                                                                   institution_address,
                                                                                                   institution_phone))
        return [SlotSet("institution_name", institution_name),
                SlotSet("institution_address", institution_address),
                SlotSet("institution_phone", institution_phone)]


def make_appointment(institution_name, contact_name, contact_age, contact_phone, contact_gender, date, time,
                     dispatcher):
    """
    Make appointment in the given hospital for the contact.
    :param dispatcher:
    :param institution_name:
    :param contact_name:
    :param contact_age:
    :param contact_phone:
    :param contact_gender:
    :param date:
    :param time:
    :return:
    """
    appointment_status = "approved"
    dispatcher.utter_message(text="Appointment done for {} in {} for {} {}".format(contact_name,
                                                                                   institution_name, date, time))
    # make a call to some API to actually book the appointment.
    return [SlotSet("appointment_status", appointment_status)]


def diagnose_symptoms(symptom1, symptom2=None, symptom3=None, allergies=None, dispatcher=None):
    """
    Diagnose symptoms and suggest what might be wrong
    :param dispatcher:
    :param symptom1:
    :param symptom2:
    :param symptom3:
    :param allergies:
    :return:
    """
    # symptom1 can't be empty or None
    flu_symptoms = [None, "Headache", "Fever", "Chills", "Cough", "Sore Throat", "Runny Nose", "Fatigue"]
    diarrhea_symptoms = [None, "Nausea", "Bloating", "Loose stools", "Abdominal pain", "Abdominal cramps"]
    diagnosis_results = "I am not sure. Please see a doctor!"

    if symptom1 in flu_symptoms[1:] and symptom2 in flu_symptoms and symptom3 in flu_symptoms:
        diagnosis_results = "Looks like Flu to me"
    elif symptom1 in diarrhea_symptoms[1:] and symptom2 in diarrhea_symptoms and symptom3 in diarrhea_symptoms:
        diagnosis_results = "It looks like you have got Diarrhea"
    dispatcher.utter_message(text="{}".format(diagnosis_results))
    return [SlotSet("diagnosis_results", diagnosis_results)]


def greet_user(contact_gender, contact_name):
    attribute = "handsome" if contact_gender == "Male" else "beautiful"
    if contact_gender == "Male":
        return "Hi {}, Good day! You look {} as ever.".format(contact_name, attribute)


class ActionSearchInstitution(Action):
    def name(self):
        return "action_search_institution"

    def run(self, dispatcher, tracker, domain):
        institution_type = tracker.get_slot("institution_type")
        contact_location = tracker.get_slot("contact_location")

        dispatcher.utter_message(text="Looking for a {} near you!".format(institution_type))

        search(institution_type, contact_location, dispatcher)
        return []


class ActionMakeAppointment(Action):
    def name(self):
        return "action_make_appointment"

    def run(self, dispatcher, tracker, domain):
        contact_name = tracker.get_slot("contact_name")
        contact_age = tracker.get_slot("contact_age")
        contact_gender = tracker.get_slot("contact_gender")
        contact_phone = tracker.get_slot("contact_phone")
        institution_name = tracker.get_slot("institution_name")
        date = tracker.get_slot("date")
        time = tracker.get_slot("time")

        dispatcher.utter_message(text="Making an appointment for you!")

        make_appointment(institution_name, contact_name, contact_age, contact_phone,
                         contact_gender, date, time, dispatcher)
        return []


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
            text="However, we still highly recommend that you go visit a specialist. As we are not legally allowed to give diagnoses")
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
