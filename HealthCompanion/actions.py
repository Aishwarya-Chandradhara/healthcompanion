from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class GE_API:
    def search(self, info):
        return "pharmacyLocation, etc."


class ActionSearchPharmacy(Action):
    def name(self):
        return "action_search_pharmacy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for a pharmacy near you")
        restaurant_api = GE_API()
        restaurants = restaurant_api.search(tracker.get_slot("pharmacy"))
        return [SlotSet("matches", restaurants)]

class ActionSearchClinic(Action):
    def name(self):
        return "action_search_pharmacy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="looking for a pharmacy near you")
        restaurant_api = GE_API()
        restaurants = restaurant_api.search(tracker.get_slot("pharmacy"))
        return [SlotSet("matches", restaurants)]


class ActionSuggest(Action):
    def name(self):
        return "action_suggest"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="here's what I found:")
        dispatcher.utter_message(text=tracker.get_slot("matches"))
        dispatcher.utter_message(
            text="is it ok for you? hint: I'm not going to find anything else :)"
        )
        return []
